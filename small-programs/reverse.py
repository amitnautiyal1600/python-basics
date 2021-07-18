data_string = 'Hi My Name Is Amit Nautiyal'
print('Data string is : {}'.format(data_string))
print('\n')

reverse_string =  data_string[::-1]
print('Reverse complete string is : {}'.format(reverse_string))
print('\n')


# Reverse the seq of word only 

new_data_list = data_string.split()
print('changes string in list is : {}'.format(new_data_list))
print('\n')
 

reverse_data_list =  new_data_list[::-1]
list_to_string = ' '.join(reverse_data_list) 
print('Reverse string is : {}'.format(list_to_string))
print('\n')