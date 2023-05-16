#!/usr/bin/python3
import os
import time
import getpass
import colorama

colorama.init()

func = True
separador = "*------------------------------*"
salasNetLabs = []
contraseña = "1234"


class salas:

    def __init__(self, nombre, maxCap, ocup):
        self.nombre = nombre
        self.capacidad = maxCap
        self.ocupados = ocup

def actualizarTxt():
    with open('/home/user/Desktop/Sprint1/Proyecto1/Salas.txt', 'w') as Archivo:
        for sala in salasNetLabs:
            Archivo.write((sala.nombre + "-" + str(sala.capacidad) + "-" + str(sala.ocupados) + '\n'))

with open('/home/user/Desktop/Sprint1/Proyecto1/Salas.txt', 'r') as Archivo:
    salasTxt = Archivo.read()

lineas = salasTxt.rstrip('\n').split('\n')
for linea in lineas:
    aux = linea.split('-')
    sala = salas(aux[0],int(aux[1]),int(aux[2]))
    salasNetLabs.append(sala)


def opciones():
    os.system("clear")
    print(separador)
    print("1. Mostrar salas y capacidad. \n2. Ingresar a sala. \n3. Retirarse de sala. \n4. Agregar sala(admin). \n5. Eliminar sala(admin). \n6. Cambiar contraseña admin. \n7. Salir.")


def mostrarSalas():
    for sala in salasNetLabs:
        percent = int(100 * sala.ocupados / sala.capacidad)
        barra = ("║" + str('▓'*int(percent*0.15)) + str('░'*int(15-percent*0.15)) + "║")

        if (percent == 100):
            print("Sala ", sala.nombre,", capacidad: ", sala.ocupados, "/", sala.capacidad, " -", colorama.Fore.RED, barra, " ", percent, "%", colorama.Fore.RESET)
        elif (percent > 74):
            print("Sala ", sala.nombre,", capacidad: ", sala.ocupados, "/", sala.capacidad, " -", colorama.Fore.YELLOW, barra, " ", percent, "%", colorama.Fore.RESET)
        else:
            print("Sala ", sala.nombre,", capacidad: ", sala.ocupados, "/", sala.capacidad, " -", colorama.Fore.GREEN, barra, " ", percent, "%", colorama.Fore.RESET)
        
    input("Toque 'Enter' para volver.")


def ingresoASala():
    ok = True
    for sala in salasNetLabs:
        indice = str(salasNetLabs.index(sala) + 1)
        print(indice + ". " + sala.nombre + " - " + str(sala.ocupados) + "/" + str(sala.capacidad))
    while (ok):
        opc = input("Ingrese a que sala entrará (Ingrese 'x' para cancelar): ")
        if (opc <= str(salasNetLabs.__len__()) and opc > '0'):
            for sala in salasNetLabs:
                if (opc == str(salasNetLabs.index(sala)+1)):
                    if (sala.ocupados < sala.capacidad):
                        sala.ocupados += 1
                        actualizarTxt()
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
                        actualizarTxt()
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
    contraOk = True
    ok = False
    while (contraOk):
        psw = getpass.getpass(prompt="Contraseña (Ingrese 'x' para salir): ")
        os.system("clear")
        opciones()
        if (psw == contraseña):
            contraOk = False
            ok = True
        elif (psw == 'x'):
            print(colorama.Fore.BLUE, "Menú", colorama.Fore.RESET)
            contraOk = False
        else:
            print(colorama.Fore.RED, "Contraseña incorrecta.", colorama.Fore.RESET)
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
            sala = salas(nombre, capacidad, ocupado)
            salasNetLabs.append(sala)
            actualizarTxt()
            ok = False
            print(colorama.Fore.GREEN, "Sala agregada.", colorama.Fore.RESET)
        else:
            print("No se agregó ninguna sala.")

def eliminarSala():
    contraOk = True
    ok = False
    while (contraOk):
        psw = getpass.getpass(prompt="Contraseña (Ingrese 'x' para salir): ")
        os.system("clear")
        opciones()
        print(separador)
        if (psw == contraseña):
            contraOk = False
            ok = True
        elif (psw == 'x'):
            print(colorama.Fore.BLUE, "Menú", colorama.Fore.RESET)
            contraOk = False
        else:
            print(colorama.Fore.RED, "Contraseña incorrecta.", colorama.Fore.RESET)
    while (ok):
        for sala in salasNetLabs:
            indice = salasNetLabs.index(sala)+1
#            print = salasNetLabs.index(sala)
            print(indice, ". ", sala.nombre, ".")
        opc = input("Ingrese que sala eliminará (Ingrese 'x' para cancelar): ")
        if (opc > '0' and opc < str(salasNetLabs.__len__())):
            confirma = input(("Confirme si quiere eliminar sala " + salasNetLabs[int(opc)-1].nombre + " ('si'): "))
            if(confirma == "si"):
                print("Sala ", salasNetLabs[int(opc)-1].nombre, " eliminada.")
                salasNetLabs.remove(salasNetLabs[int(opc)-1])
                actualizarTxt()
                ok = False
            else:
                print("No se eliminó.")
                ok = False
        elif (opc == 'x'):
            ok = False
            print(colorama.Fore.BLUE, "Menú", colorama.Fore.RESET)
        else:
            print(colorama.Fore.RED, "No existe esa sala.", colorama.Fore.RESET)
        
def cambiarPSW():
    global contraseña
    ok = True
    while (ok):
        actPsw = getpass.getpass(prompt="Ingrese la contraseña actual (Ingrese 'x' para cancelar): ")
        if (actPsw == contraseña):
            ok2 = True
            while (ok2):
                newPsw = getpass.getpass(prompt="Ingrese nueva contraseña: ")
                if (newPsw.isspace() or newPsw == ''):
                    print(colorama.Fore.RED, "La contraseña no puede ser vacía.", colorama.Fore.RESET)
                else:
                    contraseña = newPsw
                    ok2 = False
                    ok = False
                    print(colorama.Fore.GREEN, "Contraseña actualizada.", colorama.Fore.RESET)
        elif (actPsw == 'x'):
            ok = False
            print("Menu")   
        else:
            print(colorama.Fore.RED, "Contraseña incorrecta.", colorama.Fore.RESET)




while (func):
    opciones()
    opc = input("Ingrese una opción: ")
    print(separador)
    if (opc == '1'):
        mostrarSalas()
    elif (opc == '2'):
        ingresoASala()
        time.sleep(1)
    elif (opc == '3'):
        retiroDeSala()
        time.sleep(1)
    elif (opc == '4'):
        agregarSala()
        time.sleep(1)
    elif (opc == '5'):
        eliminarSala()
        time.sleep(1)
    elif (opc == '6'):
        cambiarPSW()
        time.sleep(1)
    elif (opc == '7'):
        func = False
        print("Saliendo")
        time.sleep(0.5)
    else:
        print("Opción incorrecta.")
