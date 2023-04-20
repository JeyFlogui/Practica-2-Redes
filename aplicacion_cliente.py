import socket

HOST = "localhost"  # El hostname o IP del servidor
PORT = 53040  # El puerto usado por el servidor
serverAddressPort = ("localhost", 13040)
bufferSize = 1024

# Crea un socket UDP del lado del cliente

with socket.socket(socket.AF_INET,socket.SOCK_DGRAM) as UDPClientSocket:
    with open("SmokeSprite.mp3", "rb") as archivo:
        while True:
            size = archivo.read(bufferSize)
            if not size:
                break
            UDPClientSocket.sendto(size, (HOST, PORT))
        print("Termine la transaccion")

