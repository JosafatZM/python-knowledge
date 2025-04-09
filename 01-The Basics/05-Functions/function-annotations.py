# Python is a dinammically typed languaje 
# por que una variable no tiene siempre 
# que estar declarada explicitamente  

# el ( -> str:) singinifica que el valor de retorno sera un str
def word_multiplier(word: str, times: int) -> str:
    return word * times

print(word_multiplier("dog", 5))  
print(word_multiplier(5.7,6))

print(type("hello"))

def hola(numero: int, numero_2: float):
   return numero * numero_2

print(hola(5, 7.98))   