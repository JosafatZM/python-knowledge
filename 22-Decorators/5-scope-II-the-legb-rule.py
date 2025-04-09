# LEGB
# local/ Enclosing functions/ Global/ Built-in.


# Global Scope

def outer():
    x = 10

    # Enclosing function Scope

    def inner():
        x = 5
        
        # Local Scope
        return x 
    return inner()

# Examples

print(outer())

# Global Scope

def out():

    # Enclosing function Scope

    def inside():
        
        # Local Scope
        return len# --> Built-in Scope

    return inside()

print(out()('Josafat'))