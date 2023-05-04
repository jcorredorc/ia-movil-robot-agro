# -*- coding: utf-8 -*-
"""
Created on Fri Feb 24 00:37:08 2023

@author: Julian Rene Chaux
"""

#Las variables se definen de forma dinámica. El signo igual (=) se usa para asignar valores a las variables


"""Esto es un comentario de
    varias lineas como 
    ejemplo en el curso"""

'''Este es otro comentario
    de varias lineas'''

x = 1
print(type(x))
x = 'texto'  #Esto es posible por el tipado dinámico
print(type(x))
x = 1.0
print(type(x))


"""****************************************************************************

Variables

****************************************************************************"""
x = str(3)
print(x)
print(type(x))

x = int(3)
print(x)
print(type(x))

x = float(3)
print(x)
print(type(x))
x = 3
print(type(x))

complejo = 3+5j
print(complejo)
print(type(complejo))

c = "Julian"
d = 'Julian'
c == d

a = 4
A = "Sally"

"""****************************************************************************

Casting: Hacer cast o casting significa convertir un tipo de dato a otro. 

****************************************************************************"""
#Conversión Implícita

a = 1
print(type(a))
b = 2.3
print(type(b))
c = a + b
print(c)
print(type(c))

#Conversión Explícita

a = "35.5"
b = float(a)
print(type(a))
print(a)
print(type(b))
print(b)

a = '3'
print(type(a))
b = int(a)
print(b)
print(type(b))

a = 10
print(type(a))
b = str(a)
print(b)
print(type(b))

a = 52.63
print(type(a))
b = int(a)
print(b)
print(type(b))

a = 5
b = "10"
c = a + b
c = a + int(b)
print(c)


"""****************************************************************************

Prueba operador de membresía

****************************************************************************"""
texto = "Sena"
print('N' not in texto)
print('N' in texto)
print('S' in texto)

res = 'N' in texto
print(type(res))


"""****************************************************************************

Variables Numéricas: NUMBER

****************************************************************************"""
x = 1
y = 2.8
z = 1j
print(type(x))
print(type(y))
print(type(z))

#Potencia
2**3

pow(2,3)

#Módulo
a = 8%4
print(a)

#Cociente Entero
b = 16//4
print(b)

#Números Aleatorios: Librería random
import random

a = random.random() #Números aleatorios entre 0 y 1
print(a)

print(random.randint(0,20))  #Números enteros aleatorios entre 5 y 20

#Librería Matemática: math
import math
math.ceil(3.5698) #Aproxima por encima

math.floor(3.5698) #Aproxima por debajo

math.sqrt(4) #raiz cuadrada

math.pow(3,3) #Potencia

#Constantes
math.e
math.pi

a = math.inf
print(a)
type(a)

a = math.nan
print(a)
type(a)

math.pow(math.inf, 0)

math.sin(math.pi) #Seno

math.cos(math.pi/2) #Coseno

math.factorial(3) #Factorial

"""****************************************************************************

Variables de texto: STRING

****************************************************************************"""
a = "Hello"
b = 'Hello'
print(a)
print(b)
a == b

texto = """Lorem Ipsum is simply dummy text of the printing 
and typesetting industry. Lorem Ipsum has been the industry's 
standard dummy text ever since the 1500s, when an unknown printer 
took a galley of type and scrambled it to make a type specimen book"""
print(texto)

#Los STRING son Arrays
#Slicing

texto = "Hello, World!"
print(texto[5])

print(texto[0:12])

print(texto[-1])

print(texto[-3:-1])

print(texto[2:])

print(texto[:5])

print(len(texto))

print(texto[1:len(texto)])

txt = "The best things in life are free!"
print("free" in txt)
print("expensive" not in txt)

#Modificar STRING
texto = "Hello, World, I'm very happy with us"
print(texto.upper())

print(texto.lower())

texto = "    Hello, World!  "
print(texto.rstrip())

print(texto.lstrip())

print(texto.strip())

texto = "Hello, World!"
print(texto.replace("l", "*"))

print(texto.split(" "))

texto1 = texto.split(" ")
print(texto1)
print(len(texto1))

print(texto.split(" ")[0])
print(texto.split(" ")[1])


#Concatenar
a = "Hola"
b = "Equipo"
c = a + " " + b
print(c)

nombre = "Julián"
apellido = "Cháux"
edad = 39

txt = "Mi nombre es " + nombre + " y tengo " + str(edad) + " años"
print(txt)

print("Mi nombre es ", nombre, " y tengo ", str(edad), " años")

print("Mi nombre es %s, mi apellido es %s y tengo %d años"%(nombre, apellido, edad))

txt = "Mi nombre es {}, mi apellido es {} y tengo {} años".format(nombre, apellido, edad)
print(txt)

txt = "Mi nombre es {2}, mi apellido es {1} y tengo {0} años".format(edad, apellido, nombre)
print(txt)

txt = f"Mi nombre es {nombre}, mi apellido es {apellido} y tengo {edad} años"
print(txt)

diez_espacios = "*"*10
print(diez_espacios + "un texto de diez asteriscos al iniciar")

texto = "Hola \n Mundo"
print(texto)

texto = "Hola \t Mundo \t \t hoy es martes"
print(texto)

nombre = "Julián"
apellido = "Cháux"
edad = 39.2

salida = "Mi nombre es %s, mi apellido es %s y tengo %f años"%(nombre, apellido, edad)


"""****************************************************************************

SONDEO 1

****************************************************************************"""
# Alternativa 1

texto = "Mi%nombre%es;Julian;Mi%apellido%es;Chaux;" 
#Opcion 1
print("El nombre y el apellido oculto del texto es "+texto[13:19]+" "+texto[-6:-1])

#Opcion 2
print(texto.split(";"))
print("El nombre y el apellido oculto del texto es "+texto.split(";")[1]+" "+texto.split(";")[3])