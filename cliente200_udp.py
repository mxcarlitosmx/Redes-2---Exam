import socket
import time

# Configuracion
IP_LINUX = "192.168.1.88" 
PUERTO = 5006
N_TOTAL = 100 

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print(f"[*] Iniciando envio de {N_TOTAL} datagramas...")

for i in range(1, N_TOTAL + 1):
    # Construccion del datagrama con encabezado
    contenido = f"Dato_{i}"
    fin = 1 if i == N_TOTAL else 0
    # Formato: SEQ:i | SIZE:bytes | FIN:0/1
    encabezado = f"SEQ:{i}|SIZE:{len(contenido)}|FIN:{fin}"
    
    sock.sendto(encabezado.encode(), (IP_LINUX, PUERTO))
    time.sleep(0.01) # Pausa para no saturar y permitir que 'tc' actue

print("[*] Envio finalizado.")
sock.close()
