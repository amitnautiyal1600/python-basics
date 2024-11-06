'''
Decorator are function that takes another function as an argument and extends its behavior without modifying it directly.
'''
def func():
    print('hello world')

def dec(func):
    def wrap():
        print('New decorator')
        func()
    return wrap

g = dec(func)
g()


# two decorator in same function
def welcome(func):
    def wrap():
        print('welcome')
        func()
    return wrap

def end(func):
    def wrap():
        func()
        print('by by ')
    return wrap


@end
@welcome
def hello():
    print('hello')

hello()


# decorator with argument
def arg_deco(*args, **kwargs):
    def deco_func(func):
        def wrap():
            print(f" argument passed in deco {args}")
            print(f" argument passed in deco {kwargs}")
            print('inside deco')
            func()
        return wrap
    return deco_func
    

@arg_deco(1,2,3, name="Amit", age=30, place="Rishikesh")
def normal_func():
    print('noram function')

normal_func()
