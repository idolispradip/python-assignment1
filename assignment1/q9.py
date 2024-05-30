#replace the list Item with new Value if Found
def replace_List_item(lst, last_value, first_value):
    for i in range(len(lst)):
        if lst[i] == last_value:
            lst[i] = first_value
    return lst
List = [1, 2, 3, 4, 5]
New_list = replace_List_item(List, 3, 10)
print(New_list) 