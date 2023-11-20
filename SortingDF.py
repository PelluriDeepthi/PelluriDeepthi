import pandas as pd
d = pd.read_excel("C:\\Users\\ADMIN\\Desktop\\Deepu\\dupdf.xlsx")
df = pd.DataFrame(d)
print(df.sort_values('Gender'))
print(df.sort_values('Age'))
print(df.sort_values('Age', ascending=False))