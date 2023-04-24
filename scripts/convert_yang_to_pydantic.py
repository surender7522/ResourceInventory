import os
import glob
import subprocess
import xmltodict
import json
import copy
'''
Clean up and create xml
'''
# directory = os.fsencode("input_yang")
# files = glob.glob('input_xml/*')
# for f in files:
#     os.remove(f)
# for file in os.listdir(directory):
#     filename = os.fsdecode(file)
#     if filename.endswith(".yang"):
#         print(filename)
#         subprocess.run(["pyang", "-f", "yin", "input_yang/"+filename, "-o", "input_xml/"+filename.split(".yang")[0]+".xml"])

'''
Cleanup and create json
'''
# directory = os.fsencode("input_xml")
# files = glob.glob('output_json/*')
# for f in files:
#     os.remove(f)
# for file in os.listdir(directory):
#     filename = os.fsdecode(file)
#     if filename.endswith(".xml"):
#         print(filename)
#         with open("input_xml/"+filename, 'r', encoding='utf-8') as infile:
#             my_xml = infile.read()
#             output=xmltodict.parse(my_xml)
#             with open("output_json/"+filename.split(".xml")[0]+".json", 'w', encoding='utf-8') as file:
#                 file.write(json.dumps(output))

'''
Create Pydantic models
'''
# Read all jsons into a dict
directory = os.fsencode("output_json")
models={}
for file in os.listdir(directory):
    filename = os.fsdecode(file)
    if filename.endswith(".json"):
        print(filename)
        with open("output_json/"+filename, 'r', encoding='utf-8') as infile:
            my_json = infile.read()
            models[filename.split(".json")[0]] = json.loads(my_json)
#print(models)

# For each item, gather attributes from all its basetypes and populate json, add relationships
codegen_json = {
    "$id": "person.json",
    "$schema": "http://json-schema.org/draft-07/schema#",
    "title": "Person",
    "type": "object",
    "properties": {
    },
    "required": [

    ],
    "definitions": {

    }
}


files = glob.glob('output_json_codegen/*')
for f in files:
    os.remove(f)
files = glob.glob('output_pyd/*')
for f in files:
    try:
        os.remove(f)
    except Exception as e:
        print(e)
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
    _codegen = copy.deepcopy(codegen_json)
    _codegen["$id"]=k+".json"
    _codegen["title"]=k
    properties={}
    required=[]
    for i in attributes:
        _property = {}
        _property["type"] = "string" if i["type"]["@name"]=="string" else "string"
        if _property["type"] == "integer":
            _property["default"] = 0
        if i["mandatory"].get("@value"):
            required.append(i["mandatory"]["@value"])
        if _property:
            properties[i["@name"]]=_property
    _codegen["properties"]=properties
    _codegen["required"]=required
    with open("output_json_codegen/"+k+".json", 'w', encoding='utf-8') as infile:
        infile.write(json.dumps(_codegen))
    subprocess.run(["datamodel-codegen", "--input", "output_json_codegen/"+k+".json", "--input-file-type", "jsonschema", "--output", "output_pyd/"+k+".py"])
files = glob.glob('output_pyd/*')
for f in files:
    try:
        with open(f, 'a', encoding='utf-8') as infile:
            infile.write('''
    class Config:
        from pydantic import Extra
        extra = Extra.forbid''')
    except Exception as e:
        print(e)
_files=[]
for x in files:
    if "__" in x:
        continue
    _files.append(x.split("/")[1].split(".")[0])
with open("output_pyd/"+"__init__.py", 'w', encoding='utf-8') as infile:
    infile.write("__all__ ={0}".format(_files))

with open("output_pyd/"+"all.py", 'w', encoding='utf-8') as infile:
    infile.write("all ={0}".format(_files))


