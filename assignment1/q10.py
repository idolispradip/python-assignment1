#Remove all occurances of a Specific Item if Found
def remove_all_occurrence(lst, item_to_remove):
    return [item for item in lst if item != item_to_remove]

my_list = [1, 2, 3, 2, 4, 2, 5]
New_list = remove_all_occurrence(my_list, 3)
print(New_list)  