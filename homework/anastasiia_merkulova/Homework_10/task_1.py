def finished(func):
    def wrapper():
     func()
    print('finished')
    return wrapper

@finished
def print_me():
    print('print me')
print_me()