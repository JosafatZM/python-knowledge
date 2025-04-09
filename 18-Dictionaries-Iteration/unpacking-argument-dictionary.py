from ast import arg


def milimetros_cm_a_metros(cm, mm):

    total = (cm / 100.0) + (mm / 1000.0)
    return f"La medida en metros es {total}"

print(format(milimetros_cm_a_metros(3, 3)))

# Espacio 1
print()

mm_cm = {
    "cm": 3,
    "mm": 3
}

print(milimetros_cm_a_metros(**mm_cm))

print("\n----- Ejercicio ------\n")

# Declare a plenty_of_arguments function that accepts two parameters (a and b)
# and an additional **kwargs parameter.
#
# The function should return True if the sum of a, b, and the values of 
# **kwargs is greater than 100. It should return False otherwise.
#
# EXAMPLES:
# plenty_of_arguments(20, 30)                          => False
# plenty_of_arguments(a = 50, b = 75)                  => True
# plenty_of_arguments(a = 50, b = 25, c = 50)          => True
# plenty_of_arguments(a = 25, b = 25, c = 25, d = 25)  => False
# plenty_of_arguments(a = 25, b = 25, c = 25, d = 26)  => True

def plenty_of_arguments(a, b, **kwargs):
    if a + b + sum(kwargs.values()) > 100:
        return True
    else:
        return False

print(plenty_of_arguments(20, 30))
print(plenty_of_arguments(a = 50, b = 75))
