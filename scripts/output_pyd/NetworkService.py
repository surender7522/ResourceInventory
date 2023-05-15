# generated by datamodel-codegen:
#   filename:  NetworkService.json
#   timestamp: 2023-04-25T03:55:43+00:00

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel


class NetworkService(BaseModel):
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
    nsSubType: Optional[str] = None
    nsCreatorid: Optional[str] = None
    nsDayoneconfigstatus: Optional[str] = None
    nsOssparameterstatus: Optional[str] = None
    nsUpgraded: Optional[str] = None
    nsSwversion: Optional[str] = None
    nsEmsstatus: Optional[str] = None
    nsDecommission: Optional[str] = None
    nsIpv4: Optional[str] = None
    nsIpv6: Optional[str] = None
    nsTechnology: Optional[str] = None
    nsPreswversion: Optional[str] = None
    nsNse2eoreferenceid: Optional[str] = None
    nssubType: Optional[str] = None
    nsDescriptorName: Optional[str] = None
    nsDescriptorId: Optional[str] = None
    nsDescriptorVersion: Optional[str] = None
    nsNFVOName: Optional[str] = None
    nslIsSliceAware: Optional[str] = None

    class Config:
        allow_population_by_field_name = True
        from pydantic import Extra
        extra = Extra.forbid