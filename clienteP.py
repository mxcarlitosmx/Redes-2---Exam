import socket
import time
import os

IP_SERVIDOR = "TU_IP_WINDOWS" # <--- Pon la IP de tu Windows aquí
PUERTO = 5006
ARCHIVO = "hamlet.txt"

def enviar_archivo(protocolo):
    tamano_original = os.path.getsize(ARCHIVO)
    print(f"Enviando {ARCHIVO} ({tamano_original} bytes) vía {protocolo}...")

    if protocolo == "TCP":
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((IP_SERVIDOR, PUERTO))
        with open(ARCHIVO, "rb") as f:
            while (chunk := f.read(1024)):
                sock.sendall(chunk)
        sock.close()
    else: # UDP
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        with open(ARCHIVO, "rb") as f:
            while (chunk := f.read(1024)):
                sock.sendto(chunk, (IP_SERVIDOR, PUERTO))
        sock.sendto(b"FIN", (IP_SERVIDOR, PUERTO))
    
    print("Envío finalizado.")

# CAMBIA ESTO SEGÚN LA PRUEBA:
enviar_archivo("TCP")
# enviar_archivo("UDP")
