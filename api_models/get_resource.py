from typing import ForwardRef
from typing import Optional, Literal
from typing import List

from pydantic import BaseModel, Field

Resource=ForwardRef("Resource")
class EntityCharacteristics(BaseModel):
    name: str
    value: str

class EntitySpecificationRef(BaseModel):
    id: str
    href: str
    type: str

class EntityRelationship(BaseModel):
    type: str
    entity: Resource

class Resource(BaseModel):
    id: str
    href: str
    entitySpecificationRef: Optional[EntitySpecificationRef]
    source: str
    version: str
    type: str = Field(alias="@type")
    baseType: str = Field(alias="@baseType")
    name: str
    entityCharacteristics: List[EntityCharacteristics] = []
    entityRelationship: List["EntityRelationship"] = []

EntityRelationship.update_forward_refs()