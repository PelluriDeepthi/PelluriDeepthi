import numpy as np

onesarray = np.ones([4,1],dtype=int)
zerosarray = np.zeros([4,2],dtype=int)
concatarray = np.concatenate([onesarray,zerosarray],axis=1)
#dim nd rows should be same

print(onesarray)
print(onesarray.ndim)
print("\n",zerosarray)
print(zerosarray.ndim)
print("\n",concatarray)
print(concatarray.ndim)
print(concatarray.shape)