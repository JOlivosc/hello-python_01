# Variables

my_string_variable = 'My String variable'
print(my_string_variable)

my_int_variable = 5
print(my_int_variable)

my_bool_variable = False
print(my_bool_variable)

my_int_to_str_variable = str(my_int_variable)
print(my_int_to_str_variable)
print(type(my_int_to_str_variable))

#Concatenación de variables en un print
print(my_string_variable, my_int_to_str_variable, my_bool_variable)
print("Este es el valor de:", my_bool_variable)

# Funciones del sistema
print(len(my_string_variable))

#Variables en una sola línea. Cuidado con abusar de esta sintaxis!
name, surname, alias, age = "Jaime", "Olivos", "Jaimoco", 38
print("Me llamo:", name, surname, "Mi edad es:", age, "Y mi alias es:", alias)

# Inputs - Nos pide datos por teclado
first_name = input('Cual es tu nombre?')
age = input("Cual es tu edad?")

print(first_name)
print(age)

