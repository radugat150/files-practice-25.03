import csv

# total=0
# with open("data/products-1000.csv", "r", encoding="utf-8") as file:
#     reader= csv.reader(file)
#     next(file)
#     for row in reader:
#         if row[11] = "in_stock":
#             price = float(row[5])
#             stock = int (row[7])
#             total = price * stock
# print (f"The total value is {total}")


# total=0
# with open("data/products-1000.csv", "r", encoding="utf-8") as file:
#     reader= list (csv.DictReader(file))
#     for row in reader:
#         print (f"{row["Index"]} {row["Name"]}")
# print (f"The total value is {total}")

# total=0
# with open("data/products-1000.csv", "r", encoding="utf-8") as file:
#     reader= list (csv.DictReader(file))
#     prices = []
#     for row in reader:
#         if row[11]=="in_stock":
#             prices.append(float(row[5]))
#             total+=float(row[5])
# print (f"Average is {total/len(prices)}, max value in {max(prices)}")

# with open("data/data.json", "r", encoding="utf-8") as file:
#     user_data=json.load(file)
#     # for element in user_data:
#     #     if element["state"] == "California":
#     #         total+=1
#     dictionary = {i for i in user_data if i["state"] == "California"}
#     print (list_ca)
#     print(f"The amount of Californians {len(list_ca)}, out of {len(user_data)}")


# from tkinter import filedialog
# filepath= filedialog.asksaveasfilename()

total=0
with open("data/data.json", "r", encoding="utf-8") as file, \
        open("data/data-ca.json", "w", encoding="utf-8") as data:
    user_data=json.load(file)
    list_ca = {i for i in user_data if i["state"] == "California"}
    json.dump(list_ca, dest, indent=4)
    print (list_ca)
    print(f"The amount of Californians {len(list_ca)}, out of {len(user_data)}")

