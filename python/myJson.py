# import json 

# a = {
#     "cname" : "python" ,
#     "fees" : 12000 ,
#     "duration" : "2"
# }

# x = json.loads(a)

# print( type(x))
# print(x)


# import json

# a = {"name": "Abhay"}
# x = json.dumps(a)  # Correct: dict -> JSON string
# print(x)


import json 
student = { "name" : "abhay" , "age" : 20 , "marks" : 100 }
# data = json.dumps(student)
# print(type(data))
# print(data)

# Age = json.loads(student)
# print(Age["age"])

data = json.dumps(student , indent=4 , separators=",")
print(data)