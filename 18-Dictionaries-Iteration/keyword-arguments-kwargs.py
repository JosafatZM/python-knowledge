# What is a keyword-argument:
# is the one where we provide the name of the parameter along
# wiht is argument whenever we invoke a function


# Example of a keyword-argument

def example(word):
    return len(word)

print(example(word = "Hola Mundo"))

#Espacio 1
print()

# **kwards indicate that this collect keyword arguments function can
# accept any number of keyword parameters and keyword arguments

def collect_keyword_argument(**kwards):
    print(kwards)
    print(type(kwards))

    for key, value in kwards.items():
        print(f"The value is {key} and the key is {value}")

collect_keyword_argument(A = 1, B = 2, C = 3, D = 4)

# Espacio 2
print()

# The community call this things "arns"
def args_and_kwards(a, b, *args, **kwards):
    print(f"The sum of a + b is: {a + b}")
    print(f"The sum of the tuple arg is: {sum(args)}")
    print(kwards)
    print(args)
    
    total_sum_of_dict_values = 0
    for value in kwards.values():
        total_sum_of_dict_values += value
    
    print(f"The sum of the kwards is: {total_sum_of_dict_values}")

args_and_kwards(1, 2, 3, 4, 5, x = 6, y = 7, z = 8)

# Ejemplo 
# Espacio 3
print()

def my_func(a, b, *args, **kwargs):
  print(kwargs)
  print(args)
 
my_func(b = 5, a = 10, c = 15)

# Espacio 4
print()

def my_func(a, b, *args, **kwargs):
  print(kwargs)
  print(args)
 
my_func(20, 30, 40, 50)

# Espacio Final 
print()

# Lo que pasa si no pones positional arguments
def a(a, b, c, **kwargs):
  return kwargs

print(a(1, 2, 3))