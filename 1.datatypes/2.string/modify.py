data_string = 'Amit Nautiyal'

#  Modify to upper case

print( data_string.upper() )

# Modify to lower string

print( data_string.lower() )

#  Remove white space from begining and last

new_string = '  Space in begin  '

print( len(new_string) )

print( new_string )

new_string = new_string.strip()

print( len(new_string) )

print( new_string.strip() )


#  Replace a string character

print( data_string.replace('A', '@'))

print( data_string.lower().replace('a', '@'))

#  Split a string and covert to a list

split_string = data_string.split()

print( type(split_string) )
print( split_string )