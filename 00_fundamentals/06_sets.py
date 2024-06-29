### SETS ###

'''En Python, un set (conjunto) es una colección no ordenada de elementos únicos. 
Los sets son útiles cuando quieres almacenar elementos sin duplicados 
y realizar operaciones de conjuntos como unión, intersección y diferencia.

Características de los Sets

- No ordenado: Los elementos en un set no tienen un orden específico.
- Únicos: No permite elementos duplicados.
- Mutable: Puedes agregar y eliminar elementos después de la creación del set.
- No indexado: No puedes acceder a los elementos usando índices.
'''

'''
Cómo Crear un Set:

Puedes crear un set usando llaves {} o la función set().
'''

# Usando llaves
mi_set = {1, 2, 3, 4}
print(mi_set)  # Output: {1, 2, 3, 4}

# Usando la función set()
mi_otro_set = set([1, 2, 3, 4])
print(mi_otro_set)  # Output: {1, 2, 3, 4}



''' Operaciones Básicas
1. Agregar Elementos
Puedes agregar elementos a un set utilizando el método add().
'''

mi_set = {1, 2, 3}
mi_set.add(4)
print(mi_set)  # Output: {1, 2, 3, 4}

'''
2. Eliminar Elementos
Puedes eliminar elementos utilizando el método remove() o discard(). 
La diferencia es que remove() lanza un error si el elemento no está presente, 
mientras que discard() no lo hace.
'''

mi_set = {1, 2, 3, 4}
mi_set.remove(4)
print(mi_set)  # Output: {1, 2, 3}

mi_set.discard(3)
print(mi_set)  # Output: {1, 2}

# mi_set.remove(5)  # Esto lanzará un error porque 5 no está en el set.
mi_set.discard(5)  # Esto no lanzará ningún error.

'''
3. Operaciones de Conjuntos
Unión (union() o |): Combina los elementos de dos sets.
'''

mi_set = {1, 2, 3, 4}
mi_set.remove(4)
print(mi_set)  # Output: {1, 2, 3}

mi_set.discard(3)
print(mi_set)  # Output: {1, 2}

# mi_set.remove(5)  # Esto lanzará un error porque 5 no está en el set.
mi_set.discard(5)  # Esto no lanzará ningún error.

# Intersección (intersection() o &): Obtiene los elementos comunes entre dos sets.

set1 = {1, 2, 3}
set2 = {2, 3, 4}
intersect_set = set1.intersection(set2)
print(intersect_set)  # Output: {2, 3}

# Usando el operador &
intersect_set = set1 & set2
print(intersect_set)  # Output: {2, 3}


# Diferencia (difference() o -): Obtiene los elementos que están en el primer set pero no en el segundo.

set1 = {1, 2, 3}
set2 = {2, 3, 4}
diff_set = set1.difference(set2)
print(diff_set)  # Output: {1}

# Usando el operador -
diff_set = set1 - set2
print(diff_set)  # Output: {1}
'''Diferencia Simétrica (symmetric_difference() o ^): Obtiene los elementos que están en uno de los sets pero no en ambos.'''

set1 = {1, 2, 3}
set2 = {2, 3, 4}
sym_diff_set = set1.symmetric_difference(set2)
print(sym_diff_set)  # Output: {1, 4}

# Usando el operador ^
sym_diff_set = set1 ^ set2
print(sym_diff_set)  # Output: {1, 4}


#Ejemplos de Uso Práctico

#Eliminar duplicados de una lista'''

lista = [1, 2, 2, 3, 4, 4, 5]
set_sin_duplicados = set(lista)
print(set_sin_duplicados)  # Output: {1, 2, 3, 4, 5}


#Verificar si dos sets tienen elementos en común

set1 = {1, 2, 3}
set2 = {4, 5, 6}
if set1.isdisjoint(set2):
    print("Los sets no tienen elementos en común")
else:
    print("Los sets tienen elementos en común")