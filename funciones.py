import colorama
import socket
import json


class Sala:
    def __init__(self, id, nombre, maxCap, ocup):
        self.id = id
        self.nombre = nombre
        self.capacidad = maxCap
        self.ocupados = ocup


def mostrarSalas(server):
    query_bytes = ("SELECT * FROM salas;").encode()
    server.sendall(query_bytes)
    data_str = server.recv(1024).decode()
    salas = json.loads(data_str)
    for sala in salas:
        percent = int(100 * sala[3] / sala[2])
        barra = ("║" + str('▓'*int(percent*0.15)) + str('░'*int(15-percent*0.15)) + "║")

        if (percent == 100):
            print("Sala ", sala[1],", capacidad: ", sala[3], "/", sala[2], " -", colorama.Fore.RED, barra, " ", percent, "%", colorama.Fore.RESET)
        elif (percent > 74):
            print("Sala ", sala[1],", capacidad: ", sala[3], "/", sala[2], " -", colorama.Fore.YELLOW, barra, " ", percent, "%", colorama.Fore.RESET)
        else:
            print("Sala ", sala[1],", capacidad: ", sala[3], "/", sala[2], " -", colorama.Fore.GREEN, barra, " ", percent, "%", colorama.Fore.RESET)
        
    input("Toque 'Enter' para volver.")


def ingresoASala(server, user):
    ok = True
    query_bytes = ("SELECT * FROM salas;").encode()
    server.sendall(query_bytes)
    data_str = server.recv(1024).decode()
    filas = json.loads(data_str)
    salasNetLabs = []
    for fila in filas:
        sala = Sala(fila[0], fila[1], fila[2], fila[3])
        salasNetLabs.append(sala)
    for sala in salasNetLabs:
        indice = salasNetLabs.index(sala) + 1
        print(str(indice) + ". " + sala.nombre + " - " + str(sala.ocupados) + "/" + str(sala.capacidad))
    while (ok):
        opc = input("Ingrese a que sala entrará (Ingrese 'x' para cancelar): ")
        if (opc <= str(salasNetLabs.__len__) and opc > '0'):
            for sala in salasNetLabs:
                if (opc == str(salasNetLabs.index(sala)+1)):
                    if (sala.ocupados < sala.capacidad):
                        sala.ocupados += 1
                        query_bytes = ("UPDATE salas SET ocupado = ocupado + 1 WHERE id_sala = "+ str(sala.id) +";").encode()
                        server.sendall(query_bytes)
                        print(colorama.Fore.LIGHTBLUE_EX, "Sala " + sala.nombre + " actualizada a " + str(sala.ocupados) + "/" + str(sala.capacidad), colorama.Fore.RESET)
                        query_bytes = ("UPDATE empleados SET id_sala = "+ str(sala.id) +" WHERE id_empleado = "+ str(user) +";").encode()
                        server.sendall(query_bytes)
                        ok = False
                    else:
                        print(colorama.Fore.YELLOW, "Sala llena, elija otra.", colorama.Fore.RESET)
        elif (opc == 'x'):
            print(colorama.Fore.BLUE, "Menú", colorama.Fore.RESET)
            ok = False
        else:
            print(colorama.Fore.RED, "No existe esa sala.", colorama.Fore.RESET)

def retiroDeSala(server, user):
    sala_id = None
    query_bytes = ("SELECT id_sala FROM empleados WHERE id_empleado = {};".format(user)).encode()
    server.sendall(query_bytes)
    dato_str = server.recv(1024).decode()
    dato = json.loads(dato_str)
    sala_id = dato[0][0]
    query_bytes = ("UPDATE salas SET ocupado = ocupado - 1 WHERE id_sala = " + str(sala_id) + ";").encode()
    server.sendall(query_bytes)
    query_bytes = ("UPDATE empleados SET id_sala = NULL WHERE id_empleado = " + str(user) + ";").encode()
    server.sendall(query_bytes)
    print("Retirado de la sala.")

def agregarSala(server):
    ok = True
    while (ok):
        nombreOk = False
        capOk = False
        ocupOk = False
        bien = False
        print("Si ingresa 'x' en cualquier campo se cancela la nueva sala.")
        while (not nombreOk):
            nombre = input("Ingrese nombre de la nueva sala: ")
            if (nombre.isspace() or nombre == ''):
                print(colorama.Fore.RED, "El nombre no puede ser vacío.", colorama.Fore.RESET)
            elif (nombre == 'x'):
                nombreOk = True
                capOk = True
                ocupOk = True
                ok = False
            else:
                nombreOk = True
        while (not capOk):
            capacidad = int(input("Ingrese la capacidad máxima de la sala: "))
            if (capacidad <= 0):
                print(colorama.Fore.RED, "La capacidad no puede ser menor a 1.", colorama.Fore.RESET)
            elif (nombre == 'x'):
                nombreOk = True
                capOk = True
                ocupOk = True
                ok = False
            else:
                capOk = True
        while(not ocupOk):
            ocupado = int(input("Ingrese la cantidad de lugares ya ocupados: "))
            if (ocupado > capacidad or ocupado < 0):
                print(colorama.Fore.RED, "No puede haber más lugares ocupados que la capacidad, y no puede haber ocupados negativos.", colorama.Fore.RESET)
            elif (nombre == 'x'):
                nombreOk = True
                capOk = True
                ocupOk = True
                ok = False
            else:
                ocupOk = True
                bien = True
        
        if (bien):
            query_bytes = ("INSERT INTO salas(nombre, capacidad, ocupado) VALUES ('"+ nombre +"', "+ str(capacidad) +", "+ str(ocupado) +");").encode()
            server.sendall(query_bytes)
            ok = False
            print(colorama.Fore.GREEN, "Sala agregada.", colorama.Fore.RESET)
        else:
            print("No se agregó ninguna sala.")

def eliminarSala(server):
    ok = True
    salasNetLabs = []
    query_bytes = ("SELECT * FROM salas;").encode()
    server.sendall(query_bytes)
    data = server.recv(1024).decode()
    filas = json.loads(data)
    for fila in filas:
        sala = Sala(fila[0], fila[1], fila[2], fila[3])
        salasNetLabs.append(sala)
    while (ok):
        for sala in salasNetLabs:
            indice = salasNetLabs.index(sala)+1
            print(indice, ". ", sala.nombre, ".")
        opc = input("Ingrese que sala eliminará (Ingrese 'x' para cancelar): ")
        if (opc > '0' and opc <= str(salasNetLabs.__len__)):
            confirma = input(("Confirme si quiere eliminar sala " + salasNetLabs[int(opc)-1].nombre + " ('si'): "))
            if(confirma == "si"):
                print("Sala ", salasNetLabs[int(opc)-1].nombre, " eliminada.")
                id = salasNetLabs[int(opc)-1].id
                query_bytes = ("DELETE FROM salas WHERE id_sala = "+ str(id) +";").encode()
                server.sendall(query_bytes)
                salasNetLabs.remove(salasNetLabs[int(opc)-1])
                ok = False
            else:
                print("No se eliminó.")
                ok = False
        elif (opc == 'x'):
            ok = False
            print(colorama.Fore.BLUE, "Menú", colorama.Fore.RESET)
        else:
            print(colorama.Fore.RED, "No existe esa sala.", colorama.Fore.RESET)