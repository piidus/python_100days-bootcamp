'''
Instructions
Create a logging_decorator() which is going to log the name of the function that was called, the arguments it was given and finally the returned output.

Expected Output
Unsupported image

HINT 1: You can use function.__name__ to get the name of the function.

HINT 2: You'll need to use *args
'''

def logging_decorator(fn):
    def wrapper(*args, **kwargs):
        print(f"You called {fn.__name__}{args}")
        result = fn(args[0], args[1], args[2])
        print(f"It returned: {result}")
    return wrapper


@logging_decorator
def a_function(a, b, c):
    return a * b * c
    
a_function(1, 2, 3)
