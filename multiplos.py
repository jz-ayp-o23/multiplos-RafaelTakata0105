""""
Tarea: Multiplos
Author: Rafael Takata García
Fecha de entrega: 07/10/2023
Grupo: ESI-232B-5
Profesor: Jorge Adalberto Saldivar

Descripción:
Dados número, determinar si uno es multiplo del otro.
"""

# Declaraciones
# Entradas
numero_1 = int(input("Introduzca un número: "))
numero_2 = int(input("Introduzca otro número: "))
# Proceso
if numero_1 == 0 or numero_2 == 0:
    print("Ninguno de los números es múltiplo del otro")
elif numero_1 % numero_2 == 0 or numero_2 % numero_1 == 0:
    if numero_1 < numero_2:
        print(f"El número {numero_2} es múltiplo del {numero_1}")
    else:
        print(f"El número {numero_1} es múltiplo del {numero_2}")
else: 
    print("Ninguno de los números es múltiplo del otro")
# Salidas
