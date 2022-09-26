"""bandera = True
numero=str(abs(int(input("numero: "))))
while bandera==True:
  if len(numero) ==1:
    print("unidad")
    break
  elif len(numero)==2:
    print("decena")
    break
  elif len(numero)==3:
    print("centena")
    break
  elif len(numero)==4:
    print("milesima")
    break
  elif len(numero)==5:
    print("decena de mil")
    break
  elif len(numero)==6:
    print("centena de mil")
    break
  else:
    bandera=False
    """

"""a= input("ingrese un numero: ")
b= input("ingrese un numero: ")
c= input("ingrese un numero: ")"""

"""ciudades = {
"Cartagena": ['M', 'S', 'L', 'L', 'L', 'L', 'L', 'XL', 'XXL', 'S', 'S', 'L', 'M', 'M', 'M', 'S', 'S', 'M', 'M'],
    
"Barranquilla": ['S', 'S', 'L', 'M', 'XL', 'S', 'L', 'M', 'M', 'M', 'S', 'S', 'M', 'M', 'XL', 'S', 'M', 'S', 'XXL', 'XL', 'L'],
    
"Medellin": ['L', 'L', 'XL', 'XXL', 'S', 'S', 'S', 'S', 'L', 'L', 'L', 'XL', 'XL', 'XL', 'XL', 'XL', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'M', 'M', 'S', 'S', 'S', 'S', 'XL', 'L'],
    
"Bogota": ['M', 'S', 'S', 'M', 'M', 'XL', 'S', 'M', 'S', 'S', 'S', 'L', 'S', 'S', 'S', 'M', 'M','M', 'M', 'M', 'M', 'M', 'M', 'L', 'L', 'XL', 'XL', 'XL', 'XL', 'XL', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'L', 'L', 'XL', 'XL', 'XL', 'XL', 'XL' ]
}
precios = {
'S':        2500,
'M':        3400,
'L':        5200,
'XL':       6000,
'XXL':      9000,
}

def totalDeVentas( lisTallas, dicPrecios):
    valorTotal = 0
    for talla in lisTallas:
        valorTotal += dicPrecios[talla]
    return valorTotal

#total de ventas, 
#las tallas más vendidas y 
#el total de tallas 
#por ciudad.


def tallaMasVendidaPorCiudad( lisTallas ):
    contadores = {
'S':        0, 
'M':        0,
'L':        0,
'XL':       0,
'XXL':      0,       
    }
    
    for talla in lisTallas:
        if talla == 'S':
            contadores["S"] += 1
        elif talla == "M":
            contadores["M"] += 1
        elif talla == "L":
            contadores["L"] += 1
        elif talla == "XL":
            contadores["XL"] += 1
        elif talla == "XXL":
            contadores["XXL"] += 1
    
    for key in contadores:
        contadores[key] = lisTallas.count(key)
            
    valorMasVendido = 0
    
    for key in contadores:
        print( key, contadores[key])
        if valorMasVendido < contadores[key]:
            valorMasVendido = contadores[key]
            masVendido = key   
            
    return (masVendido, valorMasVendido) 

if __name__ == "__main__":
    print("Total de ventas por ciudad")
    for ciudad in ciudades:
        print(ciudad, totalDeVentas( ciudades[ciudad], precios ) )
    
    print("Tallas mas vendidas por ciudad")

    for ciudad in ciudades:
        
        print(ciudad, tallaMasVendidaPorCiudad( ciudades[ciudad])"""
import math
from re import X

def funcionCuadratica():

  a = float(input("ingrese un numero: a =  "))
  b = float(input("ingrese un numero: b = "))
  c = float(input("ingrese un numero: c = "))

  
  resultado0 = 4*a*c
  resultado1 = b**2
  


  if resultado0 == resultado1:
    X1 = -b / (2*a)
    x2 = -b / (2*a) 
    print(X1)
    
  elif resultado1 > resultado0:
    resultado2= math.sqrt(resultado1-resultado0)
    x1= (-b + resultado2)/(2*a)
    x2= (-b - resultado2)/(2*a)
    print(x1,x2)
    
  elif resultado0 > resultado1 :
    print ("La ecuacion no tiene soluciones reales")
    print ("La ecuacion no tiene soluciones reales")


funcionCuadratica()