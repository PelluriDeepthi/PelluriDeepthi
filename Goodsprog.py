#Program to calculate the gst of goods
product = input("Enter the product name:")
sp_cost = float(input("Enter the price of the product:"))
gst_rate = float(input("Enter the GST percentage:"))
cgst = sp_cost * ((gst_rate/2)/100)
mrp_price = sp_cost + gst_rate + cgst
print("The price is:", mrp_price)
