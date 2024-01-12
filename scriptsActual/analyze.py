from 3gppnrm import *
import inspect
enumlist=[]
sliceobjlist=[]
def getattributes(obj):
    # print(f"getattributes {obj}")
    if "enum" in str(type(obj)) or "typing" in str(type(obj)):
        if obj not in enumlist:
            enumlist.append(obj)
        return {}
    return obj.__annotations__

def gettype(clsstr):
    # print(f"gettype {clsstr}")
    if "constr" in clsstr or "conint" in clsstr or "Union" in clsstr or "confloat" in clsstr:
        return "str"
    # while "Optional[" in clsstr or "List[" in clsstr:
    #     clsstr=clsstr.split('[')[1].strip("]")
    clsstr=clsstr.split('[')[-1].strip(']')
    return clsstr

def loadtype(clstype):
    # print(f"loadtype {clstype}")
    return globals()[clstype]

imp_items=["NetworkSliceSingle", "MnS11",
           "NetworkSliceSubnetSingle",
           "EPTransportSingle",
           "NetworkSliceSubnetProviderCapabilitiesSingle",
           "FeasibilityCheckAndReservationJobSingle",
           "NetworkSliceControllerSingle",
           "NetworkSliceSubnetControllerSingle",
           "IsolationProfileSingle"]
filenames=['nrcellrelation',
           'nrfrequency',
           'mnsagent',
           'subnetwork',
           'externalnrffunction',
           'udrfunction',
           'top',
           'extensions',
           'FiveQiDscpMappingSet',
           'udmfunction',
           'externalgnbcucpfunction',
           'eutrancellrelation',
           'n3iwffunction',
           'externaleutrancell',
           'externalupffunction',
           'types',
           'pcffunction',
           'smffunction',
           'rimrsset',
           'nrsectorcarrier',
           'ep',
           'cpciconfigurationfunction',
           'trace',
           'rp',
           'nfprofile',
           'sliceprofile',
           'serviceprofile',
           'externalgnbcuupfunction',
           'amfregion',
           'types',
           'neffunction',
           'eutranetwork',
           'dmrofunction',
           'ausffunction',
           'rrmpolicy',
           'externalamffunction',
           'seppfunction',
           'externalservinggwfunction',
           'nssffunction',
           'node',
           'qmcjob',
           'amfset',
           'beam',
           'yams',
           'danrmanagementfunction',
           'cesmanagementfunction',
           'dynamic5qiset',
           'README.md',
           'nrffunction',
           'predefinedpccruleset',
           'nroperatorcelldu',
           'dlbofunction',
           'filemanagement',
           'function',
           'control',
           'externalgnbdufunction',
           'externalseppfunction',
           'lmffunction',
           'nfservice',
           'bwpset',
           'ep',
           'element',
           'bwp',
           'ecmconnectioninfo',
           'common',
           'externalnssffunction',
           'commonbeamformingfunction',
           'udsffunction',
           'dpciconfigurationfunction',
           'files',
           'upffunction',
           'nrcellcu',
           'affunction',
           'smsffunction',
           'managementdatacollection',
           'gnbcuupfunction',
           'desmanagementfunction',
           'eutranfrequency',
           'dnfunction',
           'GtpUPathQoSMonitoringControl',
           'nrcelldu',
           'QFQoSMonitoringControl',
           'configurable5qiset',
           'mnsregistry',
           'networkslice',
           'drachoptimizationfunction',
           'ngeirfunction',
           'operatordu',
           'anlffunction',
           'externalnrcellcu',
           'networkslicesubnet',
           'eutranfreqrelation',
           'nrnetwork',
           'gnbcucpfunction',
           'scpfunction',
           'gnbdufunction',
           'nrfreqrelation',
           'externalenbfunction',
           'measurements',
           'amffunction',
           'fm',
           'nwdaffunction']
dont_traverse=["str", "float", "int", "bool","datetime"]
outerlist=[]

def traverse(item,space):
    cls=loadtype(item)
    clsattrs=getattributes(cls)
    for k,v in clsattrs.items():
        print(space*'\t'+f"{k}: {v}")
        if gettype(v) not in dont_traverse and gettype(v) not in imp_items:
            if gettype(v).lower() not in filenames:
                traverse(gettype(v),space+1)
            elif gettype(v) not in sliceobjlist:
                sliceobjlist.append(gettype(v))

for item in imp_items:
    print(f"Analyzing {item}================")
    traverse(item,0)
    print("--------------------------------")
print(enumlist)
print(sliceobjlist)
for item in sliceobjlist:
    print(f"Analyzing {item}================")
    traverse(item,0)
    print("--------------------------------")