# generated by datamodel-codegen:
#   filename:  K8_POD.json
#   timestamp: 2023-04-25T03:55:46+00:00

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel


class K8POD(BaseModel):
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
    k8pod_clusterId: Optional[str] = None
    k8pod_nodehostname: Optional[str] = None
    k8podCtime: Optional[str] = None
    k8podUtime: Optional[str] = None
    k8podMemory: Optional[str] = None
    k8podCpuCores: Optional[str] = None

    class Config:
        allow_population_by_field_name = True
        from pydantic import Extra
        extra = Extra.forbid