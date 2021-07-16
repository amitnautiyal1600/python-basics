number_one =  input("Enter First Number  : ")
number_one = float(number_one)

op = input("Enter Operator : ")

number_two =  input("Enter Second Number  : ")
number_two = float(number_two)

if op == "+" : print( number_one + number_two)
elif op == "-" : print( number_one - number_two)
elif op == "*" : print( number_one * number_two)
elif op == "/" : print( number_one / number_two)
elif op == "%" : print( number_one % number_two)
elif op == "^" : print( pow(number_one, number_two))
else: print('Invalid Operator !!')