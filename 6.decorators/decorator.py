def hello():
    print('hello world')


def dec(h):
    def wrap():
        h()
        print('New decorator')

    return wrap


g = dec(hello)

g()
