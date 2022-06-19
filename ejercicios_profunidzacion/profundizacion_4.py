# Condicionales [Python]
# Ejercicios de profundización

# Autor: Inove Coding School
# Version: 2.0

# NOTA: 
# Estos ejercicios son de mayor dificultad que los de clase y práctica.
# Están pensados para aquellos con conocimientos previo o que dispongan
# de mucho más tiempo para abordar estos temas por su cuenta.
# Requiere mayor tiempo de dedicación e investigación autodidacta.

# IMPORTANTE: NO borrar los comentarios en VERDE o NARANJA

# Ejercicios de práctica con texto
'''
Enunciado:
Realice un programa que solicite por consola 3 palabras cualesquiera
Luego el programa debe consultar al usuario como quiere ordenar las palabras
1 - Ordenar por orden alfabético (usando el operador ">")
2 - Ordenar por cantidad de letras (longitud de la palabra (len) y operador ">")

Si se ingresa "1" por consola se deben ordenar las 3 palabras por orden alfabético
e imprimir en pantalla de la mayor a la menor

Si se ingresa "2" por consola se deben ordenar las 3 palabras por cantidad de letras
e imprimir en pantalla de la mayor a la menor

IMPORTANTE: Para ordenar las palabras deben realizar condicionales compuestos o anidados,
no se busca utilizar bucles o algoritmos de ordenamiento ya que aún no hemos llegado a ese
contenido.
'''

from operator import truediv


print('Ejercicios de práctica con cadenas')
# Empezar aquí la resolución del ejercicio
palabra_1 = input("Ingrese la 1° Palabra:")
palabra_2 = input("Ingrese la 2° Palabra:")
palabra_3 = input("Ingrese la 3° Palabra:")

opcion = input("Que desea hacer? 1- Ordenar por orden alfabético o 2- Ordenar por cantidad de letras:")

if opcion=='1':
    if palabra_1>palabra_2 and palabra_1>palabra_3:
        if palabra_2>palabra_3:
            print("Orden: ",palabra_1,palabra_2,palabra_3)
        else:
            print("Orden: ",palabra_1,palabra_3,palabra_2)
    elif palabra_2>palabra_1 and palabra_2>palabra_3:   
        if palabra_1>palabra_3:
            print("Orden: ",palabra_2,palabra_1,palabra_3)
        else:
            print("Orden: ",palabra_2,palabra_3,palabra_1)
    elif palabra_3>palabra_1 and palabra_3>palabra_2:   
        if palabra_1>palabra_2:
            print("Orden: ",palabra_3,palabra_1,palabra_2)
        else:
            print("Orden: ",palabra_3,palabra_2,palabra_1)

if opcion=='2':
    if len(palabra_1)>len(palabra_2) and len(palabra_1)>len(palabra_3):
        if len(palabra_2)>len(palabra_3):
            print("Orden: ",palabra_1,palabra_2,palabra_3)
        else:
            print("Orden: ",palabra_1,palabra_3,palabra_2)
    elif len(palabra_2)>len(palabra_1) and len(palabra_2)>len(palabra_3):   
        if len(palabra_1)>len(palabra_3):
            print("Orden: ",palabra_2,palabra_1,palabra_3)
        else:
            print("Orden: ",palabra_2,palabra_3,palabra_1)
    elif len(palabra_3)>len(palabra_1) and len(palabra_3)>len(palabra_2):   
        if len(palabra_1)>len(palabra_2):
            print("Orden: ",palabra_3,palabra_1,palabra_2)
        else:
            print("Orden: ",palabra_3,palabra_2,palabra_1)


print ("Con Listas y bucles!!")
print ("=====================")
palabras = []
palabras.append(palabra_1)
palabras.append(palabra_2)
palabras.append(palabra_3)

opcion = input("Que desea hacer? 1- Ordenar por orden alfabético o 2- Ordenar por cantidad de letras:")
lista_ordenada = []

if opcion=='1':
    lista_ordenada = sorted(palabras)
    # Ordena inverso: lista_ordenada = sorted(palabras,reverse = True)
    print(lista_ordenada)
elif opcion=='2':
    lista_ordenada = sorted(palabras, key = len)
    print(lista_ordenada)



