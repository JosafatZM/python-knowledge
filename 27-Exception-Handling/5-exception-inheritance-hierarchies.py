class Mistake(Exception):
    pass

class StupidMistake(Mistake):
    pass

class SillyMistake(Mistake):
    pass

try:
    raise StupidMistake("Extra stupid mistake")
except StupidMistake as e:
    print(f"Caught the error: {e}")

# genera un error
# try:
#     raise SillyMistake("Extra silly mistake")
# except StupidMistake as e:
#     print(f"Caught the error: {e}")

try:
    raise SillyMistake("Extra silly mistake")
except Mistake as e:
    print(f"Caught the error: {e}")