data = ['mike', 'john', 'sam',  'ram', 'shyam']

print("\nList data items are : ")
print(data)

print("\nRam Index Number is  : ")
print(data.index('ram'))

print("\n First value of list is : ")
print(data[0])

print("\n Last value of index is : ")
print(data[-1])

print('\n After adding new data in list : ')
data.append('test')
print(data)

print('\n After removing  data from list : ')
data.remove('sam')
print(data)

print("\n Count of a data in a list : ")
print( data.count('ram') )

print("\n Make copy of list : ")
data_new = data.copy()
print(data_new)

print("\n Reverse a list : ")
data_new.reverse()
print(data_new)
print(data_new[::-1])

print("\n Sort list in ascending order : ")
data_new.sort()
print(data_new)



