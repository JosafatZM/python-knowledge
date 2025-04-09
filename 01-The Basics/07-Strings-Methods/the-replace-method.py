phone_number = "555 555 1234"

print(phone_number.replace(" ","-"))
print(phone_number.replace("5","4"))

# TAREA
def fancy_cleanup(string):
    return string.strip().replace("j","c").replace(" ","!")

print(fancy_cleanup("          josa que cosa"))