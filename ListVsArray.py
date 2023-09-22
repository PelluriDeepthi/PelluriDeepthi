import time

import numpy as np
myList = list(range(1000000))
start_time = time.time()
result_python = myList*28
end_time = time.time()
print("The time taken for list is:", end_time-start_time)

myArray = np.array(range(1000000))
start_time = time.time()
result_python = myList*28
end_time = time.time()
print("The time taken for array is:", end_time-start_time)