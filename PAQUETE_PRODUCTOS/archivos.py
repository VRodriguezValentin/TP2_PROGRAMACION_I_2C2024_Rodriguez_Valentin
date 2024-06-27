import csv
import json

def leer_txt(path, modo = 'r'):
    with open(path, modo) as archivo:
        leer = print(archivo.read())
    return leer

def escribir_txt(path, data, modo = 'w'):
    with open(path, modo) as archivo:
        escribir = archivo.write(data + '\n')
    return escribir

def leer_json(path, modo = 'r'):
    with open(path, modo, newline='\n') as file:
        leer = json.load(file)
    return leer

def escribir_json(path, data, modo = 'w'):
    with open(path, modo, newline='') as file:
        escribir = json.dump(data, file, indent=4)
    return escribir

def leer_csv(path, modo = 'r'):
    lista = []
    with open(path, modo) as archivo:
        leer = csv.reader(archivo, delimiter=',')
        for fila in leer:
            lista.append(fila)
    return lista

def escribir_csv(path, data, modo = 'w'):
    with open(path, modo, newline='') as archivo:
        escribir = csv.writer(archivo)
        escribir.writerow(data)
    return escribir

def escribir_csv_mas(path, data, modo = 'w'):
    with open(path, modo, newline='') as archivo:
        escribir = csv.writer(archivo)
        escribir.writerows(data)
    return escribir