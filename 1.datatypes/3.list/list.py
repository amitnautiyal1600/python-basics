#  List is Mutable  we can change it or modify it any time

# List items are ordered, changeable, and allow duplicate values.

#  A list can contain different data types: list1 = ["abc", 34, True, 40, "male"]



data_list = ['mike', 'john', 'sam',  'ram', 'shyam']

print("\nList data_list items are : ")
print(data_list)

print("\nRam Index Number is  : ")
print(data_list.index('ram'))

print("\nFirst value of list is : ")
print(data_list[0])

print("\nLast value of index is : ")
print(data_list[-1]) 

print("\nCount of a data_list in a list : ")
print( data_list.count('ram') )

print("\nMake copy of list : ")
data_list_new = data_list.copy() # this will make a copy
data_list_new2 = data_list # pint same list object
print(data_list_new)
print(data_list_new2)

print("\nReverse a list : ")
data_list_new.reverse()
print(data_list_new)
print(data_list_new[::-1])

print("\nSort list in ascending order : ")
data_list_new.sort()
print(data_list_new)



