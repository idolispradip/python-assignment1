def calculate_sum_average(numbers):
    total = sum(numbers)
    average = total / len(numbers)
    return total, average
numbers = []
for i in range(10):
    num = float(input(f"Enter number {i+1}: "))
    numbers.append(num)

total, average = calculate_sum_average(numbers)

print("Sum of the numbers is :", total)
print(f"Average of the numbers is :", average )
