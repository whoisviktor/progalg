#FUNCION RANGE()
""" x = range(0,101,2)
for n in x:
    print(n) """
    
#RECORRIENDO CADENAS
""" 
frase = "hola mundo987"
for char in frase:
    print(char)
#CHAR: IMPRIME CUALQUIER DATO INGRESADO EN LA STRING
 """

""" frase = "Hola Mundo"
for caracter in frase:
    print(caracter)
 """
 

#Ingresar por teclado 5 números enteros
#       num = int(input("Ingrese un numero:\n"))
#       x = range(num)
#       for n in x:
#           print(n)

#luego debe indicar: Cuántos números son mayores a cero
igual_cero = 0
mayor_cero = 0
menor_cero = 0

for n in range(5):
    num = int(input("Ingrese un numero:\n"))
    if num == 0:
        print("el numero es igual a 0")
        igual_cero = igual_cero + 1
        
    elif num < 0:
        print("el numero es menor a 0")
        menor_cero = menor_cero + 1
      
    else:
        print("el numero es mayor a 0")
        mayor_cero = mayor_cero + 1
    print(f"los numeros mayores a cero son: {mayor_cero}")
    print(f"los numeros iguales a cero son: {igual_cero}")
    print(f"los numeros menores a cero son: {menor_cero}")