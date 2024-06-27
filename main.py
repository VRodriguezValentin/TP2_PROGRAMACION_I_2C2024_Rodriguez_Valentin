import os
import re
import PAQUETE_PRODUCTOS.procesos as ps
import PAQUETE_PRODUCTOS.menu as m
import PAQUETE_PRODUCTOS.productos as prod
import PAQUETE_PRODUCTOS.depositos as depo
import PAQUETE_PRODUCTOS.map_filter_reduce_sort as mfrs


def validar_codigo(codigo):
    patron = r'^\d{4}-[A-Z]{2}$'
    if re.match(patron, codigo):
        return True
    else:
        return False
    
def validar_peso(peso):
    patron = r'^\d+\s?(g|gr)$'
    if re.match(patron, peso):
        return True
    else:
        return False
def validar_cuil(cuil):
    patron = r'^\d{2}-\d{8}-\d$'
    if re.match(patron, cuil):
        return True
    else:
        return False


def main():
    #<inicializacion de variables>
    opciones = ['0','1','2','3','4','5','6','7','8','9','10']
    opciones_menu = ['Alta de Producto', 'Baja de Producto', 'Modificacion de Producto', 'Listado de Productos', 'Importar Producto', 'Vender Producto', 'Listar Estado de Depositos','Bucar Producto con Menos Stock','Filtrar Productos por Precio de Media','Ordenar Depositos por Peso']
    vector_total_productos = prod.Producto.productos_listar_cantidad('DB_PRODUCTOS.csv')
    vector_codigos = prod.Producto.productos_listar('DB_PRODUCTOS.csv')
    lista_aux = []
    #</inicializacion de variables>

    while True:
        opcion = m.menu('MENU PRODUCTOS',opciones_menu)
        opcion = ps.validacion_lista(opcion, opciones, 'opcion')
        os.system('cls')

        if opcion == '0':
            print('¡Hasta luego!')
            break
        else:
            match opcion:
                case '1':
                    os.system('cls')
                    print('╔══════════════════════════════════════════════════╗\n\t\t   Alta de Producto\n╚══════════════════════════════════════════════════╝\n')
                    while True:
                        codigo = input('Formato: [NNNN-XX]\nIngrese un codigo: ')
                        codigo_valido = validar_codigo(codigo)
                        if codigo_valido == False:
                            os.system('cls')
                            print('¡ERROR! El codigo no es valido\n')
                            break
                        else:
                            existe_codigo = False
                            for producto in vector_codigos:
                                if codigo in producto:
                                    print('[ERROR] Ítem existente.')
                                    existe_codigo = True
                                    break
                            if existe_codigo:
                                break
                            else:
                                while True:
                                    os.system('cls')
                                    detalle = ps.get_str('Ingrese el nombre del producto: ', '¡ERROR! El nombre del producto no es valido', 25)
                                    detalle = detalle.capitalize()
                                    if len(detalle) > 1:
                                        break
                                os.system('cls')
                                usd_compra = ps.get_float('Ingrese un valor de importacion: ','¡ERROR! El valor de importacion no es valido', 0)
                                os.system('cls')
                                usd_venta = ps.get_float('Ingrese un valor de comercializacion: ','¡ERROR! El valor de comercializacion no es valido', 0)
                                os.system('cls')
                                cantidad_productos = ps.get_int('Ingrese la cantidad de productos: ','¡ERROR! La cantidad de productos no es valida', 0)
                                os.system('cls')
                                while True:
                                    peso = input('Formato: [(num)gr | (num)g]\nIngrese un peso: ')
                                    peso_valido = validar_peso(peso)
                                    if peso_valido == False:
                                        os.system('cls')
                                        print('¡ERROR! El peso no es valido\n')
                                    else:
                                        break
                                os.system('cls')
                                vector_codigos.append([codigo, detalle, usd_compra, usd_venta, peso, cantidad_productos])
                                vector_total_productos.append((codigo, cantidad_productos))

                                lista_aux = vector_codigos.copy()
                                nuevo_producto = lista_aux.pop()
                                prod.Producto.producto_alta('DB_PRODUCTOS.csv',nuevo_producto)
                                depo.Gestion.log(f'Alta de producto. PRODUCTO {codigo}')
                                for producto in vector_codigos:
                                    if codigo in producto:
                                        print(f'Producto: {producto}')
                                        break
                                for total in vector_total_productos:
                                    if codigo in total:
                                        print(f'Total de productos: {total}')
                                break

                case '2':
                    os.system('cls')
                    print('╔══════════════════════════════════════════════════╗\n\t    Baja de Producto\n╚══════════════════════════════════════════════════╝\n')
                    while True:
                        retorno = prod.Producto.productos_listar('DB_PRODUCTOS.csv')
                        for productos in retorno:
                            print(f'{productos}\n')
                        codigo_aux = input('Formato: [NNNN-XX]\nIngrese un codigo: ')
                        codigo_valido = validar_codigo(codigo_aux)
                        if codigo_valido == False: 
                            os.system('cls')
                            print('¡ERROR! El codigo no es valido\n')
                            break
                        else:
                            existe_codigo = False
                            for producto in vector_codigos:
                                if codigo_aux in producto:
                                    existe_codigo = True
                                    break
                            if existe_codigo == False:
                                print('[ERROR] Ítem no existente.')
                                break
                            else:
                                continuar = False
                                for cant in vector_total_productos:
                                        if codigo_aux in cant:
                                            if cant[1] == '0' or cant[1] == 0:
                                                continuar = True
                                                vector_codigos.remove(producto)
                                                vector_total_productos.remove(cant)
                                                break
                                if continuar:
                                    retorno = prod.Producto.producto_baja('DB_PRODUCTOS.csv', vector_codigos)
                                    if retorno:
                                        os.system('cls')
                                        print(f'Producto: {producto}\nProducto dado de baja')
                                    break
                                else:
                                    print('[ERROR] Ítem con stock')
                                    break

                case '3':
                    os.system('cls')
                    print('╔═════════════════════════════════════════════════════╗\n\t    Modificación de Producto\n╚═════════════════════════════════════════════════════╝\n')
                    while True:
                        retorno = prod.Producto.productos_listar('DB_PRODUCTOS.csv')
                        for productos in retorno:
                            print(f'{productos}\n')
                        codigo_aux = input('Formato: [NNNN-XX]\nIngrese un codigo: ')
                        codigo_valido = validar_codigo(codigo_aux)
                        if codigo_valido == False:
                            os.system('cls')
                            print('¡ERROR! El codigo no es valido\n')
                            break
                        else:
                            existe_codigo = False
                            for producto in vector_codigos:
                                if codigo_aux in producto:
                                    existe_codigo = True
                                    break
                            if existe_codigo == False:
                                print('[ERROR] Ítem no existente.')
                                break
                            else:
                                cambiar_usd_compra = ps.validacion_continuar('¿Desea modificar el valor de importacion?\n => ')
                                if cambiar_usd_compra:
                                    usd_compra_mod = ps.get_float('Ingrese un valor de importacion: ','¡ERROR! El valor de importacion no es valido', 0)
                                    for producto in vector_codigos:
                                        if codigo_aux in producto:
                                            producto[2] = usd_compra_mod
                                            print(f'Producto actualizado: {producto}')
                                    rtn1 = prod.Producto.producto_modificar_compra('DB_PRODUCTOS.csv', codigo_aux, vector_codigos, usd_compra_mod)
                                    print(rtn1)
                                
                                cambiar_usd_venta = ps.validacion_continuar('¿Desea modificar el valor de comercializacion?\n => ')
                                if cambiar_usd_venta:
                                    usd_venta_mod = ps.get_float('Ingrese un valor de comercializacion: ','¡ERROR! El valor de comercializacion no es valido', 0)
                                    for producto in vector_codigos:
                                        if codigo_aux in producto:
                                            producto[3] = usd_venta_mod
                                            print(f'Producto actualizado: {producto}')
                                    rtn2 = prod.Producto.producto_modificar_venta('DB_PRODUCTOS.csv', codigo_aux, vector_codigos, usd_venta_mod)
                                    print(rtn2)
                                break

                case '4':
                    os.system('cls')
                    print('╔═════════════════════════════════════════════════════╗\n\t\t Listado de Productos\n╚═════════════════════════════════════════════════════╝\n')
                    retorno = prod.Producto.productos_listar('DB_PRODUCTOS.csv')
                    for productos in retorno:
                        print(f'{productos}\n')

                case '5':
                    os.system('cls')
                    print('╔═════════════════════════════════════════════════════╗\n\t\t Importar Producto\n╚═════════════════════════════════════════════════════╝\n')
                    while True:
                        retorno = prod.Producto.productos_listar('DB_PRODUCTOS.csv')
                        for productos in retorno:
                            print(f'{productos}\n') 
                        codigo_aux = input('Formato: [NNNN-XX]\nIngrese un codigo: ')
                        codigo_valido = validar_codigo(codigo_aux)
                        if codigo_valido == False:
                            os.system('cls')
                            print('¡ERROR! El codigo no es valido\n')
                            break
                        else:
                            existe_codigo = False
                            for producto in vector_codigos:
                                if codigo_aux in producto:
                                    existe_codigo = True
                                    break
                            if existe_codigo == False:
                                print('[ERROR] Ítem no existente.')
                                break
                            else:
                                for cant in vector_total_productos:
                                    if codigo_aux in cant:
                                        cantidad = int(cant[1])
                                        print(f'Cantidad total: {cantidad}')
                                        cantidad_importar = ps.get_int('Ingrese la cantidad de productos a importar: ','¡ERROR! La cantidad de productos no es valida', 0, cantidad)
                                        os.system('cls')
                                        depo.Gestion.importar('DEPOSITOS.json', codigo_aux, cantidad_importar)
                                        print(f'Producto {codigo_aux} importado con exito!')
                                        break
                        break

                case '6':
                    os.system('cls')
                    print('╔═════════════════════════════════════════════════════╗\n\t\t Vender Producto\n╚═════════════════════════════════════════════════════╝\n')
                    while True:
                        retorno = prod.Producto.productos_listar('DB_PRODUCTOS.csv')
                        for productos in retorno:
                            print(f'{productos}\n')
                        codigo_aux = input('Formato: [NNNN-XX]\nIngrese un codigo: ')
                        codigo_valido = validar_codigo(codigo_aux)
                        if codigo_valido == False:
                            os.system('cls')
                            print('¡ERROR! El codigo no es valido\n')
                        else:
                            existe_codigo = False
                            for producto in vector_codigos:
                                if codigo_aux in producto:
                                    existe_codigo = True
                                    break
                            if existe_codigo == False:
                                print('[ERROR] Ítem no existente.')
                                break
                            else:
                                for cant in vector_total_productos:
                                    if codigo_aux in cant:
                                        cantidad = int(cant[1])
                                        print(f'Cantidad: {cantidad}')
                                        cantidad_seleccionar = ps.get_int('Ingrese la cantidad: ','¡ERROR! La cantidad no es valida', 0, cantidad)
                                        break
                        
                                cuil = input('Formato: [NN-NNNNNNNN-N]Ingrese el CUIL del comprador: ')
                                cuil_valido = validar_cuil(cuil)
                                if cuil_valido == False:
                                    print('[ERROR] El CUIL no es valido')
                                    break
                                else:
                                    cotizacion_usd = ps.get_float('Ingrese un valor de cotizacion: ','¡ERROR! El valor de cotizacion no es valido', 1) 
                                    rtn = depo.Gestion.vender('DEPOSITOS.json', 'DB_PRODUCTOS.csv', codigo_aux, cantidad_seleccionar, cuil, cotizacion_usd)
                                    if rtn == True:
                                        prod.Producto.producto_modificar_cantidad('DB_PRODUCTOS.csv',codigo_aux,vector_codigos,cantidad_seleccionar)
                                        print('Venta realizada con exito')
                                    break

                case '7':
                    os.system('cls')
                    print('╔═════════════════════════════════════════════════════╗\n\t    Listar Estado de Depositos\n╚═════════════════════════════════════════════════════╝\n')
                    depositos = depo.Gestion.cargar_depositos('DEPOSITOS.json')
                    for deposito in depositos:
                        capacidad_dispo = depo.Deposito.__len__(deposito)
                        capacidad_max = deposito.capacidad
                        ocupado = capacidad_max - capacidad_dispo
                        print(f'ID {deposito.id} - {ocupado}/{capacidad_max} - Disponible {capacidad_dispo}')

                case '8':
                    os.system('cls')
                    print('╔═════════════════════════════════════════════════════╗\n\t    Buscar Producto con Menos Stock\n╚═════════════════════════════════════════════════════╝\n')
                    depositos = depo.Gestion.cargar_depositos('DEPOSITOS.json')

                    stock_productos = {}
                    stock_depositos = {}
                    
                    for deposito in depositos:
                        id_deposito = deposito.id
                        for producto in vector_codigos:
                            codigo_producto = producto[0]
                            for dict in deposito.stock:
                                if dict['item'] in codigo_producto:
                                    cantidad = dict['cantidad']
                                    if codigo_producto not in stock_productos:
                                        stock_productos[codigo_producto] = 0
                                    stock_productos[codigo_producto] += cantidad
                    
                                    if codigo_producto not in stock_depositos:
                                        stock_depositos[codigo_producto] = []
                                    stock_depositos[codigo_producto].append((id_deposito, cantidad))
                    
                    producto_menos_stock = mfrs.my_reduce(lambda a, b: a if stock_productos[a] < stock_productos[b] else b, list(stock_productos.keys()))
                    total_stock_menos = stock_productos[producto_menos_stock]
                    
                    print(f'[PRODUCTO {producto_menos_stock}]\n')
                    print(f'TOTAL STOCK: {total_stock_menos}\n')
                    for deposito, cantidad in stock_depositos[producto_menos_stock]:
                        print(f'Deposito {deposito}: {cantidad}\n')

                case '9':
                    os.system('cls')
                    print('╔═════════════════════════════════════════════════════╗\n\tFiltrar Productos por Precio de Media\n╚═════════════════════════════════════════════════════╝\n')
                    lista_precio_producto = []
                    for producto in vector_codigos:
                        lista_precio_producto.append(producto[2])
                    
                    acumulador_precio = mfrs.my_reduce(lambda a, b: float(a) + float(b), lista_precio_producto)
                    precio_medio = acumulador_precio / len(lista_precio_producto)
                    print(f'\nPrecio medio de compra: {precio_medio:.2f}\n')

                    menor_precio_medio = mfrs.my_filter(lambda x: float(x) < precio_medio, lista_precio_producto)

                    print('Productos:\n')
                    for producto in vector_codigos:
                        if producto[2] in menor_precio_medio:
                            print(f'\n{producto}')

                case '10':
                    os.system('cls')
                    print('╔═════════════════════════════════════════════════════╗\n\t    Ordenar Depositos por Peso\n╚═════════════════════════════════════════════════════╝\n')
                    depositos = depo.Gestion.cargar_depositos('DEPOSITOS.json')
                    lista_sumatorias = []

                    for deposito in depositos:
                        sumatoria_pesos = 0
                        id_deposito = deposito.id
                        for producto in vector_codigos:
                            for dict in deposito.stock:
                                if dict['item'] in producto[0]:
                                    peso_base = producto[4]
                                    cantidad_aux = dict['cantidad'] / int(producto[5])

                                    num = ''
                                    for char in peso_base:
                                        if char.isdigit() or char == '.':
                                            num += char

                                    if num != '':
                                        peso = float(num)
                                        peso_real = cantidad_aux * peso
                                        sumatoria_pesos += peso_real

                        lista_sumatorias.append([id_deposito ,sumatoria_pesos])

                    depos_ordenados = ps.bubble_sort(lista_sumatorias, lambda a: a[1], True)
                    for deposito in depos_ordenados:
                        print(f'Deposito {deposito[0]}: {deposito[1]:.2f}gr\n')



                case _:
                    print('¡ERROR! La opcion no es valida')
        
        input('Presione ENTER para continuar...')
        os.system('cls')

main()