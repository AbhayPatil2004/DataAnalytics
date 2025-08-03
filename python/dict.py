dict = {
    "name" : "abhay" ,
    "age" : 20 ,
    "collage" : "kbt"
}

print(dict)
print(dict["name"])

for i in dict :
    print(i)

for i in dict :
    print(dict[i])
    
for x in dict.values():
    print(x)    


for x , y in dict.items():
    print( x , y )

print(dict.get("name"))
a = dict.items()

print(a)

b = dict.keys()
print(b)

c = dict.values()
print(c)

d = dict.copy()
print(d)

x = dict.setdefault("name" , "bavesh")
print(x)

print(dict)

myDict = {
    1 : {
        "name" : "abhay",
        "age" : 20 ,
        "gender" : "Male"
    },
    2 : {
        "name" : "sumit",
        "age" : 20 ,
        "gender" : "Male"
    }
}

print(myDict[1]["name"])