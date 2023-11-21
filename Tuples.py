a = (1, 2, 3, 4, 5)
b = (6, 7, 8, 9, 0)
del a
del b
a = ()
print("The empty tuple:", a)
a = (1,)
print("Tuple:", a)
a = 1, 2, 3, 4
print("Updated tuple:", a)
a = (10, 20, 30, 40)
b = (50, 60, 70, 80)
print("Length of tuple:", len(a))
c = a+b
print("Concatenating tuple:", c)
print("Multiplying tuple a:", a*2)
print("Is 10 in a tuple:", 10 in a)
print("Is 100 in a tuple:", 100 in a)
print("Is 10 not there in tuple a:", 10 not in a)
print("Is 100 not there in tuple a:", 100 not in a)
for ele in a:
    print(ele)
d = max(a)
print(d)
print("The minimum in tuple a is:", min(a))
print("Index at 10 is:", a.index(10))
f = (a*2)
print("Counting no of times 10 appeared:", f.count(10))
mystr = "chair"
print(tuple(mystr))
my_List = [10, 20, 30, 40, 50]
print("List as tuple:", tuple(my_List))