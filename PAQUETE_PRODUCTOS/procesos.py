# ############################################################################################################ #
################################################################################################################
##################                             VALIDACIONES                                   ##################
################################################################################################################
# ############################################################################################################ #

def validacion_rango(param: str, min: int | float, max: int | float, param_txt: str) -> int:
    '''
    Define el rango de valor de una variable\n
    :param param: Variable a la que se hace referencia
    :param min: Valor minimo del rango
    :param max: Valor maximo del rango
    :param param_txt: Nombre de la variable 
    '''
    while param < min or param > max:
        param = int(input(f'¡ERROR! {param_txt} debe estar entre {min} y {max}\nIngresa {param_txt} nuevamente: '))
    return param

def validacion_lista(param: str, param_validos: str | list, param_txt: str = 'parametro'):
    '''
    Valida si el paramtero ingresado se encuentra en los parametros validos
    :param param: Variable a la que se hace referencia
    :param param_validos: Paramteros validos para ingresar
    :param param_txt: Nombre de la variable
    '''
    while param not in param_validos:
        param = input(f'¡ERROR! Ingrese un valor valido para {param_txt}: ')
    return param

def validacion_continuar(mensaje: str) -> bool: 
    '''
    Pregunta al usuario si desea continuar.
    En caso afirmativo, ingresa una "s".
    Caso contrario, ingresa una "n".
    :mensaje:  Mensaje que se muestra al usuario para ingresar una opcion.
    '''
    opcion_continuar = input(mensaje)
    valores_continuar = ['s', 'n']
    opcion_continuar = validacion_lista(opcion_continuar, valores_continuar, 'continuar [s - n]')
    if opcion_continuar  == 's':
        return True
    else:
        return False

def validacion_int(param: any, param_txt: str = 'El numero', bucle: str = 's') -> int | None:
    '''
    Verifica si el dato es un entero indefinidamente
    :param: variable a la que se hace referencia
    :param_txt: nombre de la variable
    '''
    opciones = ['s', 'n']
    bucle = validacion_lista(bucle, opciones, 'bucle')
    if bucle == 's':
        while True:
            try:
                param = int(param)
                return param
            except ValueError:
                param = input(f'¡ERROR! {param_txt} debe ser un valor entero: ')
    else:
        try:
            param = int(param)
            return param
        except ValueError:
            print(f'¡ERROR! {param_txt} debe ser un valor entero')
    return None

#numero = 'pepe'
#print(f'Numero: {validacion_int(numero, bucle= 'f')}')

def validacion_float(param: any, param_txt: str = 'El numero', bucle: str = 's') -> float | None:
    '''
    Verifica si el dato es un flotante indefinidamente
    :param: variable a la que se hace referencia
    :param_txt: nombre de la variable
    '''
    opciones = ['s', 'n']
    bucle = validacion_lista(bucle, opciones, 'bucle')
    if bucle == 's':
        while True:
            try:
                param = float(param)
                return param
            except ValueError:
                param = input(f'¡ERROR! {param_txt} debe ser un valor flotante: ')
    else:
        try:
            param = float(param)
            return param
        except ValueError:
            print(f'¡ERROR! {param_txt} debe ser un valor flotante')
    return None

#numero = 'pepe'
#print(validacion_float(numero))

# ############################################################################################################ #
################################################################################################################
###################                            GET VARIABLES                                  ##################
################################################################################################################
# ############################################################################################################ #

