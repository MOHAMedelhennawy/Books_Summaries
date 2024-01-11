#!/usr/bin/python3

import json

json_string = '''
    {
        "students": [
            {
                "id": 1,
                "name": "Mohamed",
                "age": 22,
                "full-time": true
            },
            {
                "id": 2,
                "name": "Mostafa",
                "age": 30,
                "full-time": false
            }
        ]
    }
'''

print(type(json_string))    # => <class 'str'>
print (json_string)
print("=" * 20)

data = json.loads(json_string)  # It takes the JSON string as input and returns a Python object.
print(type(data))   # => <class 'dict'>
print(data['students'][0])  # You can treat with it as a dictionary
                            # note that print "True" with capital 'T', that mean that python obj

print("=" * 20)
# To convert python obj to json string
# Note: That when you convert obj to json string, the data will be messy..
#       so it's helpful to use indent to Arranges data
new_json = json.dumps(data, indent=2, sort_keys=True)
print(type(new_json))
print(new_json)


# ==================================================
# How to deal with .json files?

with open("data.json") as file_obj:
    json_data = json.load(file_obj)

print(json_data)

with open("data2.json", "w") as file_obj:
    json.dump(json_data, file_obj, indent=4, sort_keys=True)




# Note the difference between load, loads and dump, dumps:
#   load(f): load json data from file
#   loads(s): load json data from string 
#   dumb(j, f): write json obj to a file
#   dumbs(j): output json obj as string
# s -> string, j -> json, f -> file
    
# If you have python obj and want to convert to
# json opj, you use json.dumbs(),
# It takes the Python object as input and
# returns a JSON string. and it's call Encoding (Serializing) JSON