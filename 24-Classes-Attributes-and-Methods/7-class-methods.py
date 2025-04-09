# It is a method that is invoked directly on the class rather than an instance of it.
# The @classmethod decorator placed above a method in a class body designates it as a class method..

class SushiPlatter():

    def __init__(self, salmon, tuna, shrimp, squid) -> None:
        self.salmon = salmon
        self.tuna = tuna
        self.shrimp = shrimp
        self.squid = squid

    @classmethod
    def lunch_special_A(cls): # cls is a comunity convention for class
        return cls(salmon = 5, tuna = 0, shrimp = 3, squid = 0)
    
    @classmethod
    def gym_bro_special(cls):
        return cls(salmon = 5, tuna = 5, shrimp = 0, squid = 0)
    
# one way to initiate the class is 
Juan = SushiPlatter(salmon= 1, tuna= 1, shrimp= 3, squid= 2)
print(Juan.salmon)

print() # Space

# using class methods 
Josa = SushiPlatter.gym_bro_special()
print(Josa.salmon)
print(Josa.tuna)

print() # Space

Arkua = SushiPlatter.lunch_special_A()
print(Arkua.salmon)
print(Arkua.tuna)

print("\n ----- Ejercicio -----\n")# Ejercicio
# Define a Chocolate class that accepts and assigns a cacao_content attribute.

# Define a "sweet" class method that returns a 
# Chocolate object with a cacao_content value of 30.

# Define a "semisweet" class method that returns a 
# Chocolate object with a cacao_content value of 50.

# Define a "bittersweet" class method that returns a 
# Chocolate object with a cacao_content value of 70.

# Define a "bitter" class method that returns a 
# Chocolate object with a cacao_content value of 99.

class Chocolate():

    def __init__(self, cacao_content) -> None:
        self.cacao_content = cacao_content

    @classmethod
    def sweet(cls):
        return cls(cacao_content = 30)
    
    @classmethod
    def semisweet(cls):
        return cls(cacao_content = 50)
    
    @classmethod
    def bittersweet(cls):
        return cls(cacao_content = 70)
    
    @classmethod
    def bitter(cls):
        return cls(cacao_content = 99)



CarlosV = Chocolate.sweet()
print(CarlosV.cacao_content)