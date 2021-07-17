
data_list = ['Mike', 'John', 'Doe',  'Jack', 'Matt']


print('Data List :')
print(data_list)
print('\n')

print('Add new data in list :')
data_list.append('Chris')
print(data_list)
print('\n')

print('After removing  data_list from list : ')
data_list.remove('Matt')
print(data_list)
print('\n')

#  The extend() method does not have to append lists, you can add any iterable object (tuples, sets, dictionaries etc.).

new_list = ["Jane", "Calir", "Maya"]


data_list.extend(new_list)
print('New extended List')
print(data_list)
print('\n')

#  The remove() method removes the specified item.

data_list.remove('Maya')
print(data_list)
print('\n')

#  The pop() method removes the specified index.

data_list.pop(0) #remove from 0 index
print(data_list)
print('\n')

data_list.pop()  # remove from last
print(data_list)
print('\n')

#  The clear() method empties the list.
new_list = data_list.copy()
print(new_list)
new_list.clear()
print(new_list)
print('\n')
#  del delete  the list by index

del data_list[0]
print(data_list)
print('\n')

#  Delete complete list

del data_list  
