def welcome_user():
    print("Hello User !!")

print('*****')
welcome_user()
print('*****')

def say_hi(name) : 
    print("Hello " + name)


name =  input('Enter your name : ')
say_hi(name)


def full_data(name, age) : 
    print("hello "+ name + " your age is : " + age)
age =  input('Enter your age : ')
full_data(name, age)


## Return function

def cube(num):
    return num*num*num

print(cube(3))
print(cube(4))