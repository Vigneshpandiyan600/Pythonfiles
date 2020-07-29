from collections import ChainMap

dict1 = {'a':1, 'b':4}
dict2 = {'b':5, 'c':7}

cmap = ChainMap(dict1, dict2)
print(cmap)

for i in cmap.maps:
	print(i)

for i in cmap.keys():
	print(i)

for i in cmap.values():
	print(i)