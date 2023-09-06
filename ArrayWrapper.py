import numpy as np
import array
class myArray(array.array):
    arraymember1 = np.array([1,3,4,5])
    arraymember2 = np.array([2,4,5,6])
    def array_addition(self):
        resultarray = self.arraymember1 + self.arraymember2
        print("This array addition function returns the result array \n")
        return resultarray

arrayObj = myArray('u')
arrayObj.arraymember1 = np.array([[1,2,3,4],[34,54,36,67]])
arrayObj.arraymember2 = np.array([[2,38,95,26],[32,23,89,75]])
resultarray = arrayObj.array_addition()
print(resultarray)