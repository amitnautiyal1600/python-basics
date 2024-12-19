def greet(name , location ):
    print(f"Hello {name} lives in {location}")

greet('Amit', 'Rishikesh')
greet('Rishikesh', 'Amit')
greet(location='Rishikesh', name='Amit')



def return_fun(name, last_name) :
    f_name = name.title()
    l_name = last_name.title()
    # return f_name + ' ' + l_name
    return f"{f_name} {l_name}"

print(return_fun('AmiT', 'NAUTIYAL'))