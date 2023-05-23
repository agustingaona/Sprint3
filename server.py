import socket
import threading
import mysql.connector
import json

func = True
base = mysql.connector.connect(host="127.0.0.1", user="root", password="123456", database="SalasNetLabs")
cursor = base.cursor()
base.autocommit = True

def client(socket, address):
    print("Se conectó: {}".format(address))

    while (True):
        data = socket.recv(1024)
        if not data:
            break

        query = data.decode()
        cursor.execute(query)
        datos = cursor.fetchall()
        if (len(datos) > 0):
            json_datos = json.dumps(datos)
            json_bytes = json_datos.encode()
            socket.sendall(json_bytes)
        else:
            print("Query sin devolución.")


def start_server():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    host = '192.168.1.10'
    port = 8404

    s.bind((host, port))

    s.listen(60)
  
    while (True):
        clientSocket, clientAddress = s.accept()
        client_thread = threading.Thread(target= client, args= (clientSocket, clientAddress))
        client_thread.start()

start_server()