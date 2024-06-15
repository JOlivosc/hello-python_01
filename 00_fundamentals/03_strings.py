### Strings ###

my_string = "Mi String"
my_other_string = 'Mi otro String'

print(len(my_string))
print(len(my_other_string))

print(my_string + "  " + my_other_string)

my_new_line_string = "Este es un String\ncon salto de linea"
print(my_new_line_string)

my_tab_string = "Este es un String con tabulación"
print(my_tab_string)

my_scape_string = "\tEste es un String \n escapado"
print(my_scape_string)

### Formating ###

name, surname, age = "Jaime", "Olivos", 38

print("Mi nombre es {} {} y mi edad es {}". format(name, surname, age)) # Esta es la forma correcta de formatear
print("Mi nombre es %s %s y mi edad es %d" %(name, surname, age)) # Esta forma tb está bien. 
print("Mi nombre es " + name + " " + surname + " y mi edad es " + str(age)) # Esta no se recomienda. El lenguaje tarda mas en procesar esto. Codigo poco limpio. Mala practica
print(f"Mi nombre es {name} {surname} y mi edad es {age}") # Esta forma es la mejor, es mas facil, se ven donde quieres ver los datos. 

### Desenpaquetado de caracteres ###

