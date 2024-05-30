#Turn Every Item of a list into a Square
def square_list(lst):
    return [x ** 2 for x in lst]
List = [1, 2, 3, 4, 5]
squared  = square_list(List)
print(squared) 