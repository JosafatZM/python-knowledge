#  def p(text):
#      print(text)

#  p("hello")
#  p("good bye")


# def suma(a, b):
#     print("la suma de", a, "y", b, "es", a + b)

#  suma(3,5)
#  suma(34,8493)

# def easy_money():
#     return 100

# def best_food_ever():
#         return "Sushi"
  
# Define a convert_to_currency function thath acepts a 
# single parameter (an integer)
# the function should convert the argument to a string,
# prefix it with a dollar sing, and return the result.
#
#EXAMPLES
#convert_to_currency(15)  => "$15"
#convert_to_currency(8)   => "$8"

def convert_to_currency(money):
    return "$" + str(money)

print(convert_to_currency(5))
print(convert_to_currency(8))
