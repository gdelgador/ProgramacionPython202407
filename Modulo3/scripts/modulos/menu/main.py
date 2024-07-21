"""
Generaremos un programa menu que realice las siguiente tareas.

1. Saludar
2. Calcular el factorial de un numero
3. Calcular el area de un circulo
4. Suma de divisores de un numero
5. Generar un triangulo rectangulo
6. Salir
"""

# 1. Importamos Librerias


# 2. Definir las constantes

# 3. Definimos Funciones y/o clases


# 4. Definimos la función principal
def main():
    ### Código de la función principal
    pass

# 5. Punto de entrada a la aplicación
if __name__ == '__main__':
    main()



print("Bienvenido al menú interactivo")
while True:
    print("""¿Qué quieres hacer? Escribe una opción
    1) Saludar
    2) Sumar dos números
    3) Salir""")
    
    opcion = input() # me devuelve un string ''
    if opcion == '1':
        print("Hola, espero que te lo estés pasando bien")
    elif opcion == '2':
        n1 = float(input("Introduce el primer número: "))
        n2 = float(input("Introduce el segundo número: "))
        print(f"El resultado de la suma es: {n1+n2}")
    elif opcion =='3':
        print("¡Hasta luego! Ha sido un placer ayudarte")
        break
    else:
        print("Comando desconocido, vuelve a intentarlo")