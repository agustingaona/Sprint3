import os
import time
import colorama
import funciones
import socket
import json
import sys

colorama.init()

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '192.168.1.10'
port = 8404
server.connect((host, port))
server.settimeout(0.25)

func = True
separador = "*------------------------------*"
usuario = sys.argv[1]
query_bytes = ("SELECT nombre FROM empleados WHERE id_empleado = {}".format(usuario)).encode()
server.sendall(query_bytes)
datos_str = server.recv(1024).decode()
datos = json.loads(datos_str)
nombre_usuario = datos[0][0]
salaActual = None
nombre_sala = None





def opcionesEnSala():
    os.system("clear")
    print(separador)
    print("Hola {}, sala actual {}".format(nombre_usuario, nombre_sala) )
    print("1. Mostrar salas y capacidad. \n2. Retirarse de sala. \n3. Salir.")


def opcionesSinSala():
    os.system("clear")
    print(separador)
    print("Hola {}, no estás en ninguna sala.".format(nombre_usuario) )
    print("1. Mostrar salas y capacidad. \n2. Ingresar a sala. \n3. Salir.")



while (func):
    enSala = False
    query = ("SELECT s.id_sala, s.nombre FROM empleados e INNER JOIN salas s ON e.id_sala = s.id_sala WHERE id_empleado = {}".format(usuario)).encode()
    server.sendall(query)
    try:
        datos_str = server.recv(1024).decode()
        datos = json.loads(datos_str)
        salaActual = datos[0][0]
        nombre_sala = datos[0][1]
        enSala = True
    except socket.timeout:
        enSala = False

    if (enSala):
        opcionesEnSala()
        opc = input("Ingrese una opción: ")
        print(separador)
        if (opc == '1'):
            funciones.mostrarSalas(server)
        elif (opc == '2'):
            funciones.retiroDeSala(server, usuario)
            time.sleep(1)
        elif (opc == '3'):
            func = False
            server.close()
            print("Saliendo")
            time.sleep(0.5)
        else:
            print("Opción incorrecta.")
    else:
        opcionesSinSala()
        opc = input("Ingrese una opción: ")
        print(separador)
        if (opc == '1'):
            funciones.mostrarSalas(server)
        elif (opc == '2'):
            funciones.ingresoASala(server, usuario)
            time.sleep(1)
        elif (opc == '3'):
            func = False
            server.close()
            print("Saliendo")
            time.sleep(0.5)
        else:
            print("Opción incorrecta.")
