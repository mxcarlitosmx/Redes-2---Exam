import socket
import os

IP_SERVIDOR = "TU_IP_DE_WINDOWS" # <--- CAMBIA ESTO
PUERTO = 5006
ARCHIVO = "hamlet.txt"

def enviar_archivo(protocolo):
    paquetes_enviados = 0
    
    if protocolo == "TCP":
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((IP_SERVIDOR, PUERTO))
        with open(ARCHIVO, "rb") as f:
            while (chunk := f.read(1024)):
                sock.sendall(chunk)
                paquetes_enviados += 1
        sock.close()
    else: # UDP
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        with open(ARCHIVO, "rb") as f:
            while (chunk := f.read(1024)):
                sock.sendto(chunk, (IP_SERVIDOR, PUERTO))
                paquetes_enviados += 1
        sock.sendto(b"FIN", (IP_SERVIDOR, PUERTO))
        sock.close()
    
    print(f"\n--- CLIENTE {protocolo} ---")
    print(f"Paquetes enviados: {paquetes_enviados}")
    print(f"Archivo: {ARCHIVO}")
    print("----------------------------")

# Cambiar a "UDP" cuando vayas a probar UDP
enviar_archivo("TCP")
