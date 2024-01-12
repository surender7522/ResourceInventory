file_path="TS28541_SliceNrm.py"
output="a.py"
with open(file_path, 'r') as file1, open(output, 'w') as file2:
    count=0
    file2.write("from pydantic import validator, ValidationError\n")
    for line in file1:
        # count=count+1
        # if count > 50:
        #     break
        if "Field(..., m" in line:
            file2.write(line.split("...")[0]+")\n")
            varname=line.split(":")[0].strip()
            minitems=-1
            maxitems=-1
            if "min_items" in line:
                minitems=int(line.split("min_items=")[1].split(')')[0])
                file2.write(f"    @validator('{varname}')\n")
                file2.write(f"    def validate_min_items_{varname}(cls, value):\n")
                file2.write(f"        min_items_required = {minitems}\n")
                file2.write("        if len(value) < min_items_required:\n")
                file2.write("            raise ValidationError(f'Minimum {min_items_required} items required in my_list')\n")
                file2.write("        return value\n")
            if "max_items" in line:
                maxitems=int(line.split("max_items=")[1].split(",")[0])
                file2.write(f"    @validator('{varname}')\n")
                file2.write(f"    def validate_max_items_{varname}(cls, value):\n")
                file2.write(f"        max_items_required = {maxitems}\n")
                file2.write("        if len(value) > max_items_required:\n")
                file2.write("            raise ValidationError(f'Minimum {max_items_required} items required in my_list')\n")
                file2.write("        return value\n")
        else:
            file2.write(line)



