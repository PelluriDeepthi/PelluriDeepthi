import numpy as np

array1D = np.array([1,5])
arrayrange = np.arange(6,30,2)
onesarray = np.ones((1,3,2),dtype=int) # 1 number in 3r nd 2c
#we have given 3dim. In 3rd it has 1 item
oneslikearray = np.ones_like((1,3,2),dtype=int)
zeroarray = np.zeros((3,2),dtype=float) # 0 number in 3r,2c
zeroslikearray = np.zeros_like((3,2),dtype=float)
myarray = np.linspace(5,20,20)
randomarray = np.random.random(4)
sortedarray = np.sort(arrayrange,axis=0) #array sorting in ascending order
#axis=0 ---> column, axis=1--->row  : for sorting


onesarray[0,1] = 3 #in zero row 1st colomn change number to 3
#onesarray[1,1] = 5 #in 1st row 1st column change number to 5

identitymatrixarray = np.eye(3,dtype=int) #for identity we use eye()

print("The array is:"array1D)
print(arrayrange)
print("\n",onesarray)
print(onesarray.ndim)
print(onesarray.shape)
print("\n",oneslikearray)
print("\n",zeroarray)
print(zeroarray.ndim)
print(zeroarray.shape)
print("\n",zeroslikearray)
print("\n",myarray)
print(myarray.ndim)
print(myarray.size)
print("\n",randomarray)
print(randomarray.ndim)
print("\n",sortedarray)
print("\n", onesarray)
print("\n",identitymatrixarray)
