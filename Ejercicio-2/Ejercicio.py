#Partiendo del siguiente código y utilizando la menor cantidad de líneas, resuelva los siguientes puntos:

#1. Genere una lista con los valores no repetidos de la lista ‘repetidos’.
#2. Genere una lista con los valores en común entre la lista ‘r’ y ‘repetidos’
#3. Transforme ‘d_str’ en un diccionario. 
#Este ejercicio puede resolverse en una script independiente del ejercicio 1. 

from collections import OrderedDict
import json
repetidos = [1,2,3,"1","2","3",3,4,5]
r = [1,"5",2,"3"]
d_str = '{"valor":125.3,"codigo":123}'

#1
for i in range(len(repetidos)):
    repetidos[i] = int(repetidos[i])
print(set(repetidos))


#2
def convertir_a_numero(lista_1):
    for i in range(len(lista_1)):
        lista_1[i] = int(lista_1[i])
    return lista_1



def elementos_comunes(lista_1, lista_2):
    conjunto_1 = set(lista_1)
    conjunto_2 = set(lista_2)
    return list(conjunto_1 & conjunto_2)

repetidos = convertir_a_numero(repetidos)
r = convertir_a_numero(r)
resultado = elementos_comunes(repetidos, r)

print(resultado)


#3
aDict = json.loads(d_str)
print(aDict['valor'])