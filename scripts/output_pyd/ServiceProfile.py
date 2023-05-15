# generated by datamodel-codegen:
#   filename:  ServiceProfile.json
#   timestamp: 2023-04-25T03:55:50+00:00

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel


class ServiceProfile(BaseModel):
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
    svcpmaxNumberofUEs: Optional[str] = None
    svcpcoverageArea: Optional[str] = None
    svcplatency: Optional[str] = None
    svcpuEMobilityLevel: Optional[str] = None
    svcpresourceSharingLevel: Optional[str] = None
    svcpavailability: Optional[str] = None
    svcpMaxNumOfConnsCategory: Optional[str] = None
    svcpMaxNumOfConnsTagging: Optional[str] = None
    svcpMaxNumOfConnsExposure: Optional[str] = None
    svcpMaxNumOfConnsNoOfConns: Optional[str] = None
    svcpKPIMonitoringCategory: Optional[str] = None
    svcpKPIMonitoringTagging: Optional[str] = None
    svcpKPIMonitoringExposure: Optional[str] = None
    svcpKPIMonitoringKPIList: Optional[str] = None
    svcpSATCategory: Optional[str] = None
    svcpSATTagging: Optional[str] = None
    svcpSATExposure: Optional[str] = None
    svcpSATAccessTechList: Optional[str] = None
    svcpDTCategory: Optional[str] = None
    svcpDTTagging: Optional[str] = None
    svcpDTExposure: Optional[str] = None
    svcpDTSupport: Optional[str] = None
    svcpDCCategory: Optional[str] = None
    svcpDCTagging: Optional[str] = None
    svcpDCExposure: Optional[str] = None
    svcpDCAvailability: Optional[str] = None
    svcpDCPeriodicityList: Optional[str] = None
    svcpDLTPSCategoryPerSlice: Optional[str] = None
    svcpDLTPStaggingPerSlice: Optional[str] = None
    svcpDLTPSexposurePerSlice: Optional[str] = None
    svcpDLTPSGuaThptPerSlice: Optional[str] = None
    svcpDLTPSMaxThptPerSlice: Optional[str] = None
    svcpDLTPSCategoryPerUE: Optional[str] = None
    svcpDLTPSTaggingPerUE: Optional[str] = None
    svcpDLTPSExposurePerUE: Optional[str] = None
    svcpDLTPSGuaThptPerUE: Optional[str] = None
    svcpDLTPSMaxThptPerUE: Optional[str] = None
    svcpULTPSCategory: Optional[str] = None
    svcpULTPSTagging: Optional[str] = None
    svcpULTPSExposure: Optional[str] = None
    svcpULTPSGuaThpt: Optional[str] = None
    svcpULTPSMaxThpt: Optional[str] = None
    svcpULTPUCategory: Optional[str] = None
    svcpULTPUTagging: Optional[str] = None
    svcpULTPUExposure: Optional[str] = None
    svcpULTPUGuaThpt: Optional[str] = None
    svcpULTPUMaxThpt: Optional[str] = None
    svcpMAXPKSCategory: Optional[str] = None
    svcpMAXPKSTagging: Optional[str] = None
    svcpMAXPKSExposure: Optional[str] = None
    svcpMAXPKSMaxSize: Optional[str] = None
    svcpMaxPDUSCategory: Optional[str] = None
    svcpMaxPDUSTagging: Optional[str] = None
    svcpMaxPDUSExposure: Optional[str] = None
    svcpTDCategory: Optional[str] = None
    svcpTDTagging: Optional[str] = None
    svcpTDExposure: Optional[str] = None
    svcpTDDensity: Optional[str] = None
    svcpactivityFactor: Optional[str] = None
    svcpuESpeed: Optional[str] = None
    svcpjitter: Optional[str] = None
    svcpsurvivalTime: Optional[str] = None
    svcpreliability: Optional[str] = None
    svcpmaxDLDataVolume: Optional[str] = None
    svcpmaxULDataVolume: Optional[str] = None

    class Config:
        allow_population_by_field_name = True
        from pydantic import Extra
        extra = Extra.forbid