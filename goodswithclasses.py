import os
class Goods:
    def __init__(self, name, price, gst_rate, category):
        self.name = name
        self.price = price
        self.gst_rate = gst_rate
        self.category = category

    def calculate_gst(self):
        gst_amount = ((self.price * self.gst_rate)/100)

        #print("GST amount is:", gst_amount)
        return gst_amount

#Read goods data from the input file
goods_list = []
with open("C:\\Users\\admin\\Desktop\\Deepthi\\goodsinfofile.txt","r") as file:
    lines = file.readlines()

i = 0
while i<len(lines):
    name = lines[i].split(":")[1].strip()
    price = float(lines[i+1].split(":")[1].strip())
    gst_rate = float(lines[i+2].split(":")[1].strip())
    category = lines[i+3].split(":")[1].strip()
    i += 6
    #Move to the next record
    goods = Goods(name, price, gst_rate, category)
    goods_list.append(goods)

#Calculate GST for different categories
categories = {"5%":[], "14%":[], "18%":[]}

for goods in goods_list:
    if goods.category == "5%":
        categories["5%"].append(goods)
    elif goods.category == "14%":
        categories["14%"].append(goods)
    elif goods.category == "18%":
        categories["18%"].append(goods)

#calculated gst data to the output file
with open("C:\\Users\\admin\\Desktop\\Deepthi\\GST_Calculated.txt", "w") as file:
    for category,goods in categories.items():
        file.write(f"category:{category}\n")
        for item in goods:
            gst_amount = item.calculate_gst()
            file.write(f"Name:{item.name}, category: {item.category}, GSTAmount: {gst_amount}, GSTrate: {item.gst_rate}\n")

print("Calculated GST is written to 'GST_calculated.txt'.")


