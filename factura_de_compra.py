# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 22:03:11 2020

@author: Franco
"""

#2) De la galería de productos, el usuario introducirá el código y el número de unidades del producto que desea comprar. El programa determinará el total a pagar, como una factura.
#Una variante a este ejercicio que lo haría un poco más complejo sería dar la posibilidad de seguir ingresando diferentes códigos de productos con sus respectivas cantidades, y cuando el usuario desee terminar el cálculo de la factura completa con todas sus compras.

producto = ["Camisa", "Cinturon", "Zapatos", "Pantalon", "Calcetines", "Faldas", "Gorras", "Sueter", "Corbata", "Chaqueta"]
codigo = [1,2,3,4,5,6,7,8,9,10]
precios = [100, 50, 200, 150, 20, 100, 15, 150, 40, 300]
diccio_productos = dict(zip(producto, codigo))
diccio_precios = dict(zip(producto, precios))



def factura():
    print("Elija el producto deseado: ")
    print("")
    print("Elemento : Código")
    print("")
    for clave in diccio_productos:
        print(clave, ":",diccio_productos [clave] )
        
    opcion = 0
    monto = 0
    monto_total = 0
    
    while opcion == 0:
        codigo_seleccionado = int(input("Ingrese el código seleccionado: "))
        print("El precio es: $", precios[codigo_seleccionado - 1])
        cantidad = int(input("Ingrese la cantidad que desea comprar: "))
        monto = cantidad * precios[codigo_seleccionado - 1]
        monto_total += monto
        print("-------------------------------------------------------------------------------------------------------------------------")
        opcion = int(input("Si desea comprar otra cosa, apriete el cero . Si desea finalizar su compra, apriete cualquier otro número: "))
    
    print("")
    print("------------------------------------")
    print("Usted debe abonar un total de $", monto_total)
    print("------------------------------------")
  
    
factura()
   
        
    
    

































