address = "Colinas de santo domingo, Villahermosa, cp 86270"

print(address[0:6])
print(address[0:7])
print(address[0:16])
print(address[8:100])  #en estos casos python te permite poner el 100 y lo toma como si dijeras "desde aqui hasta el final del string"

print("\n")

print(address[-5:-1])
print(address[23:-2])
print(address[-8:49])

print("\n")

print(address[5:]) #From IndexPosition number [] until the end of the string
print(address[13:])
print(address[-10:])

print("\n")

print(address[:10]) #From the bigining until the index position number []
print(address[0:10])
print(address[:32])
print(address[:-3])

print("\n")
 
print(address[:])  #python creates a new object

print("ESPECTACULO"[-4:])