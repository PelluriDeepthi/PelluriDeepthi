import numpy as np

myArray = np.array([[1, 3, 4, 5], [7, 3, 4, 2], [3, 2, 6, 8]])

unique_items, item_counts = np.unique(myArray, return_counts=True)

unique_items_not_repeated = unique_items[item_counts == 1]  # ==1 means if item is returned 1 time it takes, if repeated doesn't take
print("Unique items not repeated:", unique_items_not_repeated)

#numpy.unique() with the return_counts=True parameter returns both the unique items and their corresponding counts.
#Then, by filtering the unique_items based on item_counts being equal to 1, you'll get only the unique items that are not repeated in the array.

