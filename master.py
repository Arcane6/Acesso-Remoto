import time
import socket
import sys
import os

s = socket.socket()
host = socket.gethostname()
port = 8080
s.bind(('',port))

s.listen()
conn, addr = s.accept()
print(addr, "Conectado! ")

command = input(str("Entre com o comando: "))
conn.send(command.encode())
print("Comando enviado com sucesso.")
data = conn.recv(1024)

if data:
    print("Comando recebido e executado com sucesso.")