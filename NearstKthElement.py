mylist = [(3, 4), (78, 76), (2, 3), (9, 8), (19, 23)]
print("The original list is:" +str(mylist))
tup = (17, 23)

k = 1
res = min(range(len(mylist)), key = lambda sub : abs(mylist[sub][k - 1] - tup[k - 1]))
print("The nearest tuple near to Kth index element is:" +str(mylist[res]))