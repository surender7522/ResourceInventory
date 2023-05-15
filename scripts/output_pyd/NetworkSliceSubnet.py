# generated by datamodel-codegen:
#   filename:  NetworkSliceSubnet.json
#   timestamp: 2023-04-25T03:55:27+00:00

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel


class NetworkSliceSubnet(BaseModel):
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
    nssDescriptorId: Optional[str] = None
    nssDecriptorId: Optional[str] = None
    nssDescriptorName: Optional[str] = None
    nssDescriptorVersion: Optional[str] = None
    nssTemplateId: Optional[str] = None
    nssTemplateName: Optional[str] = None
    nssTemplateVersion: Optional[str] = None
    nssLCMTrackerId: Optional[str] = None
    nssRanCapacity: Optional[str] = None

    class Config:
        allow_population_by_field_name = True
        from pydantic import Extra
        extra = Extra.forbid