def check_palindrome(data_string):
    data_string = data_string.lower()
    print('\n')
    if data_string == data_string[::-1]:
        print('The text is palindrome')
    else:
        print('The text is not palindrome')


data_string = 'malayalam'

check_palindrome(data_string)

data_string = 'amitnautiyal'

check_palindrome(data_string)
