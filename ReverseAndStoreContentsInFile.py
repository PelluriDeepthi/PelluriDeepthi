f1 = open("C:\\Users\\ADMIN\\Desktop\\Deepu\\outputrevfile.txt", "w")
with open("C:\\Users\\ADMIN\\Desktop\\Deepu\\revfile.txt", "r") as myfile:
    data = myfile.read()
data1 = data[::-1]
f1.write(data1)
f1.close()