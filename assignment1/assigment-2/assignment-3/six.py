def calculate_interest(balance):
    if balance > 99999:
        interest_rate = 0.07
    elif balance >= 50000:
        interest_rate = 0.05
    else:
        interest_rate = 0.03
    
    interest = balance * interest_rate
    return interest
balance = float(input("Enter the balance: "))
interest = calculate_interest(balance)

print("Balance:", balance)
print("Interest: ", interest)