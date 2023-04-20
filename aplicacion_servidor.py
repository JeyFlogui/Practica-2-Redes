# Prueba practica 2

import sys
import socket
import selectors
import types

HOST = "localhost"  # El hostname o IP del servidor
PORT = 53040  # El puerto que usa el servidor
bufferSize = 1024
sel = selectors.DefaultSelector()

def read_write(Socket, mask):
    if mask & selectors.EVENT_READ:
        data, addr = Socket.recvfrom(1024)  # Should be ready
        if data:
            print("recibido", repr(data), 'a', Socket)
            with open(f"audioget{addr}.mp3", "ab") as archivo:
                archivo.write(data)
        else:
            print("cerrando", Socket)
            sel.unregister(Socket)
            Socket.close()

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as Socket:
    Socket.bind((HOST, PORT))
    Socket.setblocking(False)
    sel.register(Socket, selectors.EVENT_READ, read_write)

    while True:
        print("Esperando evento...")
        events = sel.select()
        for key, mask in events:
            callback = key.data
            callback(key.fileobj, mask)
