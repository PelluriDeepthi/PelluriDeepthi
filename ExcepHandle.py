while(True):
    itemName = input("Enter the item name:")
    itemID = input("Enter the item ID:")
    itemQty = int(input("Enter the item quantity:"))
    itemPrice = float(input("Enter the price of the item:"))
    nextItem = input("Do you want to enter the new record: Y/N")
    if (nextItem=='y' or nextItem=='Y'):
        continue
    else:
        break