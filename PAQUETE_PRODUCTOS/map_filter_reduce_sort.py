def my_map(funcion, lista: list):
    lista_map = [] 
    for elemento in lista:
        elemento_modificado = funcion(elemento, lista)
        lista_map.append(elemento_modificado)
    return lista_map

def my_filter(funcion, lista: list):
    lista_filter = []
    for elemento in lista:
        if funcion(elemento):
            lista_filter.append(elemento)
    return lista_filter

def my_reduce(funcion, lista: list):
    variable = lista[0]
    for i in range(len(lista) - 1):
        variable = funcion(variable, lista[i+1])
    return variable

def my_sort(lista: list, criterio, criterio2, reverse: bool = False) -> list: #bubblesort
    for i in range(len(lista)-1):
        if reverse:
            for j in range( i+1, len(lista)):
                if criterio(lista[i]) < criterio(lista[j]):
                    aux = lista[i]
                    lista[i] = lista[j]
                    lista[j] = aux
                elif criterio(lista[i]) == criterio(lista[j]):
                    if criterio2(lista[i]) < criterio2(lista[j]):
                        aux = lista[i]
                        lista[i] = lista[j]
                        lista[j] = aux
        else:
            for j in range( i+1, len(lista)):
                if criterio(lista[i]) > criterio(lista[j]):
                    aux = lista[i]
                    lista[i] = lista[j]
                    lista[j] = aux
                elif criterio(lista[i]) == criterio(lista[j]):
                    if criterio2(lista[i]) > criterio2(lista[j]):
                        aux = lista[i]
                        lista[i] = lista[j]
                        lista[j] = aux
    return lista
