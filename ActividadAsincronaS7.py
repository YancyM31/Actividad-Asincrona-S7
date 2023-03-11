print("")
print (" 1) NÚMERO ENTERO (INT)")
print("")
#Multiplicación
print ("MULTIPLICACIÓN DE TRES VARIABLES")
#variables:
v1= 6
v2= 8
v3= 4
print("""El valor de las variables: 
      v1= 6
      v2= 8
      v3= 4""")
multiplicación= v1 * v2 * v3
print ("El resultado de la multiplicación de las tres variables es: ", multiplicación)
print("")

#Realización de la división entera.
print ("DIVISIÓN ENTERA DE DOS VARIABLES")
#variables:
VUno= 10
VDos= 3
print("""EL VALOR DE LAS VARIABLES ES: 
      VUno= 10
      VDos= 3""")
división= VUno // VDos
print("El resultado de la división de las dos variables es: ", división)
print("")

#Suma de los dos resultados
print ("Suma de los resultados")
suma= multiplicación + división
print ("El resultado de la suma de los dos resultados es de: ",suma )
print("")
print ("2) FLOTANTE (FLOAT)")
#Tomamos la variable Exp2 como exponente de la variable Exp1.
print ("VARIABLES EXPONENCIALES")
Exp1= 3
Exp2= 5
print ("""El valor de las variables exponenciales es de:
    Exp1= 3
    Exp2= 5""")
TotalExp= Exp1 ** Exp2
print ("El resultado exponencial es de: ",TotalExp)
print ("")
#Creamos dos variables y cálculamos su porcentaje.
print("VARIABLES DE MÓDULO")
Mod1= 20
Mod2= 8
print ("""El valor de las variables es de:
       Mod1= 20
       Mod2= 8""")
TotalMod= Mod1 % Mod2
print("El resultado del módulo es: ", TotalMod)
print("")
#realizamos la resta del resultado exponencial menos el resultado de módulo.
print("RESTA DE LOS RESULTADOS")
resta= TotalExp - TotalMod
print("El resultado de la resta es de: ", resta)
print("")
#realizamos la división del resultado de la resta entre el resultado de la suma.
print("DIVISIÓN DE RESULTADOS")
print("""El reultado de la resta será dividido entre resultado el de la suma:
      suma= 195
      resta= 239""")
División= resta / suma
print("El reultado de la división de estos es de: ", División)
print("")
#En este apartado definiremos las 4 variables complejas distintas.
print ("VARIABLES COMPLEJAS (COMPLEX)")
Com1= 2 + 5j
Com2= 8 - 3j
Com3= 5 + 1j
Com4= 6 - 1j

comp= (Com1, Com2, Com3, Com4)
print("Los valores para las varibles complex son:", comp)
print ("")
#En esta parte vamos a definir una variable para cada integrante del grupo y en esta almacenaremos el nombre de una fruta.
print("CARACTER (STRING)")
#Aqui enumeraremos los nombres de los integrantes del equipo
string1= "Mi nombre es Mauricio, "
string2= "Mi nombre es Jonathan, "
string3= "Mi nombre es Ana, "
string4= "Mi nombre es Alicia, "
string5= "Mi nombre es Nestor, "
string6= "Mi nombre es Juan, "
#Aqui asignaremos las frutas
fruta1= "Melocotón"
fruta2= "Uva"
fruta3= "Mango"
fruta4= "Piña"
fruta5= "Papaya"
fruta6= "Jocote"
#Llamaremos los nombres junto con las frutas
print(string1, "mi fruta favorita es", fruta1)
print(string2, "mi fruta favorita es", fruta2)
print(string3, "mi fruta favorita es", fruta3)
print(string4, "mi fruta favorita es", fruta4)
print(string5, "mi fruta favorita es", fruta5)
print(string6, "mi fruta favorita es", fruta6)
print("")
print("BOOLEANO (BOOL)")
# Capturar el nombre de una fruta desde el teclado
fruta = input("Ingresa el nombre de una fruta: ")

# Utilizar una estructura de control "if" para mostrar un mensaje dependiendo de la fruta ingresada
if fruta == "Melocotón":
    print(True, type (True))
    print("La fruta ingresada es manzana. Fruta elegida por mi compañero Mauricio.")
if fruta == "Uva":
    print(True, type(True))
    print("La fruta ingresada es uva. Fruta elegida por mi compañero Jonathan.")
if fruta == "Mango":
    print (True, type(True))
    print("La fruta ingresada es mango. Fruta elegida por mi compañera Ana.")
if fruta == "Piña":
    print(True, type(True))
    print("La fruta ingresada es piña. Fruta elegida por mi compañera Alicia")
if fruta== "Papaya":
    print(True,type(True))
    print("La fruta ingresada es papaya. Fruta elegida por mi compaeñero Nestor")
if fruta== "Jocote":
    print(True, type(True))
    print("La fruta ingresada es jocote. Fruta elegida por mi compañero Juan")
print("")
print("Fin.")
print("")
