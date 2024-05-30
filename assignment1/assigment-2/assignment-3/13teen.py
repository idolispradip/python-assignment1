def sum_of_digits(number):
    total = 0
    while number > 0:
        digit = number % 10
        total += digit
        number //= 10
    return total
number = int(input("Enter a number: "))
result = sum_of_digits(number)

print("The sum of the digits of number is:", result)