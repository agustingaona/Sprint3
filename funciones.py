import getpass
import os
import colorama
import mysql.connector


class Sala:
    def __init__(self, id, nombre, maxCap, ocup):
        self.id = id
        self.nombre = nombre
        self.capacidad = maxCap
        self.ocupados = ocup

base = mysql.connector.connect(host="127.0.0.1", user="root", password="123456", database="SalasNetLabs")
cursor = base.cursor()
base.autocommit = True


def mostrarSalas():
    cursor.execute("SELECT * FROM salas;")
    salas = cursor.fetchall()
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


def ingresoASala():
    ok = True
    salasNetLabs = []
    cursor.execute("SELECT * FROM salas;")
    filas = cursor.fetchall()
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
                        cursor.execute("UPDATE salas SET ocupado = ocupado + 1 WHERE id_sala = "+ str(sala.id) +";")
                        print(colorama.Fore.LIGHTBLUE_EX, "Sala " + sala.nombre + " actualizada a " + str(sala.ocupados) + "/" + str(sala.capacidad), colorama.Fore.RESET)
                        ok = False
                    else:
                        print(colorama.Fore.YELLOW, "Sala llena, elija otra.", colorama.Fore.RESET)
        elif (opc == 'x'):
            print(colorama.Fore.BLUE, "Menú", colorama.Fore.RESET)
            ok = False
        else:
            print(colorama.Fore.RED, "No existe esa sala.", colorama.Fore.RESET)

def retiroDeSala():
    ok = True
    salasNetLabs = []
    cursor.execute("SELECT * FROM salas;")
    filas = cursor.fetchall()
    for fila in filas:
        sala = Sala(fila[0], fila[1], fila[2], fila[3])
        salasNetLabs.append(sala)
    for sala in salasNetLabs:
        indice = str(salasNetLabs.index(sala) + 1)
        print(indice + ". " + sala.nombre + " - " + str(sala.ocupados) + "/" + str(sala.capacidad))
    while (ok):
        opc = input("Ingrese que sala dejará (Ingrese 'x' para cancelar): ")
        if (opc <= str(salasNetLabs.__len__()) and opc > '0'):
            for sala in salasNetLabs:
                if (opc == str(salasNetLabs.index(sala)+1)):
                    if (sala.ocupados > 0):
                        sala.ocupados -= 1
                        cursor.execute("UPDATE salas SET ocupado = ocupado - 1  WHERE id_sala = " + str(sala.id) +";")
                        print(colorama.Fore.LIGHTBLUE_EX, "Sala " + sala.nombre + " actualizada a " + str(sala.ocupados) + "/" + str(sala.capacidad), colorama.Fore.RESET)
                        ok = False
                    else:
                        print(colorama.Fore.YELLOW, "Sala vacía, no hay nadie que pueda salir.", colorama.Fore.RESET)
        elif (opc == 'x'):
            print(colorama.Fore.BLUE, "Menú", colorama.Fore.RESET)
            ok = False
        else:
            print(colorama.Fore.RED, "No existe esa sala.", colorama.Fore.RESET)

def agregarSala():
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
            cursor.execute("INSERT INTO salas(nombre, capacidad, ocupado) VALUES ('"+ nombre +"', "+ str(capacidad) +", "+ str(ocupado) +");")
            ok = False
            print(colorama.Fore.GREEN, "Sala agregada.", colorama.Fore.RESET)
        else:
            print("No se agregó ninguna sala.")

def eliminarSala():
    ok = True
    salasNetLabs = []
    cursor.execute("SELECT * FROM salas;")
    filas = cursor.fetchall()
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
                cursor.execute("DELETE FROM salas WHERE id_sala = "+ str(id) +";")
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