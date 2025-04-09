def be_nice(fn):
    def inner(*args, **kwargs):
        print(r"Nice to meet you! I'm honored to execute for you!")
        fn(*args, **kwargs)
        print("It was my pleasure to execute your function!")

    return inner

@be_nice
def complex_function(stakeholder, position):
    print(f"Something complex for our {position} {stakeholder}!")

complex_function('Josafat', 'CEO')