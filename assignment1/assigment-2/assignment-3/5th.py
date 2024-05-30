amount = float(input("Enter the sale price: "))

if amount >= 5000:
    discount = amount * 0.01
if amount >=4000:
    discount = amount * 0.07
if amount >=3000:
    discount = amount * 0.05
if amount >=2000:
    discount = amount * 0.03
else:
    discount = amount * 0.02

print("Discount:", discount)
