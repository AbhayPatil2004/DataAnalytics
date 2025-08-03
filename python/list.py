a  = [ "apple" , "mango" , "banana"]
print(a)

print(a[0])
print(a[-1])
print(a[1:3])
print(a[-1:-3:-1])
print(a[-3:-1])

# List iteration 

for i in a :
    print(i)

for i in range ( 0 , len(a)):
    print(a[i])

i = 0 
while( i < len(a) ):
    print(a[i])
    i += 1     

# list function

print(len(a))

print(a.count("apple"))

a.append("Lichi")
print(a)

a.insert(1 , "Vision")
print(a)

a.remove("Vision")
print(a)

print(a.pop(2))

b = a.copy()

print(a.index("mango"))

a.extend(b)
print(a)

print(a.reverse())
print(a)
print(a.sort())
print(a)