data_string = 'Amit nautiyal is a software engineer. amit lives in rishikesh. rishikesh is good place to live'

sub_string_one = 'amit'
sub_string_two = 'Amit'
sub_string_three = 'Nau'
sub_string_four = 'Nauyy'
sub_string_five = 'rishikesh'

# Using Find method iwch return the index of string and if not ound it return -1

def check_substring(data_string, sub_string) :

	print(data_string.find(sub_string))

	if(data_string.find(sub_string) != -1) :
		print('Substring Exist')
	else : 
		print('Substring Not Exist')

	print('\n')


check_substring(data_string, sub_string_one)
check_substring(data_string, sub_string_two)
check_substring(data_string, sub_string_three)
check_substring(data_string, sub_string_four)


# Using count method it return the count how many time substring occer return 0 if not exist

print('*********************************')

def check_substring_two(data_string, sub_string) :

	print(data_string.count(sub_string))

	if(data_string.find(sub_string) != -1) :
		print('Substring Exist')
	else : 
		print('Substring Not Exist')

	print('\n')


check_substring_two(data_string, sub_string_one)
check_substring_two(data_string, sub_string_two)
check_substring_two(data_string, sub_string_three)
check_substring_two(data_string, sub_string_four)
check_substring_two(data_string, sub_string_five)