if 5 > 3:
    print("yup that is true, this will be printed")
    print("hi this is another line")

if 6 > 10:
    print("nope that is false. it will never be printed")   

if "josa" == "josa":
    print("awesome name")

if "DAVE" == "dave":
    print("no thats false")

if "dave" != "Dave":
    print("haha yeah got you to print")

if True:
    print("always true, always print")    

if False:
    print("never true means never print")


# Tarea even_or_odd
  
def par_impar(numero):
    if numero & 2 == 0:
        return "even"

    return "odd"        

print(par_impar(3)) 

print()

# josa mode
def truethy_or_falsy(argument):
    if argument == False:
       return f"The value {argument} is falsy"    
       

    return f"The value {argument} is truthy"

print(truethy_or_falsy(0))
print(truethy_or_falsy("hello"))

# elegant mode

def thruthy_or_falsy(value):
    if bool(value):
        return f"The value {value} is truthy"
        
    return f"The value {value} is falsy"  