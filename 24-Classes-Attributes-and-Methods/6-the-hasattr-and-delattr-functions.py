# hasattr = returns true if an attribute exists on an object
# delattr = deletes an attribute on an object
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

print(bbq.size)

stats_to_delete = ["size", "price", "color", "spiciness", "cost"]

for stat in stats_to_delete:
    if hasattr(bbq, stat):
        delattr(bbq, stat)

# print(bbq.size)