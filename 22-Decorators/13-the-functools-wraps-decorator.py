import functools

def be_nice(fn):
    @functools.wraps(fn)
    def inner(*args, **kwargs):
        print(r"Nice to meet you! I'm honored to execute for you!")
        result = fn(*args, **kwargs)
        print("It was my pleasure to execute your function!")
        return result

    return inner

@be_nice
def complex_function_sum(a, b):
    "Adds two numbers together"
    return a + b

# print(complex_function_sum(5, 6))
help(complex_function_sum)