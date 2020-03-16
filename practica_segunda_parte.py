# -*- coding: utf-8 -*-
"""
Created on Sun Mar  8 17:49:48 2020

@author: Franco
"""


#Ejercicio 1
#Escribir una función max_in_list() que tome una lista de números y devuelva el mas grande.

def max_in_list(lista):
    return max(lista)

        
             
            

lista = [1,2,3,4,5,7,49,55,2,1000]
max_in_list(lista)


def max_in_lista(lista):
    inicio = 0
    for i in lista:
        if i > inicio:
            inicio = i
    return inicio


 

lista = [1,2,3,4,5,7,49,55,2,1000]
max_in_lista(lista)


#Ejercicio 2
#Escribir una función mas_larga() que tome una lista de palabras y devuelva la mas larga. 
def mas_larga(lista):
    inicio = ""
    for elemento in lista:
        if len(elemento) > len(inicio):
            inicio = elemento
    return (inicio)
        

lista = ["Hola", "Pelotudo", "Hijodemilputa", "fffffffffffffffffffffff"]

mas_larga(lista)



#Ejercicio 3
#Escribir una función filtrar_palabras() que tome una lista de palabras y un entero n, y devuelva las palabras que tengan mas de n caracteres. 

def filtrar_palabras (lista, n):
    for elemento in lista:
        if len(elemento) > n:
            print (elemento)
 
lista = ["Hola", "Pelotudo", "Hijodemilputa", "fffffffffffffffffffffff"]
filtrar_palabras(lista,3)

           
#Ejercicio 4
#Escribir un programa que le diga al usuario que ingrese una cadena. El programa tiene que evaluar la cadena y decir cuantas letras mayúsculas tiene. 

def contar_mayusculas(): 
    cadena = str(input("Ingrese una cadena: "))
    i = 0
    q_mayuscula = 0
    for i in range (len(cadena)):
        if(( cadena[i] == "A") or (cadena[i] == "B") or (cadena[i] == "C") or (cadena[i] == "D") or (cadena[i] == "E") or (cadena[i] == "F") or (cadena[i] == "G") or (cadena[i] == "H") or (cadena[i] == "I") or (cadena[i] == "J") or (cadena[i] == "K") or (cadena[i] == "L") or (cadena[i] == "M")or (cadena[i] == "N") or (cadena[i] == "O") or (cadena[i] == "P") or (cadena[i] == "Q") or (cadena[i] == "R") or (cadena[i] == "S") or (cadena[i] == "T") or (cadena[i] == "U") or (cadena[i] == "V") or (cadena[i] == "W") or (cadena[i] == "X") or (cadena[i] == "Y") or (cadena[i] == "Z")):
              q_mayuscula +=1
              i +=1        
    return q_mayuscula
    
contar_mayusculas()






#Ejercicio 5
#Construir un pequeño programa que convierta números flotantes en enteros. 
def enteros(x):
    return '{:.{prec}f}'.format(x, prec=0)

enteros(2.49)


#Ejercicio 6
#Escribir un pequeño programa donde:
#- Se ingresa el año en curso.
#- Se ingresa el nombre y el año de nacimiento de tres personas.
#- Se calcula cuántos años cumplirán durante el año en curso.
#- Se imprime en pantalla.

año_en_curso = int(input("Ingrese el año en curso: "))
i = 0
while 3 > i:
    nombre = input("Ingrese su nombre : ")
    fecha_de_nacimiento = int(input("Ingrese el año en el cual nació: "))
    edad = año_en_curso - fecha_de_nacimiento
    print("")
    print(nombre + " tiene (o va a cumplir) " + str(edad) + " años")
    i +=1
print("Gracias por utilizar el programa")
    
    

#Ejercicio 7
#Definir una tupla con 10 edades de personas. Imprimir la cantidad de personas con edades superiores a 20.
#Puedes variar el ejercicio para que sea el usuario quien ingrese las edades.

def mayores_20(tupla):
    i = 0
    for elemento in tupla:
        if elemento > 20:
            i += 1
    return i        

tupla = (15,16,17,18,19,20,21,22,23,24)
mayores_20(tupla)


#Ejercicio 8
#Definir una lista con un conjunto de nombres, imprimir la cantidad de comienzan con la letra a.
#También se puede hacer elegir al usuario la letra a buscar.  (Un poco mas emocionante)

def nombre_con_letra (lista, x):
    i = 0
    for elemento in lista:
        if elemento[0] == x:
            print(elemento)
            i +=1
    print("La cantidad de nombres que comienzan con la letra: " + x + " es igual a " + str(i), end = " ")
    
    

lista = ["Franco", "Sol", "Agustina", "Paulo", "Pablo", "Tamara"] 
nombre_con_letra(lista, "P")       
            
    

#Ejercicio 9
#Crear una función contar_vocales(), que reciba una palabra y cuente cuantas letras "a" tiene, cuantas letras "e" tiene y así hasta completar todas las vocales.
#Se puede hacer que el usuario sea quien elija la palabra.

def contar_vocales(palabra):
    q_vocales = 0
    for letra in palabra:
        if ((letra == "a") or (letra == "e") or (letra == "i") or (letra == "o") or (letra == "u")):
            q_vocales += 1
    return q_vocales

contar_vocales("agustina")
        


#Ejercicio 10
#Escriba una función es_bisiesto() que determine si un año determinado es un año bisiesto.Un año bisiesto es divisible por 4, pero no por 100. También es divisible por 400

def es_bisiesto(x):
    resta = abs(2020-x)
    if (resta % 4) == 0 :
        print("El año " + str(x) + " es bisiesto")
    else:
        print("El año " + str(x) + " no es bisiesto")


es_bisiesto(2028)