def get_int(mensaje: str = 'Ingrese entero: ', mensaje_error: str = '¡ERROR!', minimo: int = None, maximo: int = None, reintentos: int = None) -> int | None:
    '''
    Verifica si el dato ingresado es un entero y se encuentra dentro de un rango con una cantidad de reintentos determinada
    :mensaje: Mensaje que se va a imprimir antes de pedirle al usuario el dato por consola.
    :mensaje_error: Mensaje de error en el caso de que el dato ingresado sea invalido.
    :mínimo: Valor minimo admitido (inclusive)
    :máximo: Valor maximo admitido (inclusive)
    :reintentos: Cantidad de veces que se volvera a pedir el dato en caso de error.
    '''
    if reintentos == 0:
        numero = input(mensaje)
        numero = validacion_int(numero, bucle='n')
        if numero == None or (maximo == None and minimo == None):
            return numero
        elif maximo == None:
            if numero >= minimo:
                return numero
            else:
                print(mensaje_error)
        elif minimo == None:
            if numero <= maximo:
                return numero
            else:
                print(mensaje_error)
        else:
            if minimo <= numero and numero <= maximo:
                return numero
            else:
                print(mensaje_error)
    elif reintentos == None:
        while True:
            numero = input(mensaje)
            numero = validacion_int(numero, bucle='s')
            if (maximo == None and minimo == None) or numero == None:
                return numero
            elif maximo == None:
                if numero >= minimo:
                    return numero
                else:
                    print(mensaje_error)
            elif minimo == None:
                if numero <= maximo:
                    return numero
                else:
                    print(mensaje_error)
            else:
                if minimo <= numero and numero <= maximo:
                    return numero
                else:
                    print(mensaje_error)
    else:
        for numero in range(reintentos):
            numero = input(mensaje)
            numero = validacion_int(numero, bucle='n')
            if numero == None:
                pass
            elif minimo == None and maximo == None:
                return numero
            elif maximo == None:
                if numero >= minimo:
                    return numero
                else:
                    print(mensaje_error)
            elif minimo == None:
                if numero <= maximo:
                    return numero
                else:
                    print(mensaje_error)
            else:
                if minimo <= numero and numero <= maximo:
                    return numero
                else:
                    print(mensaje_error)
        reintentos -= 1
    return None

#rtn = get_int('Ingrese un numero: ', '!ERROR¡ El numero no se encuentra dentro del rango', 3,reintentos=3)
#print(f'Numero: {rtn}')

def get_float(mensaje: str = 'Ingrese flotante: ', mensaje_error: str = '¡ERROR!', minimo: float = None, maximo: float = None, reintentos: int = None) -> float | None:
    '''
    Verifica si el numero flotante ingresado se encuentra dentro de un rango con una cantidad de reintentos determinada
    :mensaje: Mensaje que se va a imprimir antes de pedirle al usuario el dato por consola.
    :mensaje_error: Mensaje de error en el caso de que el dato ingresado sea invalido.
    :mínimo: Valor minimo admitido (inclusive)
    :máximo: Valor maximo admitido (inclusive)
    :reintentos: Cantidad de veces que se volvera a pedir el dato en caso de error.
    '''
    if reintentos == 0:
        numero = input(mensaje)
        numero = validacion_int(numero, bucle='n')
        if numero == None or (maximo == None and minimo == None):
            return numero
        elif maximo == None:
            if numero >= minimo:
                return numero
            else:
                print(mensaje_error)
        elif minimo == None:
            if numero <= maximo:
                return numero
            else:
                print(mensaje_error)
        else:
            if minimo <= numero and numero <= maximo:
                return numero
            else:
                print(mensaje_error)
    elif reintentos == None:
        while True:
            numero = input(mensaje)
            numero = validacion_float(numero, bucle='s')
            if (maximo == None and minimo == None) or numero == None:
                return numero
            elif maximo == None:
                if numero >= minimo:
                    return numero
                else:
                    print(mensaje_error)
            elif minimo == None:
                if numero <= maximo:
                    return numero
                else:
                    print(mensaje_error)
            else:
                if minimo <= numero and numero <= maximo:
                    return numero
                else:
                    print(mensaje_error)
    else:
        for numero in range(reintentos):
            numero = input(mensaje)
            numero = validacion_float(numero, bucle='n')
            if numero == None:
                pass
            elif minimo == None and maximo == None:
                return numero
            elif maximo == None:
                if numero >= minimo:
                    return numero
                else:
                    print(mensaje_error)
            elif minimo == None:
                if numero <= maximo:
                    return numero
                else:
                    print(mensaje_error)
            else:
                if minimo <= numero and numero <= maximo:
                    return numero
                else:
                    print(mensaje_error)
        reintentos -= 1
    return None

