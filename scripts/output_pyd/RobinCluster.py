# generated by datamodel-codegen:
#   filename:  RobinCluster.json
#   timestamp: 2023-04-25T03:55:42+00:00

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel


class RobinCluster(BaseModel):
    id: Optional[str] = None
    href: Optional[str] = None
    name: Optional[str] = None
    displayName: Optional[str] = None
    gId: Optional[str] = None
    uuid: Optional[str] = None
    originid: Optional[str] = None
    type: Optional[str] = None
    baseType: Optional[str] = None
    description: Optional[str] = None
    typeversion: Optional[str] = None
    status: Optional[str] = None
    operatationalState: Optional[str] = None
    administrativeState: Optional[str] = None
    source: Optional[str] = None
    creationTime: Optional[str] = None
    creatorid: Optional[str] = None
    modificationTime: Optional[str] = None
    modifierid: Optional[str] = None
    category: Optional[str] = None
    vendor: Optional[str] = None
    domain: Optional[str] = None
    specificationId: Optional[str] = None
    isDeleted: Optional[str] = None
    isEntity: Optional[str] = None
    metaParam: Optional[str] = None
    rcClusterId: Optional[str] = None
    rcVRId: Optional[str] = None
    rcMgmtIPV4: Optional[str] = None
    rcMgmtIPV6: Optional[str] = None
    rcServiceIP: Optional[str] = None
    rcE2EOUUID: Optional[str] = None
    rcClusterNumber: Optional[str] = None
    rcBuildVersion: Optional[str] = None
    rcCalicoIP: Optional[str] = None
    rcBMaaSUUID: Optional[str] = None
    rcApplicationTag: Optional[str] = None
    rcConfigVersion: Optional[str] = None
    rcRobinVIP: Optional[str] = None
    rcRobinVersion: Optional[str] = None
    rcInstallType: Optional[str] = None
    rcZonceID: Optional[str] = None
    rcHealth: Optional[str] = None
    rcDataCenterType: Optional[str] = None
    rcDataCenterId: Optional[str] = None
    rcCPUAvail: Optional[str] = None
    rcMemoryAvail: Optional[str] = None
    rcStorageAvail: Optional[str] = None

    class Config:
        allow_population_by_field_name = True
        from pydantic import Extra
        extra = Extra.forbid