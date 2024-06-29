# Ejercicio 1
# - Escribir un programa que muestre por pantalla la cadena ¡Hola Mundo!.

print("¡Hola Mundo!")


# Ejercicio 2
# - Escribir un programa que almacene la cadena ¡Hola Mundo! en una variable y luego muestre por pantalla el contenido de la variable.

mensaje = "¡Hola Mundo!"
print(mensaje)


# Ejercicio 3
# - Escribir un programa que pregunte el nombre del usuario en la consola 
# y después de que el usuario lo introduzca muestre por pantalla 
# la cadena ¡Hola <nombre>!, donde <nombre> es el nombre que el usuario haya introducido.

nombre = input("¿Cuál es tu nombre? ")
print(f"¡Hola {nombre}!")


# Ejercicio 4
# Escribir un programa que muestre por pantalla el resultado de la siguiente operación aritmética (3+2)/(2*5)

resultado = ((3 + 2) / (2 * 5)) ** 2
print(resultado)


# Ejercicio 5
#Escribir un programa que pregunte al usuario por el número de horas trabajadas y el coste por hora. 
#Después debe mostrar por pantalla la paga que le corresponde.

horas_trabajadas = float(input("Introduce el número de horas trabajadas: "))
coste_por_hora = float(input("Introduce el coste por hora: "))
paga = horas_trabajadas * coste_por_hora
print(f"La paga que te corresponde es: {paga}")


# Ejercicio 6
# - Escribir un programa que lea un entero porsitivo, $n$, introducido por el usuario y después 
# muestre en pantalla la suma de todos los enteros desde 1 hasta $n$. 
# La suma de los $n$ primeros enteros positivos puede ser calculada de la siguiente forma: 
# $$ \mbox{suma} = \frac{n(n+1)}{2} $$

n = int(input("Introduce un número entero: "))
suma = n * (n + 1) / 2
print("La suma de los primeros números enteros desde 1 hasta " + str(n) + " es " + str(suma))

# Ejercicio 7
# - Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros), 
# calcule el índice de masa corporal y lo almacene en una variable, 
# y muestre por pantalla la frase "Tu índice de masa corporal es <imc>",
# donde <imc> es el índice de masa corporal calculado redondeado con dos decimales.

peso = float(input("Introduce tu peso en kg: "))
estatura = float(input("Introduce tu estatura en metros: "))
imc = peso / (estatura ** 2)
print(f"Tu índice de masa corporal es {imc:.2f}")


#Ejercicio 8
# - Escribir un programa que pida al usuario dos números enteros y muestre 
# por pantalla la <n> entre <m> da un cociente <c> y un resto <r> donde <n> 
# y <m> son los números introducidos por el usuario, 
# y <c> y <r> son el cociente y el resto de la división entera respectivamente.

n = int(input("Introduce el primer número entero (n): "))
m = int(input("Introduce el segundo número entero (m): "))
cociente = n // m
resto = n % m
print(f"{n} entre {m} da un cociente {cociente} y un resto {resto}")


# Ejercicio 9
# - Escribir un programa que pregunte al usuario una cantidad a invertir, 
# el interés anual y el número de años, y muestre por pantalla el capital obtenido en la inversión.

cantidad_invertir = float(input("Introduce la cantidad a invertir: "))
interes_anual = float(input("Introduce el interés anual (en %): "))
numero_anos = int(input("Introduce el número de años: "))
capital_final = cantidad_invertir * (1 + interes_anual / 100) ** numero_anos
print(f"El capital obtenido después de {numero_anos} años es: {capital_final:.2f}")

# Ejercicio 10
# - Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas. 
# Suele hacer venta por correo y la empresa de logística les cobra por peso de cada 
# paquete así que deben calcular el peso de los payasos y muñecas que saldrán 
# en cada paquete a demanda. Cada payaso pesa 112 g y cada muñeca 75 g. 
# Escribir un programa que lea el número de payasos y muñecas vendidos en el último pedido y calcule el peso total del paquete que será enviado.

# Definir los pesos de los payasos y muñecas
peso_payaso = 112  # Peso de cada payaso en gramos
peso_muneca = 75   # Peso de cada muñeca en gramos

# Preguntar al usuario el número de payasos vendidos
num_payasos = int(input("Introduce el número de payasos vendidos: "))

# Preguntar al usuario el número de muñecas vendidas
num_munecas = int(input("Introduce el número de muñecas vendidas: "))

# Calcular el peso total del paquete
peso_total = (num_payasos * peso_payaso) + (num_munecas * peso_muneca)

# Mostrar el peso total del paquete por pantalla
print(f"El peso total del paquete es: {peso_total} gramos")


# Ejercicio 11
# - Imagina que acabas de abrir una nueva cuenta de ahorros que te ofrece el 4% de interés al año.
# Estos ahorros debido a intereses, que no se cobran hasta finales de año, se te añaden al balance final de tu cuenta de ahorros. 
# Escribir un programa que comience leyendo la cantidad de dinero depositada en la cuenta de ahorros, introducida por el usuario. 
# Después el programa debe calcular y mostrar por pantalla la cantidad de ahorros tras el primer, segundo y tercer años. 
# Redondear cada cantidad a dos decimales.

# Pedir al usuario la cantidad de dinero depositada
deposito_inicial = float(input("Introduce la cantidad de dinero depositada en la cuenta de ahorros: "))

# Definir el interés anual
interes_anual = 0.04

# Calcular la cantidad de ahorros tras el primer año
ahorros_1er_ano = deposito_inicial * (1 + interes_anual)

# Calcular la cantidad de ahorros tras el segundo año
ahorros_2do_ano = ahorros_1er_ano * (1 + interes_anual)

# Calcular la cantidad de ahorros tras el tercer año
ahorros_3er_ano = ahorros_2do_ano * (1 + interes_anual)

# Mostrar los resultados redondeados a dos decimales
print(f"La cantidad de ahorros tras el primer año es: {ahorros_1er_ano:.2f}")
print(f"La cantidad de ahorros tras el segundo año es: {ahorros_2do_ano:.2f}")
print(f"La cantidad de ahorros tras el tercer año es: {ahorros_3er_ano:.2f}")

# Ejercicio 12
# - Una panadería vende barras de pan a 3.49€ cada una. 
# El pan que no es el día tiene un descuento del 60%. 
# Escribir un programa que comience leyendo el número de barras vendidas que no son del día. 
# Después el programa debe mostrar el precio habitual de una barra de pan, 
# el descuento que se le hace por no ser fresca y el coste final total.

# Definir el precio habitual de una barra de pan
precio_normal = 3.49  # Euros

# Definir el descuento por ser pan del día anterior (60%)
descuento = 0.60

# Pedir al usuario el número de barras vendidas que no son del día
barras_no_frescas = int(input("Introduce el número de barras vendidas que no son del día: "))

# Calcular el precio total sin descuento
precio_total_sin_descuento = barras_no_frescas * precio_normal

# Calcular el descuento aplicado
descuento_aplicado = precio_total_sin_descuento * descuento

# Calcular el coste final total
coste_final = precio_total_sin_descuento - descuento_aplicado

# Mostrar los resultados
print(f"Precio habitual de una barra de pan: {precio_normal:.2f} €")
print(f"Descuento por ser pan del día anterior ({descuento*100}%): {descuento_aplicado:.2f} €")
print(f"Coste final total: {coste_final:.2f} €")
