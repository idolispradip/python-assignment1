def sum_of_evens(numbers):
    return sum([number for number in numbers if number % 2 == 0])

numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sum_evens = sum_of_evens(numbers_list)
print("Sum of even numbers:", sum_evens)