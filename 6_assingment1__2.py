#    ASSINGMENT 6.1.2
# Create a dictionary of any 7 Indian states and their capitals. Write this into a JSON file.

import json
states_capitals = [
    {
        "HIMACHAL PRADESH" : "SHIMLA",
        "JAMMU AND KASHMIR" : "SHRINAGAR",
        "GOA" : "PANAJI",
        "PUNJAB": "CHANDIGARH",
        "HARYANA" : "CHANDIGARH",
        "UTTRAKHAND" : "DEHRADUN",
        "GUJRAT": "GANDHINAGAR",
        "RAJASTHAN" : "JAIPUR"
    }
]

with open("states.json", "w") as file:          #JSON FILE CREATED
    json.dump(states_capitals, file)

f = open("states.json")                   
data = json.load(f)
    

json_list = json.dumps(data)
print(json_list)



