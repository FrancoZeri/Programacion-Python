# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 18:43:48 2020

@author: Franco
"""

#1- Definir una función max() que tome como argumento dos números y devuelva el mayor de ellos. (Es cierto que python tiene una función max() incorporada, pero hacerla nosotros mismos es un muy buen ejercicio.

def max_funcion(n1,n2):
    return max(n1,n2)
max_funcion(2,3)


#otra forma de hacerlo

def max_funcion2 (n1,n2):
    if n1 > n2:
        print(str(n1))
    elif n2 > n1:
        print(str(n2))
    else:
        print(str(n1))
        
max_funcion2(1000,1000)




#2- Definir una función max_de_tres(), que tome tres números como argumentos y devuelva el mayor de ellos. 


def max_de_tres(n1,n2,n3):
    def max_de_dos(n1,n2):
        return max(n1,n2)
    return max(max_de_dos(n1,n2), n3)

max_de_tres(854,2,1000000)

# Otra forma

def max_de_tres2(n1,n2,n3):
    if n1 > n2 and n1 > n3:
        print(str(n1))
    elif n1 > n2 and n3 > n1:
        print(str(n3))
    elif n2 > n1 and n2 > n3:
        print(str(n2))
    elif n2 > n1 and n3 > n2:
        print(str(n3))
        
max_de_tres2(45,88,66)



#3- Definir una función que calcule la longitud de una lista o una cadena dada. (Es cierto que python tiene la función len() incorporada, pero escribirla por nosotros mismos resulta un muy buen ejercicio.

def otra_funcion(x):
    if type(x) == list:
        for elemento in x:
            print (elemento)
    elif type(x) == str:
        for caracter in x:
            print(caracter)
    else:
        print("Error. Usted no está trabajando con listas o cadenas.")


def longitud(x):
    if type(x) == list:
        print(len(x))
    elif type(x) == str:
        print(len(x))
    else:
        print("Error. Usted no está trabajando con listas o cadenas.")
            
y = "Hola"
z = [1,2,3,4]

longitud(y)
longitud(z)
        
               


#4- Escribir una función que tome un carácter y devuelva True si es una vocal, de lo contrario devuelve False.

def vocal(x):
    if type(x) == str:
        for caracter in x: 
            if ((caracter == "a") or (caracter == "e") or (caracter == "i") or (caracter == "o") or (caracter == "u")):
                print("True")
            else:
                print("False")
    else:
        print("Esta función sirve para Strings únicamente")

x = "Hola"

vocal(x)



#5- Escribir una funcion sum() y una función multip() que sumen y multipliquen respectivamente todos los números de una lista. Por ejemplo: sum([1,2,3,4]) debería devolver 10 y multip([1,2,3,4]) debería devolver 24.

def sum_y_mult(x):
    if type(x) == list:
        suma=0
        multiplicacion=1
        for elemento in x:
            suma += elemento
        print("La suma de los elementos de la lista es igual a: " + str(suma))
        for elemento in x:
            multiplicacion = multiplicacion * elemento
        print("La multiplicación de los elementos de la lista es igual a: " + str(multiplicacion))   
    else:
        print("La función sirve unicamente para listas") 
        
y = [45,2,33]

sum_y_mult(y) 
       
            
              

#6- Definir una función inversa() que calcule la inversión de una cadena. Por ejemplo la cadena "estoy probando" debería devolver la cadena "odnaborp yotse"


def inversa(cadena):
    cadena_invertida = ""
    longitud = len(cadena)
    indice = -1
    while longitud >= 1:
        cadena_invertida += cadena[indice]
        indice = indice + (-1)
        longitud -= 1
    return cadena_invertida    




#7 - Definir una función es_palindromo() que reconoce palíndromos (es decir, palabras que tienen el mismo aspecto escritas invertidas), ejemplo: es_palindromo ("radar") tendría que devolver True.

def es_palindromo(x):
    if type(x) == str:
        cadena_invertida = ""
        longitud = len(x)
        indice = -1
        while longitud >= 1:
            cadena_invertida += x[indice]
            indice -= 1
            longitud -= 1
        if cadena_invertida == x:
            print("la palabra " + x + " es palíndromo")
        else:
            print("la palabra " + x + " no es palíndromo")
    elif type(x) == int:
        numero_invertido = int(str(x)[::-1])
        if numero_invertido == x:
            print("El número " + str(x) + " es capicúa")
        else: 
            print("El número " + str(x) + " no es capicúa")
    elif type (x) == float: 
        numero_invertido = float(str(x)[::-1])
        if numero_invertido == x:
            print("El número " + str(x) + " es capicúa")
        else: 
            print("El número " + str(x) + " no es capicúa")
    else: 
        print("Error en el tipo de dato")
        
x = "Neuquen"
es_palindromo(x)
       
        

#8- Definir una función superposicion() que tome dos listas y devuelva True si tienen al menos 1 miembro en común o devuelva False de lo contrario. Escribir la función usando el bucle for anidado. 

def superposicion(x,y):
    for elemento_x in x:
        i = 0
        while (len(y)-1) >= i :
            if elemento_x == y[i]:
                print("True")
            i += 1  
           

x = [1,2,3]
y = [0,4,3,6,7]

superposicion(x,y)




#9- Definir una función generar_n_caracteres() que tome un entero n y devuelva el caracter multiplicado por n. Por ejemplo: generar_n_caracteres(5, "x") debería devolver "xxxxx".

def generar_n_caracteres(q, cadena):
    return q * cadena

generar_n_caracteres(5,"p")


#10- Definir un histograma procedimiento() que tome una lista de números enteros e imprima un histograma en la pantalla. Ejemplo: procedimiento([4, 9, 7]) debería imprimir lo siguiente:


  



