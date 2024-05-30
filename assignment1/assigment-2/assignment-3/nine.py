def calculate_net_salary(gross_salary):
    if gross_salary < 10000:
        tax_rate = 0
    elif gross_salary <= 19999:
        tax_rate = 0.10
    elif gross_salary <= 39999:
        tax_rate = 0.15
    else:
        tax_rate = 0.20
    
    tax_amount = gross_salary * tax_rate
    net_salary = gross_salary - tax_amount
    
    return net_salary, tax_amount 
    
gross_salary = float(input("Enter the gross salary: "))
net_salary, tax_amount = calculate_net_salary(gross_salary)

print("Gross Salary:", gross_salary)
print("Tax Amount:", tax_amount)
print("Net Salary: ", net_salary)

