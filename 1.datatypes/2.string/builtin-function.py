data_string = "my name is Amit Nautiyal"


#  capitalize()	Converts the first character to upper case

new_string  = data_string.capitalize()

print( new_string )
print('\n')

#  title()	Converts the every first character to upper case

new_string  = data_string.title()

print( new_string )
print('\n')

# casefold()	Converts string into lower case

new_string  = data_string.casefold()
print( new_string )
print('\n')

# center()	Returns a centered string

new_string  = data_string.center(50)
print( new_string )
print('\n')

# count()	Returns the number of times a specified value occurs in a string

new_string = "Hi my name is amit Hi"

new_string = new_string.count("Hi")
print(new_string)
print('\n')

# encode()	Returns an encoded version of the string

new_string = "Hi my name is amit Hi"

new_string = new_string.encode()
print(new_string)
print('\n')