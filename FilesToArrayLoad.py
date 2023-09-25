import numpy as np
itemsDataArray = np.loadtxt("C:\\Users\\ADMIN\\Desktop\\Deepu\\ItemDetails.txt", skiprows=1, dtype=int)
itemsDataArrayGen = np.genfromtxt("C:\\Users\\ADMIN\\Desktop\\Deepu\\ItemDetails.txt", dtype=int)
print("The itemDataArray is:\n", itemsDataArray)
print("The itemDataArrayGen details is:\n", itemsDataArrayGen)


# To run this piece of code, we have to add , in the text file
ItemCode, ItemQty, ItemPrice = np.loadtxt("C:\\Users\\ADMIN\\Desktop\\Deepu\\ItemDetails.txt", skiprows=1, unpack=True, dtype=int, delimiter=',')
print("The ItemCode Array is:\n", ItemCode)
print("The ItemQty Array is:\n", ItemQty)
print("The ItemPrice Array is:\n", ItemPrice)

# To run this piece of code, we have to add , in the text file
itemArray1, itemArray2, itemArray3, itemArray4 = np.loadtxt("C:\\Users\\ADMIN\\Desktop\\Deepu\\ItemDetails.txt", skiprows=1, dtype=int, delimiter=',')
print("The item1 Array is:\n", itemArray1)
print("The item2 Array is:\n", itemArray2)
print("The item3 Array is:\n", itemArray3)
print("The item4 Array is:\n", itemArray4)

print("The item4 Array in reverse order is:", itemArray4[::-1])
np.savetxt("C:\\Users\\ADMIN\\Desktop\\Deepu\\ItemDetails.txt", itemArray3[::-1])


itemsDataArray[1][2] = 111111
print("The itemData Array is:\n", itemsDataArray)
np.savetxt("C:\\Users\\ADMIN\\Desktop\\Deepu\\ItemDetails.txt", itemsDataArray)
updateArray = np.loadtxt("C:\\Users\\ADMIN\\Desktop\\Deepu\\ItemDetails.txt", dtype=int)
print("The updated Array from text file is:\n", updateArray)