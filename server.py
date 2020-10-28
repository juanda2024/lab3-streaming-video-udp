#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 26 11:16:00 2020

@author: Juanda2420
"""

import socket
import sys
import time
import os

UDP_IP = "239.0.0.1"
UDP_PORT = 1234 
UDP_PORT2 = 1235
os.system("sudo ntpdate 0.es.pool.ntp.org")
rec = 0
def autoIncremenet():
    global rec
    pStart = 1
    pInterval = 1
    if(rec == 0):
        rec = pStart
    else:
        rec = rec + pInterval
    return str(rec).zfill(7)

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error:
    print("Fallo al conectar al socket del player")
    sys.exit()
    
print("Socket creado!!!!")

hostSource = ""
portSource = 8080
channelSource = ""

try:
    remote_ip = socket.gethostbyname(hostSource)
except socket.gaierror():
    print("No es posible conectarse al host")
    sys.exit()
    
s.connect((remote_ip, portSource))
sock2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock2.bind((UDP_IP, UDP_PORT2))
print("Socket conectado al reproductor VCL!!!!")
data, addr = sock2.recvfrom(1024)

message = "GET/" + channelSource + "HTTP/1.1\r\n\r\n"

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.sendall(message)

print("....Enviando datos por UDP a la dirección: " + UDP_IP)

while True:
    try:
        reply = s.recv(1024)
        sock.sendto(autoIncremenet() + "-----"+ str(time.time())+ "------"+reply, (UDP_IP, UDP_PORT))
    except socket.error:
        print("Mensaje no se ha podido enviar correctamente")
        sys.exit()
        

s.close()
sock.close()






















