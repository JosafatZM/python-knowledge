print(len ("python"))
print(len ("programacion"))
print(len ("&$/$"))
print(len (" "))
print(len (""))

print("josafat" + " zamora")

print("josafat" " zamora")

print("----" * 45)

#Tarea 

def long_word(text):
    return len(text) >= 7

print(long_word("python"))

def longer_than_second(a,b):
    return len(a) > len(b)

print(longer_than_second("hola mi amor","hola mi amor"))