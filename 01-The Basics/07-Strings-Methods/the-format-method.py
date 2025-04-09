#nNMname, adjetive, noun 
mad_libs = "{} laughed at the {} {}."

print(mad_libs.format("Bobby","green", "lion"))
print(mad_libs.format("Josa", "yellow", "church"))

print("\n")

mad_libs = "{2} laughed at the {0} {1}."

print(mad_libs.format("Bobby","green", "lion"))
print(mad_libs.format("Josa", "yellow", "church"))

mad_libs = "{name} laughed at the {adjetive} {noun}."

print(mad_libs.format(name = "Bobby",adjetive ="green", noun = "lion"))
print(mad_libs.format( name ="Josa", noun = "yellow", adjetive ="church"))

name = input("Enter a namer: ")
adjetive = input("Enter an adjetive: ")
noun = input("Enter a noun: ")

print(mad_libs.format(name=name, noun=noun, adjetive=adjetive))