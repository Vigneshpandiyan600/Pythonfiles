# collections package 

from collections import deque

list1 = deque([1,2,3,4])
list1.append(6)
list1.appendleft(-9)

print(list1)
print(list1.pop())
print(list1.popleft())

# OrderedDict

# from collections import OrderedDict

# od = OrderedDict()

# od['a'] = 1
# od['b'] = 2
# od['c'] = 3
# od['d'] = 4

# print (od)

# for key, value in od.items():
# 	print(key, value)

# print("\nAfter deleting")
# od.pop('c')
# print(od)

# defaultdict 

# from collections import defaultdict 

# vehicle = defaultdict(lambda: 'Train')
# vehicle['vicky'] = 'SkodA'
# vehicle['vinod'] = 'Benz'

# print(vehicle)
# print(vehicle['vicky'])
# print(vehicle['sasi'])

# #Counter

# from collections import Counter 

# list1 = [11,22,33,44,11,22,33,77]
# print(Counter(list1))

#namedtuple
#Like dictionaries they contain keys
#that are hashed to a particular value. But on contrary,
#it supports both access from key value and iteration,
#the functionality that dictionaries lack.

# from collections import namedtuple 

# student = namedtuple('student',['name', 'age', 'DOB'])
# S = student('Vicky', '29', '18FEB1990')

# print("The student age using index is : ", end = "")
# print(S[1])

# print("The student name using keyname is : ", end = "")
# print(S.name)

# print("The student DOB using getattr() is : ", end = "")
# print(getattr(S, 'DOB'))

# #frozenset
# #Sets are mutable but frozen sets are immutable,
# #both are unorder and can't accept duplicate values

# Fav_subject = ["OS", "DBMS", "Python"]
# f_subject = frozenset(Fav_subject)
# print(f_subject)

# student = {"name": "Vicky", "age": "29", "gender": "Male"}
# key = frozenset(student)
# print('The frozen set is :', key)

# from array import array

# arr1 = array('i', [1,2,3,4])
# print(arr1)

# for val in arr1:
# 	print(val)

# arr1.append(5)
# print(arr1)

# arr1.extend([90,30,46])
# print(arr1)
# arr1.reverse()
# print(arr1)
# print(arr1.pop())
# print(arr1.tolist())

# print(arr1[2])

# arr1.insert(0,10)
# print(arr1)
# print(arr1.count(3))


list1 = ["vicky", "sasi", "karthi"]
for i, m in enumerate(list1	, 1):
	print(i,m)

# list1.sort()
# print(list1)

new_sorted = sorted(list1)
print(list1)
print(new_sorted)

 

# line1 = "Today is Tuesday"
# line2 = "Tomorrow is wednesday"

# for cmn in line1.split():
#   for cmn1 in line2.split(): 
#       if cmn == cmn1:
#       # if cmn != cmn1:
#           print (cmn)




