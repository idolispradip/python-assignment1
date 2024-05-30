amount = int(input("Enter the sale price: "))

if amount >= 1000:
    discount = amount * 0.05
else:
    discount = 0

print("Discount: ", discount)