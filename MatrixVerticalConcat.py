import numpy as np
test_list = [["Today", "Good"], ["is", "Day"], ["a"]]
max_len = max(len(sublist) for sublist in test_list)

# Pad the sublist with empty strings to make them the same length
padded_list = [sublist + [''] * (max_len - len(sublist)) for sublist in test_list]

arr = np.array(padded_list)
arr_trans = arr.T
res = [''.join(row) for row in arr_trans]
print("List after column concatanation:", str(res))