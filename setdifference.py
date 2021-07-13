setA = {1,2,3,4,5}
setB = {3,4,7,8,9}

print(setA - setB)
print(setB - setA)
print(setA.difference(setB))
print(setB.difference(setA))

print(setA ^ setB) #symmetric difference
print(setA.symmetric_difference(setB))
print(setB.symmetric_difference(setA))

