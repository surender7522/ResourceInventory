# create nodes
payload= {
    "id": "string",
    "href": "string",
    "entitySpecificationRef": {
        "id": "string",
        "href": "string",
        "type": "string"
    },
    "source": "string",
    "version": "string",
    "@type": "CNFC",
    "@baseType": "string",
    "name": "CNFC",
    "entityCharacteristics": [
        {
            "name": "modificationTime",
            "value": "string"
        },
        {
            "name": "creationTime",
            "value": "string"
        },
        {
            "name": "isEntity",
            "value": "string"
        }
    ],
    "entityRelationship": [

    ]
}
all =['Package', 'GeographicArea', 'GeoLocation', 'SliceProfile', 'Bundle', 'ServiceProfile', 'LogicalLink', 'Service', 'User', 'PODInterface', 'LogicalInterface', 'K8_POD', 'Server', 'DC', 'Tenant', 'IPPool', 'NetworkElement', 'SideCar', 'VLAN', 'K8_Service', 'VNFC_R', 'Fabric', 'VLANInterface', 'VM', 'NetworkService', 'PerfReq', 'ServiceInterface', 'VNFC', 'NELocation', 'RobinCluster', 'GeoSubLocation', 'Role', 'ManagedEntity', 'WDM', 'GenericEntity', 'Switch', 'BundleClusterMapping', 'CNFC', 'Connection', 'Location', 'Cluster', 'LogicalResource', 'ClusterRole', 'Entity', 'PerfMetricJob', 'Router', 'VNF_R', 'PhysicalLink', 'RPool', 'NetworkSlice', 'CNF', 'NetworkSliceSubnet', 'ClusterVLAN', 'VNF', 'ThresholdMonitor', 'DCPod', 'ThresholdInfo', 'Party']
print(len(all))
id_dict = {}
for item in all:
    id_dict[item] = []
import httpx
import uuid
for i in all:
    for k in range(30):
        payload["@type"] = i
        payload["name"] = i+" "+str(uuid.uuid4())
        res = httpx.post(url="http://localhost:8000/api/v1/resource", json=payload, timeout=300.0)
        try:
            id_dict[i].append(res.json()["id"])
        except Exception as e:
            print(e.__repr__())
        #print(res.status_code)

print(id_dict)

# link nodes
import os
import json
from graph_service import add_rel
directory = os.fsencode("output_json")
models={}
for file in os.listdir(directory):
    filename = os.fsdecode(file)
    if filename.endswith(".json"):
        print(filename)
        with open("output_json/"+filename, 'r', encoding='utf-8') as infile:
            my_json = infile.read()
            models[filename.split(".json")[0]] = json.loads(my_json)

for k, v in models.items():
    #print(k)
    if k in ["Base"]:
        continue
    item=v["module"]["Base:baseType"]
    attributes=[]
    while item.get("@name"):
        print(item["@name"])
        if models[item["@name"]]["module"]["container"][0].get("leaf"):
            if type(models[item["@name"]]["module"]["container"][0]["leaf"]) == dict:
                attributes.append(models[item["@name"]]["module"]["container"][0]["leaf"])
            else:
                attributes+=models[item["@name"]]["module"]["container"][0]["leaf"]
        item=models[item["@name"]]["module"]["Base:baseType"]
    if v["module"]["container"][0].get("leaf"):
        if type(v["module"]["container"][0]["leaf"]) == dict:
            attributes.append(v["module"]["container"][0]["leaf"])
        else:
            attributes+=v["module"]["container"][0]["leaf"]
    #print(attributes)
    relationships = []
    if v["module"]["container"][1].get("leaf"):
        if type(v["module"]["container"][1]["leaf"]) == dict:
            relationships.append(v["module"]["container"][1]["leaf"])
        else:
            relationships+=v["module"]["container"][1]["leaf"]
    #print(relationships)
    for item in relationships:
        rel=item["type"]["Base:relationship"]["@name"]
        objtype = item["type"]["Base:relType"]["@name"]
        for i in range(len(id_dict[v["module"]["@name"]])):
            try:
                add_rel(id_dict[v["module"]["@name"]][i], v["module"]["@name"],id_dict[objtype][i],objtype, rel)
            except Exception as e:
                print(e.__repr__())