def  finish_me(func):
    def wrapper():
        func()
        print('finished') # additional action
    return wrapper


@finish_me
def hello():  # finish_me(hello)
    print('print me')

hello()
