#the let us get or set the value of an 
# attribute on an object without the use
# of DOT syntax


stats = {
    'name' :'BBQ sauce',
    'price' : 19.99, 
    'size' : 'Extra large', 
    'ingredients' : ['Chicken', 'Onions', 'BBQ sauce']
}

class Pizza():

    def __init__(self, stats) -> None:
        for key, value in stats.items():
            setattr(self, key, value)


bbq = Pizza(stats)

print(bbq.name)
print(bbq.ingredients)

#Space
print()

for attr in ["price", "name", "diameter", "discounted"]:
    # (The object,  the attribute whose value should be extracted, default fallback value to return if attribute doesn't exist)
    print(getattr(bbq, attr, "Unknown")) 
    
#Space
print()
# different ways to use it

# guardas en un diccionario todos los atributos de un metodo 
def get_attributes(method):
    params = {}
    for k in dir(method): # dir: sirve para obtener los atributos
        params[k] = getattr(method, k)

    return params

print(get_attributes(len))