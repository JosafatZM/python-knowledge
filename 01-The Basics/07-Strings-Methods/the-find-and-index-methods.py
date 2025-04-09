browser = "google chrome"

print(browser.find("c"))
print(browser.find("ch"))
print(browser.find("o"))
print(browser.find("g"))
print(browser.find("x"))
print(browser.find("chrome"))
print(browser.find("google"))

print()

print(browser.find("o"))
print(browser.find("o",3))

print("ch" in browser)

print(browser.index("h")) 

print()
#Tarea rfind()

text = "mi casa es tu casa"
x = text.rfind("casa")
print(x)

print()

texto = "hola mi amor como estas?"
print(texto.rfind("a"))

palabra = "Amo programar y me gustaria ser muy bueno"
print(palabra.rfind("o"))
print(palabra.find("o"))

# El metodo rfind() busca la ultima aparicion
# de un valor especificado y te da la index position