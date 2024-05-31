import datetime

asiento = [["L"] * 10 for _ in range(10)]
base = {}
usuario = {}


def mapa(asiento):
    print('Asientos disponibles')
    print('  1 2 3 4 5 6 7 8 9 10', end='')
    for x in range(10):
        print('\n', x, sep='', end=' ')
        for y in range(10):
            print(asiento[y][x], sep='', end=' ')
    print('\n')


def reserva(asiento, base, usuario):
    print('Elija un asiento')
    logic = True
    while logic:
        try:
            x = int(input('Numero de fila: '))
            y = int(input('Numero de asiento: '))
            if x and y in range(1, 10):
                if asiento[y - 1][x - 1] == 'L':
                    asiento[y - 1][x - 1] = 'X'
                    id = sum(item.count('X') for item in asiento)
                    clave = f'ticket_{id}'
                    nombre = input('Nombre cliente: ')
                    apellido = input('Apellido cliente: ')
                    tarjeta = input('Tarjeta cliente: ')
                    usuario[id] = {'nombre': nombre, 'apellido': apellido, 'tarjeta': tarjeta}
                    base[clave] = {'fila': x, 'asiento': y, 'compra': int(datetime.datetime.now().timestamp()),
                                   'evento': int(datetime.date(2024, 11, 23).strftime('%Y%m%d')),
                                   'precio': 10, 'cliente': usuario[id]}
                    print('Asiento', y, 'en fila', x, 'registrado correctamente.', sep=' ')
                    logic = False
                elif asiento[y - 1][x - 1] == 'X':
                    raise Exception('Asiento no disponible')
            else:
                raise Exception('Asientos no existen')
            return asiento, base, usuario

        except ValueError:
            print('Dato incorrecto. Intente nuevamente.')



def admin(base):
    if base:
        total = 0
        filax = int(input('Ingrese una fila para ver tickets: '))
        keys = []
        for clave, valor in base.items():
            if 'precio' in valor:
                total += valor['precio']

            if filax == valor['fila']:
                keys.append(clave)
        print('Ganancia total $', total, sep='')
        print('Tickets en fila', filax, keys)
        print('Registro\n', base, end='\n')

    else:
        print('No hay información')


main = True
while main:
    try:
        print('Sistema de Reserva de Asientos\n1-Mapa de asientos\n2-Adquirir un asiento\n3-Administración\n4-Salir')
        op = int(input('Opción a elegir: '))
        if op == 1:
            mapa(asiento)
        elif op == 2:
            reserva(asiento, base, usuario)
        elif op == 3:
            admin(base)
        elif op == 4:
            main = False
    except:
        'Opción no válida'
