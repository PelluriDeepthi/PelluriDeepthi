import pandas as pd
weekDict = {1:"Monday", 2:"Tuesday", 3:"Wednesday", 4:"Thursday", 5:"Friday", 6:"Saturday", 7:"Sunday"}
dictPandas = pd.Series(weekDict)
print("The series created from Dictionary is:\n", dictPandas)

dictPandas.index = ["day1", "day2", "day3", "day4", "day5", "day6", "day7"]
print("The selected days is:\n", dictPandas[["day1", "day6"]])


dictPandas[1:4] = "Sunday"
print("The selected days is:\n", dictPandas)
# 1-3 elements are replaced by Sunday
