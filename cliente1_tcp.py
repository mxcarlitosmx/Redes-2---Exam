import socket
import time

# Configuración del destino
IP_DESTINO = "127.0.0.1"
PUERTO_DESTINO = 5005
CANTIDAD = 200

# Crear el socket TCP
cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    # Conectar al servidor (Establece el canal de comunicación)
    cliente.connect((IP_DESTINO, PUERTO_DESTINO))
    print("[*] Conectado. Iniciando envio de paquetes...")

    # Guardar el tiempo de inicio exacto
    tiempo_inicio = time.time()

    for i in range(1, CANTIDAD + 1):
        mensaje = f"Mensaje numero {i}"

        #Si se aplica el "tc lost" TCP detectara que el paquete se perdio y lo volvera a enviar automaticamente y el tiempo final sera mayor.
        cliente.send(mensaje.encode())
        
        # Pausa de 0.01s para que la simulacion de perdida sea efectiva
        time.sleep(0.01)

    # Guardar el tiempo de fin
    tiempo_fin = time.time()
    
    # Calculo del tiempo total transcurrido
    duracion = tiempo_fin - tiempo_inicio

    print("\n" + "="*40)
    print(f"RESULTADO DE LA PRUEBA TCP")
    print(f"Tiempo total: {duracion:.4f} segundos")
    print(f"Paquetes enviados: {CANTIDAD}")
    print("="*40)

except ConnectionRefusedError:
    print("[!] ERROR: No se encontro el servidor. ¿Lo encendiste primero?")
finally:
    # Cerrar el socket
    cliente.close()