#rtn = get_float('Ingrese un numero: ','!ERROR¡ El numero no se encuentra dentro del rango',6.33, reintentos=3)
#print(f'Numero: {rtn}')

def get_str(mensaje: str = 'Ingrese texto: ', mensaje_error: str = '¡ERROR!', longitud: int = None, reintentos: int = None) -> str|None:
    '''
    Verifica si la palabra ingresada se encuentra dentro de la longitud determinada
    :mensaje: Mensaje que se va a imprimir antes de pedirle al usuario el dato por consola.
    :mensaje_error: Mensaje de error en el caso de que el dato ingresado sea invalido.
    :longitud: Maximo numero de letras admitidas en la palabra.
    :reintentos: Cantidad de veces que se volvera a pedir el dato en caso de error.
    '''
    if reintentos == 0:
        if longitud == None:
            texto = str(input(mensaje))
            if not any(letra.isdigit() for letra in texto):
                return texto
        else:
            texto = str(input(mensaje))
            if len(texto) <= longitud and not any(letra.isdigit() for letra in texto):
                return texto
            else:
                print(mensaje_error)
    elif reintentos == None:
        while True:
            if longitud == None:
                texto = str(input(mensaje))
                if not any(letra.isdigit() for letra in texto):
                    return texto
                else:
                    print('No se pueden ingresar digitos')
            else:
                texto = str(input(mensaje))
                if len(texto) <= longitud and not any(letra.isdigit() for letra in texto):
                    return texto
                else:
                    print(mensaje_error)
    else:
        for texto in range(reintentos):
            texto = str(input(mensaje))
            if len(texto) <= longitud and not any(letra.isdigit() for letra in texto):
                return texto
            else:
                print(mensaje_error)
                reintentos -= 1
        return None

#rtn = get_str('Ingrese una cadena de texto: ', '!ERROR¡ La cadena de texto excede la longitud maxima')
#print(f'Palabra: {rtn}')

# ############################################################################################################ #
################################################################################################################
######################                             LISTAS                                 ######################
################################################################################################################
# ############################################################################################################ #

def suma_numeros_lista(lista: list) -> int:
    '''
    Suma los numeros de una determinada lista
    :lista: Lista a analizar
    '''
    suma_numeros = 0
    for numero in lista:
        suma_numeros += numero
    return suma_numeros 

#lista = [-10, 2, 20, 3, 10]
#import os
#os.system('cls')
#print(f'---------\n{suma_numeros_lista(lista)}\n---------')

def mayor_num_lista(lista: list) -> int:
    '''
    Busca el numero mas grande dentro de una determinada lista
    :lista: Lista a analizar
    '''
    for numero in lista:
        if numero == lista[0]:
            mayor_numero = numero
        else:
            if numero > mayor_numero:
                mayor_numero = numero
    return mayor_numero

#lista = [555, -22222, 20, 556, 10]
#import os
#os.system('cls')
#print(f'---------\n{mayor_num_lista(lista)}\n---------')
'''
from MODULOS.operaciones import es_primo #Comentar el llamado para probar los print comentados
def primos_lista(lista: list) -> list:
    
    Genera una lista de los numeros primos de una determinada lista
    :lista: Lista a analizar
    
    lista_primos = []
    for numero in lista:
        if es_primo(numero):
            lista_primos.append(numero)
    return lista_primos

#lista = [2, 1, 3, 9, 5, 8, 7, 11, 999, 199, 3030, 444, 151, 101, 1997]
#import os
#os.system('cls')
#print(f'---------\n{primos_lista(lista)}\n---------')
'''

# ############################################################################################################ #
################################################################################################################
######################                          ORDENAMIENTO                              ######################
################################################################################################################
# ############################################################################################################ #

