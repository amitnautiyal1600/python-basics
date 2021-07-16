## IF statements

is_male = True
is_tall =  False

if is_male :
    print('You are a male')

if is_tall :
    print('your are tall')
else : 
    print('you are short')


if is_male or is_tall : 
    print('you are tall  or you are a male')


## if else

if is_male and is_tall : 
    print('you are tall male')
elif  is_male  and not(is_tall):
    print('you are mail')
elif is_tall and not(is_male) :
    print ('you are tall')
else :
    print('neither male nor tall')