# generated by datamodel-codegen:
#   filename:  VLANInterface.json
#   timestamp: 2023-04-24T11:37:40+00:00

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel


class VLANInterface(BaseModel):
    lifpName: Optional[str] = None
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

    class Config:
        from pydantic import Extra
        extra = Extra.forbid