single_line_string = "Hello this is a string."

print('Print type of string =>')
print(type(single_line_string))

print('Print var value =>')
print(single_line_string)


## multi line asignment

muti_line_string = """This is a multiline string,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""


print('multi line string')
print(muti_line_string)




# String store as a array so we can access them as using index

new_string = 'Amit Nautiyal'

print(new_string[0])
print(new_string[1])


# Since strings are arrays, we can loop through the characters in a string, with a for loop.

for x in new_string :
	print(x)


# To get the length of a string, use the len() function.


print( 'The length of single line string is => {}'.format(len(single_line_string)) )
print( 'The length of muti line string is => {}'.format(len(muti_line_string)) )
print('The length of new string ( {} ) is => {}'.format(new_string, len(new_string)))


#To check if a certain phrase or character is present in a string, we can use the keyword in

print('amit' in new_string)

print('Amit' in new_string)


if 'Nau' in new_string :
	print('exist')
else :
	print('Not exist')



#To check if a certain phrase or character is NOT present in a string, we can use the keyword not in.

print('Amit' not in new_string)

if 'Test' not in new_string :
	print('Not Exist')
else :
	print('Exist')