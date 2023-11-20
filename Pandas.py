import pandas as pd
my_list = [30, 20, 50, 48]
a = pd.Series(my_list)
print(a)
d = {'name': ['Vaishnavi', 'Deepthi', 'Pelluri'], 'percentage': [72, 90, 61]}
print(pd.DataFrame(d))