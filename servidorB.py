import socket
import os
import random
import time

IP_SERVIDOR = "192.168.56.1" 
PUERTO = 5006
ARCHIVO = "hamlet.txt"

def enviar_con_perdida(protocolo, porcentaje_perdida):
    paquetes_enviados_reales = 0
    paquetes_omitidos = 0
    
    print(f"--- Iniciando Cliente {protocolo} con {porcentaje_perdida}% de pérdida simulada ---")

    if protocolo == "TCP":
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((IP_SERVIDOR, PUERTO))
        with open(ARCHIVO, "rb") as f:
            while (chunk := f.read(1024)):
                # Simulación de pérdida
                if random.random() * 100 >= porcentaje_perdida:
                    sock.sendall(chunk)
                    paquetes_enviados_reales += 1
                else:
                    paquetes_omitidos += 1
        sock.close()
    else: # UDP
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        with open(ARCHIVO, "rb") as f:
            while (chunk := f.read(1024)):
                if random.random() * 100 >= porcentaje_perdida:
                    sock.sendto(chunk, (IP_SERVIDOR, PUERTO))
                    paquetes_enviados_reales += 1
                else:
                    paquetes_omitidos += 1
        sock.sendto(b"FIN", (IP_SERVIDOR, PUERTO))
        sock.close()
    
    print(f"Prueba finalizada.")
    print(f"Paquetes enviados a la red: {paquetes_enviados_reales}")
    print(f"Paquetes 'perdidos' por el código: {paquetes_omitidos}")

# 1. Cambia el protocolo ("TCP" o "UDP")
# 2. Cambia el porcentaje (10 o 30)
enviar_con_perdida("TCP", 10)
