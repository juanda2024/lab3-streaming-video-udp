import socket
import os
import time
import numpy as np

os.system('sudo ntpdate 0.es.pool.ntp.org')
UDP_IP = '239.0.0.1'
UDP_PORT = 1234
UDP_PORT2 = 1235
print ("Preparado para recibir datos")
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock2 = socket.socket (socket.AF_INET, socket.SOCK_DGRAM)
socketPlayer = socket.socket (socket.AF_INET, socket.SOCK_DGRAM)
socket. socket (socket.AF_INET, socket.SOCK_STREAM)
sock.bind((UDP_IP, UDP_PORT))
socketPlayer.bind(('', 8081))
socketPlayer.listen(1)
print ('Esperando')
conn, addr = socketPlayer.accept()
print ('Conexion establecida con VLC')
sock2.sendto("hola", (UDP_IP, UDP_PORT2))

lista = [None] * 128
bandera = 0
total = 0
data, addr = sock.recvfrom(2048)
elementos = data.split("----")
conn.sendall(elementos[2])

while True:
    data, addr = sock.recvfrom(2048)
    elementos = data.split("----")
    hora = elementos[1]
    print(time. time() - float(hora))
    total+=1

    if bandera==1:
        conn.sendall(lista[total%128])

    lista[((elementos[0]))%128] = elementos[2]
    if total == 127:
        bandera = 1

sock.close()
