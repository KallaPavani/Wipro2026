import json

data={
    "Name":"Pavani",
    "Age":20,
    "Skills":[
        "python",
        "java"
    ]
}

with open("data.json","w") as file:
    json.dump(data,file,indent=4)