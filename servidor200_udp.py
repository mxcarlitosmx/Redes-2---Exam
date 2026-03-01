import socket

# Configuracion
IP = "0.0.0.0"
PUERTO = 9999
N_TOTAL = 100

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((IP, PUERTO))

# Aumentar tiempo de espera para que capte todo
sock.settimeout(10.0) 

print(f"[*] Servidor UDP esperando {N_TOTAL} paquetes...")
print("[!] El calculo se hara automaticamente 10 segundos despues del ultimo paquete.")

recibidos_unicos = set()

try:
    while True:
        data, addr = sock.recvfrom(1024)
        mensaje = data.decode()
        
        # Extraemos la informacion del encabezado
        partes = mensaje.split('|')
        seq = int(partes[0].split(':')[1])
        
        recibidos_unicos.add(seq)
        print(f"Recibido paquete #{seq}")
    
except socket.timeout:
    print("\n[!] Tiempo agotado de espera. Calculando metricas finales...")

# METRICAS DE LA PRACTICA
n_recibidos = len(recibidos_unicos)
n_faltantes = [i for i in range(1, N_TOTAL + 1) if i not in recibidos_unicos]
porcentaje_perdida = ((N_TOTAL - n_recibidos) / N_TOTAL) * 100

print("\n" + "═"*40)
print(f"    RESULTADOS DEL CONTROL ESTADISTICO")
print("═"*40)
print(f"1. Paquetes esperados (N_total): {N_TOTAL}")
print(f"2. Paquetes recibidos (N_unicos): {n_recibidos}")
print(f"3. Numeros de secuencia faltantes: {n_faltantes if len(n_faltantes) < 15 else 'Multiples'}")
print(f"4. PORCENTAJE DE PERDIDA: {porcentaje_perdida:.2f}%")
print("═"*40)

sock.close()
