#Add new Item to a List After a Specified Item
def add_new_item(lst, insert_after, new_item):
    index = lst.index(insert_after)
    lst.insert(index + 1, new_item)
    return lst
my_list = ['pradip', 'hari', 'ram']
List = add_new_item(my_list, 'hari', 'sita ')
print(List) 