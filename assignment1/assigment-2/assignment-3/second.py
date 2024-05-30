def sum1(num1, num2):
    return num1 + num2

def main():
    number1 = float(input("Enter the first number: "))
    number2 = float(input("Enter the second number: "))
    result = sum1(number1, number2)
    print("The sum of {number1} and {number2} is: ", result)
main()
