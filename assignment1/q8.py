#Extend a nested list by adding a Sublist
def _nested_list(nested_list, sublist):
    nested_list.extend(sublist)
    return nested_list
nested_list = [[11, 12], [13, 14]]
sublist = [15, 16]
List = _nested_list(nested_list, sublist)
print(List) 