from datetime import datetime

def run(function):
    def wrapper():
        if 17 <= datetime.now().hour < 22:
            return function()
        else:
            return False
    return wrapper()

@run
def say_hello():
    print('hello my friend')