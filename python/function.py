def hello():
    print("Hello World")
hello() 


def add( a , b ):
    return a + b 

print(add(10,20))
    
def func(*name):
    print(name) 


print(func("abhay","patil"))

a = lambda b : b * 5 
print(a(5))

x = lambda y , z : y * z 
print(x(10,20))

