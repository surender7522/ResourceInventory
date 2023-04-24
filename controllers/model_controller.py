from fastapi import APIRouter, HTTPException, types
from fastapi import Request, status
from fastapi.exceptions import RequestValidationError
from api_models.get_resource import Resource
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from scripts.output_pyd import *
from services.graph_service import add_node, add_rel, get_node_by_id
model_router = APIRouter()

def validator(res:Resource):
    ch={}
    for i in res.entityCharacteristics:
        ch[i.name]=i.value
    print(ch)
    if res.type == "Bundle":
        Bundle.Bundle(**ch)
    elif res.type == 'Package':
        Package.Package(**ch)
    elif res.type == 'GeographicArea':
        GeographicArea.GeographicArea(**ch)
    elif res.type == 'GeoLocation':
        GeoLocation.GeoLocation(**ch)
    elif res.type == 'SliceProfile':
        SliceProfile.SliceProfile(**ch)
    elif res.type == 'ServiceProfile':
        ServiceProfile.ServiceProfile(**ch)
    elif res.type == 'LogicalLink':
        LogicalLink.LogicalLink(**ch)
    elif res.type == 'Service':
        Service.Service(**ch)
    elif res.type == 'User':
        User.User(**ch)
    elif res.type == 'PODInterface':
        PODInterface.PODInterface(**ch)
    elif res.type == 'LogicalInterface':
        LogicalInterface.LogicalInterface(**ch)
    elif res.type == 'K8_POD':
        K8_POD.K8_POD(**ch)
    elif res.type == 'Server':
        Server.Server(**ch)
    elif res.type == 'DC':
        DC.DC(**ch)
    elif res.type == 'Tenant':
        Tenant.Tenant(**ch)
    elif res.type == 'IPPool':
        IPPool.IPPool(**ch)
    elif res.type == 'NetworkElement':
        NetworkElement.NetworkElement(**ch)
    elif res.type == 'SideCar':
        SideCar.SideCar(**ch)
    elif res.type == 'VLAN':
        VLAN.VLAN(**ch)
    elif res.type == 'K8_Service':
        K8_Service.K8_Service(**ch)
    elif res.type == 'VNFC_R':
        VNFC_R.VNFC_R(**ch)
    elif res.type == 'Fabric':
        Fabric.Fabric(**ch)
    elif res.type == 'VLANInterface':
        VLANInterface.VLANInterface(**ch)
    elif res.type == 'VM':
        VM.VM(**ch)
    elif res.type == 'NetworkService':
        NetworkService.NetworkService(**ch)
    elif res.type == 'PerfReq':
        PerfReq.PerfReq(**ch)
    elif res.type == 'ServiceInterface':
        ServiceInterface.ServiceInterface(**ch)
    elif res.type == 'VNFC':
        VNFC.VNFC(**ch)
    elif res.type == 'NELocation':
        NELocation.NELocation(**ch)
    elif res.type == 'RobinCluster':
        RobinCluster.RobinCluster(**ch)
    elif res.type == 'GeoSubLocation':
        GeoSubLocation.GeoSubLocation(**ch)
    elif res.type == 'Role':
        Role.Role(**ch)
    elif res.type == 'ManagedEntity':
        ManagedEntity.ManagedEntity(**ch)
    elif res.type == 'WDM':
        WDM.WDM(**ch)
    elif res.type == 'GenericEntity':
        GenericEntity.GenericEntity(**ch)
    elif res.type == 'Switch':
        Switch.Switch(**ch)
    elif res.type == 'BundleClusterMapping':
        BundleClusterMapping.BundleClusterMapping(**ch)
    elif res.type == 'CNFC':
        CNFC.CNFC(**ch)
    elif res.type == 'Connection':
        Connection.Connection(**ch)
    elif res.type == 'Location':
        Location.Location(**ch)
    elif res.type == 'Cluster':
        Cluster.Cluster(**ch)
    elif res.type == 'LogicalResource':
        LogicalResource.LogicalResource(**ch)
    elif res.type == 'ClusterRole':
        ClusterRole.ClusterRole(**ch)
    elif res.type == 'Entity':
        Entity.Entity(**ch)
    elif res.type == 'PerfMetricJob':
        PerfMetricJob.PerfMetricJob(**ch)
    elif res.type == 'Router':
        Router.Router(**ch)
    elif res.type == 'VNF_R':
        VNF_R.VNF_R(**ch)
    elif res.type == 'PhysicalLink':
        PhysicalLink.PhysicalLink(**ch)
    elif res.type == 'RPool':
        RPool.RPool(**ch)
    elif res.type == 'NetworkSlice':
        NetworkSlice.NetworkSlice(**ch)
    elif res.type == 'CNF':
        CNF.CNF(**ch)
    elif res.type == 'NetworkSliceSubnet':
        NetworkSliceSubnet.NetworkSliceSubnet(**ch)
    elif res.type == 'ClusterVLAN':
        ClusterVLAN.ClusterVLAN(**ch)
    elif res.type == 'VNF':
        VNF.VNF(**ch)
    elif res.type == 'ThresholdMonitor':
        ThresholdMonitor.ThresholdMonitor(**ch)
    elif res.type == 'DCPod':
        DCPod.DCPod(**ch)
    elif res.type == 'ThresholdInfo':
        ThresholdInfo.ThresholdInfo(**ch)
    elif res.type == 'Party':
        Party.Party(**ch)
    else:
        raise Exception("Not valid type")

@model_router.get("/api/v1/hello")
async def get_hello():
    return {"message": "Hello World!"}


@model_router.get("/api/v1/resource/{id}")
async def get_resource_id(id: str):
    try:
        records = get_node_by_id(id)
    except RequestValidationError as e:
        return JSONResponse(content=jsonable_encoder({"detail": e.errors()}), status_code=status.HTTP_422_UNPROCESSABLE_ENTITY)
    except Exception as e:
        return JSONResponse(content=jsonable_encoder({"detail": e.__repr__()}), status_code=status.HTTP_422_UNPROCESSABLE_ENTITY)
    return JSONResponse(content=jsonable_encoder({"detail": records}), status_code=status.HTTP_200_OK)


@model_router.get("/api/v1/resource")
async def get_resource(fields: str  = None, offset: str  = None, limit: str  = None):
    return {"message": "Hello World! {0} {1} {2}".format(fields, offset, limit)}


@model_router.post("/api/v1/resource/{id}")
async def post_resource(id: str, resource: Resource ):
    try:
        validator(resource)
        add_node(resource)
    except RequestValidationError as e:
        return JSONResponse(content=jsonable_encoder({"detail": e.errors()}), status_code=status.HTTP_422_UNPROCESSABLE_ENTITY)
    except Exception as e:
        return JSONResponse(content=jsonable_encoder({"detail": e.__repr__()}), status_code=status.HTTP_422_UNPROCESSABLE_ENTITY)
    return {"message": "Hello World! {0} ".format(resource)}


@model_router.patch("/api/v1/resource/{id}")
async def patch_resource(id: str, resource: str  = None):
    return {"message": "Hello World! {0} ".format(resource)}