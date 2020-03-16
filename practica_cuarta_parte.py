# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 19:11:35 2020

@author: Franco
"""

#1) Este programa pide primeramente la cantidad total de compras de una persona. Si la cantidad es inferior a $100.00, el programa dirá que el cliente no aplica a la promoción. Pero si la persona ingresa una cantidad en compras igual o superior a $100.00, el programa genera de forma aleatoria un número entero del cero al cinco. Cada número corresponderá a un color diferente de cinco colores de bolas que hay para determinar el descuento que el cliente recibirá como premio. Si la bola aleatoria es color blanco, no hay descuento, pero si es uno de los otros cuatro colores, sí se aplicará un descuento determinado según la tabla que  aparecerá, y ese descuento se aplicará sobre el total de compra que introdujo inicialmente el usuario, de manera que el programa mostrará un nuevo valor a pagar luego de haber aplicado el descuento.

def programa_de_descuentos():

    print("-----------------------------------------------------------------------------")
    print("Este es un programa para calcular los descuentos a aplicar a los consumidores")
    print("-----------------------------------------------------------------------------")
    
    valor_compra = float(input("Ingrese el monto total de su compra: "))
    descuento = [0, 0.1, 0.2, 0.25, 0.5]
    lista_colores = ["Blanco", "Rojo", "Azul", "Verde", "Amarillo"]
    
    if 100 > valor_compra:
        print("Usted no tiene descuento")
    else:
        print("Felicidades, usted participa de la siguiente promoción:")
        print("Color" + "     " + "Descuento")
        diccio_colores = {"Bola Blanca":"0 %", "Bola Roja":"10 %", "Bola Azul":"20 %", "Bola Verde":"25 %", "Bola Amarilla":"50 %"}
        for elemento in diccio_colores:
            print(elemento, ":", diccio_colores[elemento])
        num_aleatorio = (rand(0,5))
        def aviso(color):
            print("Usted obtuvo aleatoriamente una bola de color", color)
            
        for i in range (0,5):
            if num_aleatorio == i:    
                aviso(lista_colores[i])
                print("Su descuento es del ", str(descuento[i] * 100), "%")
                print("")
                print("Su nuevo total a pagar es: $", str(valor_compra*(1-descuento[i])))
        
   
programa_de_descuentos()
