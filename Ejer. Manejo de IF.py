'''
Realizar un programa que lea dos números por teclado y permita elegir entre 3 opciones en un menú: 
Mostrar una suma de los dos números Mostrar una resta de los dos números (el primero menos el segundo) 
Mostrar una multiplicación de los dos números En caso de no introducir una opción válida, el programa 
informará que la opción no es correcta.
Instrucciones
Para la solución de este problema, se requiere que el usuario escriba un script en donde se enumeren tres posibilidades. 
En cada posibilidad, el usuario deberá ingresar dos números, los cuales tendrá que operar según la opción escogida. 
La primera opción será la suma (numero1+numero2) La segunda será la resta (numero1 - numero 2) 
La tercera opción es la multiplicación de los números (numero1 * numero2). 
Si hay un error al ingresar los números, se debe colocar un mensaje que indique: información incorrecta
'''
print('''
Menú:
1. Suma
2. Resta (el primer número menos el segundo)
3. Multiplicación
''')
opcion = int(input("Escoja una de las opciones del menú: "))
num1, num2 = (input("Escoja los dos números a operar: ")).split(",")
num1 = int(num1)
num2 = int(num2)

if opcion not in range(4):
   print("La opción no se encuentra dentro del menú")
else:
    if opcion == 1:
       resultado = num1+num2
    elif opcion == 2:
        resultado = num1-num2
    elif opcion == 3:
        resultado = num1*num2
    print("El resultado es: ", resultado)
    


    