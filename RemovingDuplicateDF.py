import pandas as pd
d = pd.read_excel('C:\\Users\\ADMIN\\Desktop\\Deepu\\dupdf.xlsx')   #takes only xlsx file format
df = pd.DataFrame(d)
print(df)
print(df.duplicated())
print(df.drop_duplicates())