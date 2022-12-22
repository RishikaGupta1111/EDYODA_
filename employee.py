import json


employee=[
    {
    "NAME" : "RISHIKA",
    "DOB": "23-03-2000",
    "HIEGHT": "5.3",
    "CITY": "SOLAN",
    "STATE": "HIMACHAL PRADESH"
    },
    {
    "NAME" : "ANIRUDH",
    "DOB": "03-04-2000",
    "HIEGHT": "5.8",
    "CITY": "AMRITSAR",
    "STATE": "PUNJAB"
                
    },
    {
    "NAME" : "ANMOL",
    "DOB": "07-08-1999",
    "HIEGHT": "5.9",
    "CITY": "RAJGRAH",
    "STATE": "HIMACHAL PRADESH"
                
    },
    {
                
    "NAME" : "SAHIL",
    "DOB": "27-09-1999",
    "HIEGHT": "5.11",
    "CITY": "SOLAN",
    "STATE": "HIMACHAL PRADESH"
                

    },
    {
    "NAME" : "VAIBHAVI",
    "DOB": "04-11-1998",
    "HIEGHT": "5.5",
    "CITY": "SHIMLA",
    "STATE": "HIMACHAL PRADESH"
                
    },
    {
    "NAME" : "BHAWNA",
    "DOB": "26-07-1999",
    "HIEGHT": "5.3",
    "CITY": "YAMUNANAGAR",
    "STATE": "HARYANA"
                
        }
    ]





with open("employee.json", "w") as file:
    json.dump(employee, file)


class Employee:
    f = open("employee.json")
    data = json.load(f)

    json_list = json.dumps(data)
    print(json_list)
