#Interate two list simultaneously
def iterate_simu(list1, list2):
    for item1, item2 in zip(list1, list2):
        print(item1, item2)
list1 = [4, 5, 6]
list2 = ['a', 'b', 'c']
iterate_simu(list1, list2)