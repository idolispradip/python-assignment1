def find_smallest_largest(numbers):
    smallest = min(numbers)
    largest = max(numbers)
    return smallest, largest
numbers = []
for i in range(10):
    num = float(input(f"Enter number {i+1}: "))
    numbers.append(num)

smallest, largest = find_smallest_largest(numbers)

print("The smallest number is:", smallest)
print("The largest number is:", largest)