#Removal of Empty Strings from a List of Elements
def remove_empty_(lst):
    return [item for item in lst if item != '']
    
List = ['hello', '', 'world', '', '']
List1 = remove_empty_(List)
print(List1)  