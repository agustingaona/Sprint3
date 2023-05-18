#!/usr/bin/python3
import os
import time
import colorama
import funciones

colorama.init()


func = True
separador = "*------------------------------*"
salasNetLabs = []
contraseña = "1234"



def opciones():
    os.system("clear")
    print(separador)
    print("1. Mostrar salas y capacidad. \n2. Ingresar a sala. \n3. Retirarse de sala. \n4. Agregar sala(admin). \n5. Eliminar sala(admin). \n6. Cambiar contraseña admin. \n7. Salir.")



while (func):
    opciones()
    opc = input("Ingrese una opción: ")
    print(separador)
    if (opc == '1'):
        funciones.mostrarSalas()
    elif (opc == '2'):
        funciones.ingresoASala()
        time.sleep(1)
    elif (opc == '3'):
        funciones.retiroDeSala()
        time.sleep(1)
    elif (opc == '4'):
        funciones.agregarSala()
        time.sleep(1)
    elif (opc == '5'):
        funciones.eliminarSala()
        time.sleep(1)
    elif (opc == '7'):
        func = False
        print("Saliendo")
        time.sleep(0.5)
    else:
        print("Opción incorrecta.")
