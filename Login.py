import mysql.connector
import getpass
import os
import time

bd = mysql.connector.connect(host="127.0.0.1", user="root", password="123456", database="SalasNetLabs")
cursor = bd.cursor()

def netseat():
    print(" _   _        _    _____               _   ")
    print("| \ | |      | |  /  ___|             | |  ")
    print("|  \| |  ___ | |_ \ `--.   ___   __ _ | |_ ")
    print("| . ` | / _ \| __| `--. \ / _ \ / _` || __|")
    print("| |\  ||  __/| |_ /\__/ /|  __/| (_| || |_ ")
    print("\_| \_/ \___| \__|\____/  \___| \__,_| \__|")
    print("")

ok = True
while(ok):
    os.system("clear")
    netseat()
    usuario = input("Ingrese su CI: ")
    contraseña = getpass.getpass("Ingrese su contraseña: ")
    cursor.execute("SELECT id_empleado, admin FROM empleados WHERE ci = '"+usuario+"' AND contraseña = '"+contraseña+"';")
    datos = cursor.fetchall()
    if (cursor.rowcount == 0):
        print("Usuario o contraseña incorrectos.")
        time.sleep(2)
    elif (datos[0][1] == 1): 
        ok = False
        os.system("python3 interfazAdmin.py")
    elif (datos[0][1] == 0):
        ok = False
        os.system("python3 interfazUsuario.py")