### Tuples ###

'''Características de las Tuplas
Inmutabilidad: Una vez que se crea una tupla, no se pueden modificar sus elementos.

Ordenadas: Los elementos en una tupla tienen un orden definido, y este orden no puede cambiar.

Heterogéneas: Pueden contener elementos de diferentes tipos (números, cadenas, listas, otras tuplas, etc.).

Acceso por índice: Puedes acceder a los elementos de una tupla utilizando su índice, comenzando desde 0 para el primer elemento.
'''

'''
Ventajas de las Tuplas

Eficiencia: Las tuplas suelen ser más eficientes en términos de uso de memoria y tiempo de procesamiento comparado con las listas, debido a su inmutabilidad.

Seguridad: La inmutabilidad de las tuplas puede hacer que el código sea más seguro, ya que los datos no pueden ser modificados accidentalmente.

Conclusión
Las tuplas son una herramienta poderosa y útil en la programación que ofrece una forma eficiente de agrupar y proteger conjuntos de datos. 
Son especialmente útiles cuando necesitas una colección de elementos que no debe cambiar a lo largo del tiempo.
'''

my_tuple = tuple() # estas es una forma de definir. 
my_other_tuple = () # esta es la otra forma de definir

my_tuple = (38, 1.69, "Jaime", "Olivos")
print(my_tuple)
print(type(my_tuple))

print(my_tuple[0])
print(my_tuple[-1])
#print(my_tuple[-4]) IndexError
#print(my_tuple[-6]) IndexError

print(my_tuple.count("Jaime")) #Para contar 
print(my_tuple.index("Olivos")) #Indice

my_sum_tumple = my_tuple + my_other_tuple
print(my_sum_tumple)

my_other_tuple = ("Azul", "Amarillo","Rojo", "Verde")
print(my_tuple + my_other_tuple)

print (my_sum_tumple[3:6])

#del my_tuple[2] TypeError: 'tuple' object doesn't support item deletion

del my_tuple
#print(my_tuple) NameError: name 'my_tuple' is not defined