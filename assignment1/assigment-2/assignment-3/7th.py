def check_even_odd(number):
    if number % 2 == 0:
        return "even"
    else:
        return "odd"

number = int(input("Enter a number: "))
result = check_even_odd(number)

print("The number is ", result)