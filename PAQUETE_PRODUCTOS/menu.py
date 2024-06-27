def menu(titulo: str, opciones: list, opcion_salir: str = 'SALIR'):
    '''
    Interfaz de menú con opciones indefinidas
    :titulo: Titulo del menu
    :opciones: Lista de opciones del menu
    :opcion_salir: Salir
    '''
    print(  '╔══════════════════════════════════════════════════╗\n'
            f'                   {titulo}                    \n'
            '╚══════════════════════════════════════════════════╝')

    i = 1
    for opcion in opciones:
        print(f' [{i}] {opcion}')
        i += 1
    
    print(  '╔══════════════════════════════════════════════════╗\n'
            f' [0] {opcion_salir}                            \n'
            '╚══════════════════════════════════════════════════╝')

    opcion = input('[Opcion]: ')
    return opcion

#opciones = ['Opción A', 'Opción B', 'Opción C', 'Opción D','Opción E','Opción E','Opción E','Opción E','Opción E','Opción E','Opción E','Opción E','Opción E','Opción E','Opción E','Opción E','Opción E','Opción E','Opción E']
#opcion = menu('Menu Principal', opciones)