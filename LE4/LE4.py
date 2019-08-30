Appliances = ("oven", "refrigerator", "coffee maker", "rice cooker")
# Add 3 indispensable appliances to this tuple


# Way One:
# Appliances = Appliances + ("Stove", "Microwave", "Toaster")

# print(Appliances)

#Way Two:
Appliances = set(Appliances)
Appliances.update(["dishwasher", "microwave", "toaster"])
Appliances = tuple(Appliances)
print(Appliances)