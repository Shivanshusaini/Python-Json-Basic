import jmespath 
#used for Data Extraction 

j = {
    "people": [{"name": "Abhi", "age": 22},
               {"name": "Abhiv", "age": 24}
               ]
    }

f= jmespath.search("people[*].age", j)
print(f)