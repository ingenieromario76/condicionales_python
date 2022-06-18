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

# Ejercicios de práctica con números
'''
Enunciado:
Realice un programa que solicite ingresar tres valores de temperatura
De las temperaturas ingresadas por consola determinar:
1 - ¿Cuáles de ellas es la máxima temperatura ingresada?
2 - ¿Cuáles de ellas es la mínima temperatura ingresada?
3 - ¿Cuál es el promedio de las temperaturas ingresadas?

En cada caso imprimir en pantalla el resultado

IMPORTANTE: Para ordenar las temperatuas debe utilizar condicionales compuestos o anidados,
no se busca utilizar bucles o algoritmos de ordenamiento ya que aún no hemos llegado a ese
contenido. Recomendamos pensar bien este problema de lógica con un lápiz y papel.
'''

from tokenize import Double


print('Ejercicios de práctica con números')
# Empezar aquí la resolución del ejercicio

temp_1 = int(input("Ingrese 1er Temperatura:"))
temp_2 = int(input("Ingrese 2da Temperatura:"))
temp_3 = int(input("Ingrese 3er Temperatura:"))

# CALCULO MAXIMA
if temp_1>temp_2:
    if temp_1>temp_3:
        print("La máxima temperatura es la 1°:",temp_1)
    elif temp_1==temp_3:
        print("Las máximas temperaturas son la 1° y 3° {}!".format(temp_1,temp_3))
    else: 
        print("La máxima temperatura es la 3°:",temp_3)
elif temp_1==temp_2:
    if temp_1>temp_3:
        print("Las máximas temperaturas son las 1° ",temp_1,"y la 2°",temp_2)
    elif temp_1==temp_3:
        print("Las máximas temperaturas son las 3")
    else: 
        print("La máxima temperatura es la 3°:",temp_3)
elif temp_2>temp_3:
    print("La máxima temperatura es la 2°:",temp_2)
elif temp_2==temp_3:
    print("Las máximas temperaturas son la 2° y 3° {}!".format(temp_2,temp_3))
else: 
    print("La máxima temperatura es la 3°:",temp_3)


# CALCULO MINIMA
if temp_1<temp_2:
    if temp_1<temp_3:
        print("La Mínima temperatura es la 1°:",temp_1)
    elif temp_1==temp_3:
        print("Las mínimas temperaturas son la 1° y 3° {}!".format(temp_1,temp_3))
    else: 
        print("La mínima temperatura es la 3°:",temp_3)
elif temp_1==temp_2:
    if temp_1<temp_3:
        print("Las máximas temperaturas son las 1° ",temp_1,"y la 2°",temp_2)
    elif temp_1==temp_3:
        print("Las mínimas temperaturas son las 3")
    else: 
        print("La mínima temperatura es la 3°:",temp_3)
elif temp_2<temp_3:
    print("La mínima temperatura es la 2°:",temp_2)
elif temp_2==temp_3:
    print("Las mínimas temperaturas son la 2° y 3° {}!".format(temp_2,temp_3))
else: 
    print("La mínima temperatura es la 3°:",temp_3)

# Promedio
promedio = (temp_1+temp_2+temp_3)/3
print ("El promedio de las temperaturas es:",promedio)
        
