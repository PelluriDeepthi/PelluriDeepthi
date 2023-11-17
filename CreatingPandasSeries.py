import pandas as pd
import numpy as np
sd = pd.Series()
print("Empty pandas series", sd)   #Empty Series

l = [10, 20, 30, 40, 50]
sd = pd.Series(l)
print("Pandas series using list\n",  sd)   #Series using list

sd = pd.Series(l, index=['a', 'b', 'c', 'd', 'e'])
print("Pandas series using indexing\n", sd)   #indexing

a = np.array(l)
print("Array of elements in pandas series", a)

sa = pd.Series(a)
print("Pandas series using array\n", sa)   #Series using array

d = {'a': 10, 'b': 20, 'c': 30}
print("Pandas series using dictionaries\n", pd.Series(d))     #Series using dictionary

dt = [('a', 10), ('b', 20), ('c', 30)]
print("Pandas series using list of tuples\n", pd.Series(dt))    #series using list of tuples