# Actividad 1: describe su edad, nombre y comida favorita

text1 = "Hola, mi nombre es "
nombre = " Andres "
edad = " 20 años "
text3 = ' y tengo '
comida_fav = ' salchipapa '
text2 = " mi comida favorita es la "

result1 = text1 + nombre + text3 + edad + text2 + comida_fav

print(result1)

#Actividad 2
text4 = 'hola '
text5 = ' tu nombre tiene '
text6 = ' letras '
text7 = ' excluyendo los espacios'
nombrecompleto = input("Escriba su nombre completo: ")
numero_letras = len(nombrecompleto.replace(" "," "))

result2 = text4 + nombrecompleto + text5 + str (numero_letras) + text6 + text7
print(result2)

#Actividad 3

porcentaje1 = float(input("increaseSalesPercent = "))
porcentaje2 = float(input("revenueGrowthPercent = "))

result3 = f"Las ventas de la empresa láctea aumentaron un {porcentaje1:.2f}% y el crecimiento de ingresos es {porcentaje2:.2f}%."

print(result3)

#4

mensajeOculto=  "aS!Ir waQm  VL!eDafrcnXi n=gS .P,yytahgoln.!"
mensjeDecodificado = mensajeOculto [3::2]
print(mensjeDecodificado)

#5

def con_palabras(text):
    palabras = text.split()
    return len(palabras)

text = "La programacion en python es agradable a la vista"
num_palbras = con_palabras(text)
print(f" El numero de palabras en la frase es: {num_palbras}")

#6

def rem_letra(cadena, letraOriginal, letra_New):
    return cadena.replace(letraOriginal, letra_New)

#Palabra Original
working = "Elefante"

#Remplaza 'e' por 'i'

newWorking = rem_letra(working, 'e', 'i')
print(newWorking)




