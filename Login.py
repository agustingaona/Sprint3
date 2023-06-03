import getpass
import os
import time
import socket
import json


def netseat():
    print(" _   _        _    _____               _   ")
    print("| \ | |      | |  /  ___|             | |  ")
    print("|  \| |  ___ | |_ \ `--.   ___   __ _ | |_ ")
    print("| . ` | / _ \| __| `--. \ / _ \ / _` || __|")
    print("| |\  ||  __/| |_ /\__/ /|  __/| (_| || |_ ")
    print("\_| \_/ \___| \__|\____/  \___| \__,_| \__|")
    print("")

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '192.168.100.119'
port = 8404

ok = True
while(ok):
    os.system("clear")
    netseat()
    usuario = input("Ingrese su CI: ")
    contraseña = getpass.getpass("Ingrese su contraseña: ")
    query = {
        "tipo": "query",
        "data": "SELECT id_empleado, admin FROM empleados WHERE ci = '"+usuario+"' AND contraseña = '"+contraseña+"';"
    }
    query_json = json.dumps(query)
    query_bytes = query_json.encode()
    server.connect((host, port))
    server.sendall(query_bytes)
    data_str = server.recv(1024).decode()
    datos = [[]]
    datos = json.loads(data_str)
    if (datos.__len__() < 1):
        print("Usuario o contraseña incorrectos.")
        time.sleep(2)
    elif (datos[0][1] == 1): 
        ok = False
        os.system(f"python3 interfazAdmin.py {datos[0][0]}")
    elif (datos[0][1] == 0):
        ok = False
        os.system(f"python3 interfazUsuario.py {datos[0][0]}")