def quick_sort(lista: list, criterio = lambda x: x, reversa: bool = False) -> list:
    '''
    Ordena la lista de manera creciente (menor a mayor)
    :lista: Lista a ordenar
    :reversa:
    '''
    lista_aux = lista.copy()
    if len(lista_aux) <=1:
        return lista
    
    pivote = lista_aux.pop()

    elementos_mas_chicos = []
    elementos_mas_grandes = []
    
    for elemento in lista_aux:
        if elemento > pivote:
            elementos_mas_grandes.append(elemento)
        else:
            elementos_mas_chicos.append(elemento)
    if reversa:
        lista_ordenada = quick_sort(elementos_mas_grandes, True) + [pivote] + quick_sort(elementos_mas_chicos, True)
        return lista_ordenada
    else:
        lista_ordenada = quick_sort(elementos_mas_chicos) + [pivote] + quick_sort(elementos_mas_grandes)
        return lista_ordenada

def bubble_sort(lista: list, criterio, reversa: bool = False) -> list:
    '''
    Ordena la lista de menor a mayor o de mayor a menor
    :lista: Lista a ordenar
    :criterio: Criterio de ordenamiento
    :reversa: Realizarlo de mayor a menor
    '''
    for i in range(len(lista)-1):
        if reversa:
            for j in range( i+1, len(lista)):
                if criterio(lista[i]) < criterio(lista[j]):
                    aux = lista[i]
                    lista[i] = lista[j]
                    lista[j] = aux
        else:
            for j in range( i+1, len(lista)):
                if criterio(lista[i]) > criterio(lista[j]):
                    aux = lista[i]
                    lista[i] = lista[j]
                    lista[j] = aux
        return lista

def selection_sort(lista: list) -> list:
    # Tomo un elemento de la lista
    for i in range(len(lista)-1): 
        # En el mejor de los casos, el elemento mas chico esta en el indice i
        indice_del_minimo = i
        # Recorro el resto de la lista para buscar si hay un valor mas chico
        for j in range( i+1, len(lista)): 
            # Si encuentro un valor mas chicos, guardo su indice
            if lista[indice_del_minimo] > lista[j]:
                indice_del_minimo = j
        # Guardo el valor mas chico al principio de la lista
        aux = lista[i]
        lista[i] = lista[indice_del_minimo]
        lista[indice_del_minimo] = aux

# ############################################################################################################ #
################################################################################################################
######################                            BUSQUEDA                                ######################
################################################################################################################
# ############################################################################################################ #

def busqueda_lineal(lista: list, elemento_a_buscar: any) -> any:
    '''
    Busca un elemento en una lista
    :lista: Lista en la que busca
    :elemento_a_buscar: Elemento buscado
    '''
    for i in range(len(lista)):
        if lista[i] == elemento_a_buscar:
            return i
    return None

def busqueda_binaria(lista: list, elemento_a_buscar: any) -> any:
    '''
    La busqueda binaria siempre busca el valor del medio de un rango
    para intentar encontrar un valor. Esto nos permite descartar multiples 
    valores por iteracion. Recordar que la lista DEBE estar ordenada para 
    usar esta busqueda
    :lista: Lista en la que busca
    :elemento_a_buscar: Elemento buscado
    '''
    indice_minimo = 0
    indice_maximo = len(lista) - 1 #indice maximo de cualquier lista

    # si el indice minimo supera el maximo significa que el valor no se encuentra
    # en la lista
    while indice_minimo <= indice_maximo: 
        medio = (indice_maximo + indice_minimo) // 2 #Calculo el valor del medio

        # Si encuentro el elemento retorno su indice
        if lista[medio] == elemento_a_buscar: 
            return medio
        # Si el elemento actual no es el buscado, pregunto si el elemento es
        # mayor o menor que el elemento actual
        else:
            if lista[medio] < elemento_a_buscar:
                # Descarto todos los elementos menores, junto al elemento actual
                indice_minimo = medio + 1
            else:
                # Descarto todos los elementos mayores, junto al elemento actual
                indice_maximo = medio - 1
    # En caso de que el valor no exista retorno None
    return None