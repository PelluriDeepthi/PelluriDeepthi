import os
f = open("tenthchar.txt", "r")
item = list(f.readlines())
print(item[0])
f.close()