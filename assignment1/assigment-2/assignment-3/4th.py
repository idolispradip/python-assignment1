amount = float(input("Enter the sale price: "))

if amount >= 1000:
    discount = amount * 0.05
else:
    discount = amount * 0.03

print("Discount:", discount)
