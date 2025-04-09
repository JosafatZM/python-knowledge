# def count_down_from(number):
#     start = number
#     while start > 0:
#         print(start)
#         start -= 1

# usando recursion => Cuando invocas una funcion dentro de si misma
def count_down_from(number):
    if number <= 0:
        return

    print(number)
    count_down_from(number - 1)


count_down_from(5)