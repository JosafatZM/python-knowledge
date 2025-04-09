# Higuer Order Function 
# a function that either accepts a function as an argument or returns a function 
# as a return value 

def one():
    return 1

print(type(one))

# First space
print()

# Definig functions
def add(a, b):
    return a + b

def substract(a, b):
    return a - b

# Defining the HOF - Higher Order Function 
def calculate(func, a, b):
    return func(a, b)

# printing the higuer order function (HOF)
print(calculate(add, 5, 6))
print(calculate(substract, 10, 11))

# Second Space
print()

# Josafat's idea of a HOF
def add_ten(func, a, b): 

    # Adding 10 to our normal function result
    total = func(a, b) + 10
    return total 

# Printing Josafat's HOF
print(add_ten(add, 10, 10))


# Define an invoke_thrice function.
# it should accept a sigle argument (wich will be a fucntion)
# In it's body, the invoke_thrice should invoke
# the fucntion that's passed in exactly three times
print("\n-----Ejercicio-----\n")

def invoke_thrice(func):
    func()
    func()
    

def function():
    print("CA")
    print("CA")

invoke_thrice(function)

# Las Space
print()

print(invoke_thrice(function))
# print(invoke_thrice(function)) --> if I do this at the 
#                                    end i will get a 'none'
#                                    Why?, idk!

print()


def multiply(a, b):

  return a * b



def divide(a, b):

  return a / b



def calculate(func, a, b):
    return func(a, b)



print(calculate(multiply, 10, 5))




















#hola este soy yo escribiendo una carta de amor en un IDE de programación (nada más
#josa que escribir una carta de amor en un IDE).
#Que te puedo decir sigo enamorado de ella, extraño poder contarle las cosas
#especiales que me pasan o simplemente contarle como va mi dia pero creo que eso 
#no es amar a alguien, amar a alguien no es depender emocionalmente de la
#atencion que la persona pone sobre ti pero... aunque debo aceptar que aveces odio esa 
#concepcion de la dependecia emocional ya que no todo en esta vida es dependencia emocinal
#a mi me gusta mucho el saber que tengo a alguien que le importa las cosas que estoy haciendo 
#al final sabemos que necesitamos de un otro para que nos de significado si nadie se
#interesa en lo que hacemos entonces, cual es el significado de lo que hacemos?!? y
#por qué lo hacemos?!?, yo se y estoy de acuerdo que en el sentido aristocratico mi 
#felicidad no puede depender de alguien más pero mi felicidad no dependia de ella,
#desde que no hablo con ella igual he llegado a 
#tener momentos felices pero eso no quiere decir que no extrañe esas noches en 
#las que nos contabamos las cosas que haciamos y hablabamos de las metas que 
#teniamos en la vida, ya ni siquiera se si tus sueños y metas siguen siendo los 
#mismos o si tu cancion favorita sigue siendo la misma, se que se supone que 
#seguimos siendo amigos pero siento que cada vez se siente mas como si no quisieramos
#saber nada el uno del otro y acepto que yo he creado esa concepcion y he llevado a que la realcion
#se sienta de esa manera, desde el momento en que no te he vuelto a mandar mensaje
#pero no lo hago porque no quiera sino porque no quiero molestarte y llegar a ser
#incomodo para ti, no es como que piense decir cosas que no van pero siento que el 
#el hecho de querer saber como estas puede llegar a entenderse como algo egoista de
#mi parte, ¿Por que rayos querria el saber de mi si ya le deje muy en claro que no
#quiero que nuestra relacion vaya mas allá que una amistad? y siendo sinceros yo 
#despues de todo lo que pasó no quiero ser solo tu amigo pero entiendo que el momento
#no es el correcto y no se si algún dia lo sera asi que prefiero aislarme en mis 
#pensamientos y aceptar que nada va a pasar y comenzar a aceptar que a veces las personas 
#son momentaneas.
#Vaya mierda que es la vida!!, pero debo aprender a aceptarlo y quedarme con los bellos
#e inolvidables momentos que pase a tu lado. la vida ha sido muy rara desde que no 
#hablamos y no solo por el hecho de que ya no hablamos si no por el hecho de que siento
#que perdi una de las mejores amistades que he tenido en mi vida y en verdad se siente
#de la chingada, el cariño que sentia por ella era en verdad muy real y viniendo de 
#alguien como yo, que detesta a todo mundo en secreto excepto por un redusido número de
#persona (si estas leyendo esto es porque eres de ese redusido numero de personas que amo)
#es muy real lo que sentia por ella, esa admiracion que sentia por ella, 
#ese sentimiento que tenia todos los dias deseando que le fuera bien en todo lo que 
#hiciera era tan grande y es tan indescriptible que en verdad no puedo ponerlo en palabras
#ese sentimiento de orgullo y admiracion conjugado con amor solo me hacia desearle lo
#mejor siempre, pero me quedaré con esas ganas tan grandes de estar a su lado.
#en verdad la admiraba y se me hace muy loco ese sentimiento de admiracion combinado con amor,
#justo ahora tengo a dos parejas junto a mi y no dimensionas el nivel de envidia que siento 
#(jajajajaa en el buen sentido ojalá les vaya bien)
#porque el amor es un maldito milagro el hecho de encontrar
#una persona que te quiera y ademas los dos esten en el momento correcto para estar juntos
#es a lo que verdaderamente llamo un maldito sueño. amo escribir del amor es de mis cosas
#favoritas en la vida por que despues vuelvo en el tiempo y leo como me sentia en estos
#momentos y disfruto mucho y me alegro el saber que a lo largo de mi vida he sentido y 
#he disfrutado mucho la vida sintiendo aunque las cosas no siempre salen como uno las planea
#el sentir es lo que le da sentido a la vida. Gracias amor por existir y demostrarme que
#existe algo por lo cual seguir viviendo esta vida y a esa persona especial que he hizo
#sentir todo esto. Gracias en verdad gracias jamás olvidare lo bello y real que senti el
#haberte amado.
