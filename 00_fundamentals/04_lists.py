### Listas ###

my_list = list() # dos formas de definir listas
my_other_list = [] # Segunda forma. 

print(len(my_list))

my_list = [35, 24, 62, 52, 30, 30, 27]

print(my_list)
print(len(my_list))

my_other_list = [38, 1.69, "Jaime", "Olivos"]

print(type(my_list))
print(type(my_other_list))

print(my_other_list[0])
print(my_other_list[1])
print(my_other_list[-1])
print(my_other_list[-4])
print(my_list.count(30)) # Es para saber cuantas veces se repite, en este caso, el número 30. 
#print(my_other_list[-5]) # IndexError. Ya que estamos fuera de rango, no tiene elemento para "contar", ya que en la lista hay solo 4 datos. 0 al 3
#print(my_other_list[4]) # IndexError. Ya que estamos fuera de rango, no tiene elemento para "contar", ya que en la lista hay solo 4 datos.  0 al 3

age, height, name, surname = my_other_list
print(name)

name, height, age, surname = my_other_list[2], my_other_list[1], my_other_list[0], my_other_list[3]
print(age)

print(my_list + my_other_list)

#print(my_list - my_other_list)

my_other_list.append("Jaimoco")
print(my_other_list)

my_other_list.insert(1, "Azul")
print(my_other_list)

my_other_list.remove("Azul")
print(my_other_list)

print(my_list.pop(2))
print(my_list)

my_pop_element = my_list.pop(2)
print(my_pop_element)
print(my_list)

del my_list[2]
print(my_list)

my_new_list = my_list.copy() 

my_list.clear()
print(my_list)
print(my_new_list)

my_new_list.reverse()
print(my_new_list)

my_new_list.sort()
print(my_new_list)

my_list = "Hola Python"
print(my_list)
print(type(my_list))

