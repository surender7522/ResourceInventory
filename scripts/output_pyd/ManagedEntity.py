# generated by datamodel-codegen:
#   filename:  ManagedEntity.json
#   timestamp: 2023-04-25T03:55:30+00:00

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel


class ManagedEntity(BaseModel):
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
    meHostname: Optional[str] = None
    mePhysicalhostName: Optional[str] = None
    meNeId: Optional[str] = None
    meFMEMSId: Optional[str] = None
    mePMEMSId: Optional[str] = None
    meCMEMDId: Optional[str] = None
    meSubType: Optional[str] = None
    meSwVersion: Optional[str] = None
    meBuildVersion: Optional[str] = None
    meLicense: Optional[str] = None
    meState: Optional[str] = None
    meEMSstatus: Optional[str] = None
    meMgmtIPV4: Optional[str] = None
    meMgmtIPV6: Optional[str] = None
    meFQDN: Optional[str] = None
    meStage: Optional[str] = None
    meSecured: Optional[str] = None
    meOnAirDate: Optional[str] = None
    meTechnology: Optional[str] = None
    meRole: Optional[str] = None

    class Config:
        allow_population_by_field_name = True
        from pydantic import Extra
        extra = Extra.forbid