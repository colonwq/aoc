#!/usr/bin/python3
'''
Solution for Day00 part 1
This is a generic file for all days.
Copy this directory to the new day and part
'''

import sys

def check_record_limits(record):
    '''given a valid record,check all fileds are in valid ranges'''
    limits = {
            "byr": [1920, 2002],
            "iyr": [2010, 2020],
            "eyr": [2020, 2030],
            "hgt": {
                "cm": [150, 193],
                "in": [59, 76]
                },
            "hcl": [0x000000, 0xffffff],
            "ecl": ["amb", "blu", "brn", "gry", "grn", "hzl", "oth" ],
            "pid": 9,
            "cid": 9
            }
    #print("Checking record: %s."% (record))
    fields = {}
    items = record.split(" ")
    for item in items:
        key, value = item.split(":")
        #print("Key: %s Value: %s"%(key, value))
        fields.update({key: value})
        #fields[key] = value
    #print( fields )
    #print("byr: %s", fields["byr"])
    for field in [ "byr", "iyr", "eyr" ]:
        #print("Year: %s"% (fields["byr"]) )
        if len(fields[field]) != 4:
            #print("%s Year not right length" %(field) )
            return 0
        elif not fields[field].isdigit():
            #print("%s Year not digits" %(field))
            return 0
        else:
            year = int(fields[field])
            #print("Part: %s Year: %d"%(field,year))
            #print("Min %d Max: %d" % (limits[field[0]], limits[field[1]]))
            min_max = limits[field]
            min_value = min_max[0]
            max_value = min_max[1]
            #print("Min_max: ", min_max)
            #print("Min %d Max:%d"%(min_value, max_value))
            if not (year >= min_value and year <=max_value):
            #    print("%s Year %d not in range"%(field, year))
                return 0
    field = "hgt"
    value = fields[field]
    if value.endswith("cm"):
        value = int(value.rstrip("cm"))
        #print("%s height %d cm" %(field,value))
        min_max = limits[field]["cm"]
        min_value = min_max[0]
        max_value = min_max[1]
        #print("Min_max: ", min_max)
        #print("Min %d Max %d" % (min_value, max_value) )
        if not (value >= min_value and value <=max_value):
            #print("%s height %d not in range %s"%(field,value, min_max))
            return 0
    elif value.endswith("in"):
        value = int(value.rstrip("in"))
        #print("%s height %d in" %( field, value))
        min_max = limits[field]["in"]
        min_value = min_max[0]
        max_value = min_max[1]
        #print("Min_max: ", min_max)
        #print("Min %d Max %d" % (min_value, max_value) )
        if not (value >= min_value and value <=max_value):
            #print("%s height %d not in range %s"%(field,value, min_max))
            return 0
    else:
        #print("%s bad height" %(field))
        return 0

    field = "hcl"
    value = fields[field]
    if len(value) != 7:
        #print("Hair color not long enough")
        return 0
    if value[0] != "#":
        #print("Hair color not right #")
        return 0
    #print("color %s" %(value))
    value = int(value.lstrip("#"),16)
    #print("color %d" %(value))
    min_value = 0x0
    max_value = 0xffffff
    #print("Min %d Max %d" % (min_value, max_value) )
    if not (value >= min_value and value <=max_value):
        #print("%s hair color not in range" % (field))
        return 0

    field = "ecl"
    value = fields[field]
    #print("Field: %s" %( field))
    #print("Value: %s" %( value))
    #print("Fieled: %s Value: %s" %(field, value))
    colors = limits[field]
    #colors = items[value]
    #print("eye color items ", colors)

    if not (value in colors):
        #print("%s is not a valid eye color" %(value))
        return 0

    field = "pid"
    value = fields[field]
    #print("Field:%s"%(field))
    #print("Type value: ", type(value))
    #print("PID length: %d" %(len(value)))
    if not (value.isdigit()):
        #print("Not a pid valid digets %s (%s)" %(field,value))
        return 0
    if len(value)!=9:
       #print("Not a pid valid length %s (%s)" %(field,value))
       return 0


    return  1

def check_record_fields(record):
    '''Checks each record for needed fileds'''
    needed_fields = [ "byr", "iyr", "eyr", "hgt",
            "hcl", "ecl", "pid" ]
    special_field = ["cid"]
    for field in needed_fields:
        #if record.index(field):
        #    print("Found: %s"% (field) )
        try:
            record.index(field)
        except ValueError as v_e:
            #print("Field new found: %s"%( field ) )
            return 0
    return check_record_limits(record)

def main():
    """Script entry point"""
    #print("Hello World")
    answer = 0
    passports = []

    try:
        file_input = open(sys.argv[1], "r")
    except IndexError as i_exception:
        print("No file given: ", i_exception)
        sys.exit()
    except FileNotFoundError as f_exception:
        print("File not found: ", f_exception)
        sys.exit()

    new_line = ""
    for line in file_input:
        line = line.strip("\n")
        #print("Line: %s(%d)"% (line, len(line)) )
        if len(line) > 0:
            new_line = new_line + " " + line
        else:
            passports.append(new_line.lstrip(" "))
            new_line = ""
    passports.append(new_line.lstrip(" "))
    #print("Passports: ", passports)
    for passport in passports:
        answer += check_record_fields(passport)

    print("WRONG anser: 115")
    print("WRONG anser: 2")
    print("Answer %d" % (answer) )

if __name__ == "__main__":
    main()
