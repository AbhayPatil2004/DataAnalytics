import numpy as np 
import statistics as stats

arr = np.array([[10,20,30,40],[50,60,70,80]])
# arr = np.array([[10,20,30,40],[50,60,70,80],[90,100,110,120],[130,140,150,160]])

# print(arr)
# print(type(arr))

# print(arr[0:2])
# print(arr[2:])
# print(arr[:3])

# print(arr[-3:-1])
# print(arr[-1:])

# print(arr[0:2,0:2])
# print(arr[0,1:2])


# print(arr[0,0])
# print(arr[1,0])

# print(np.shape(arr))

# print(np.size(arr))

# print(np.ndim(arr))

# print(arr.dtype)

# print(arr.shape)

# print(len(arr))

# print(arr.size)

# print(type(arr))

# print(arr.dtype)

# print(arr.astype(float))

# print(arr)

arr1 = np.array([[10,20],[30,40]])
arr2 = np.array([[10,60],[70,80]])

# print(arr1+arr2)
# print(np.add(arr1,arr2))
# print(np.subtract(arr1,arr2))
# print(np.multiply(arr1,arr2))

# print(np.power(arr1,arr2))
# print(np.sqrt(arr1))


# print(np.concatenate([arr1,arr2]))

# print(np.concatenate([arr1,arr2]))

print(np.hstack([arr1,arr2]))
print(np.vstack([arr1,arr2]))

a = np.array([10,20,30,40])
print(np.split(a,4))

print(np.append(a,20))
print(np.append(arr1,20))

print(arr1)

print(np.insert(a,1,100))

print(np.delete(a,1))


print(np.sort(a))
print(np.sort(arr1))

n = len(a)
for i in range ( 0 , n ):
    print(a[i])

s = np.where(a == 10)
print(s)

# print( np.where( a == 10 | a == 20 ))

# fa = [True , False , True , False ]
 
fa = a > 20

newArr = a[fa]

print(newArr)

print( np.sum(a))
print(np.min(a))
print(np.size(a))

print(np.mean(a))

print(np.cumsum(a))

print(np.cumprod(a))

baked_food = [ 200,300,150,130,120,200,170,188,200]

a = np.array(baked_food)

print(np.mean(a))
print(np.median(a))
print(stats.mode(a))

print(np.std(a))
print(np.var(a))

# print(np.corrcoef([arr1,arr2]))