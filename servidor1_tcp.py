import socket

# Configuración de conexión
IP_LOCAL = "127.0.0.1"  
PUERTO = 5005           
TOTAL_PAQUETES = 200    # Cantidad de paquetes a recibir 

# Crear socket TCP 
servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind: Asignar la IP y el puerto al socket
servidor.bind((IP_LOCAL, PUERTO))

# Espera del servidor que se conecten
servidor.listen(1)
print(f"[*] Servidor TCP esperando en {IP_LOCAL}:{PUERTO}...")

# Accept: Se completa el 'Three-way Handshake' (Sincronización inicial)
conexion, direccion = servidor.accept()
print(f"[+] Conexión establecida desde: {direccion}")

recibidos = 0
try:
    while recibidos < TOTAL_PAQUETES:
        # recv(1024): Leer los datos que llegan por el cable virtual
        datos = conexion.recv(1024)
        
        if not datos:
            break # Si no hay datos, el cliente cerró la conexión
            
        recibidos += 1
        # Decodificacion del mensaje (de bytes a texto) para imprimirlo
        print(f"Recibido: {datos.decode()} | Contador: {recibidos}")

    print("\n[!] PRUEBA FINALIZADA: Se recibieron los 200 paquetes correctamente.")

except Exception as e:
    print(f"[-] Error: {e}")

finally:
    # Cerrar sockets para liberar el puerto en el sistema
    conexion.close()
    servidor.close()
    print("[*] Conexión cerrada.")
