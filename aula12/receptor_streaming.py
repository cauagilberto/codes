import socket

HOST, PORT = "0.0.0.0", 9998
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((HOST, PORT))
sock.settimeout(2)

recebidos = []
try:
    while True:
        dados, _ = sock.recvfrom(1024)
        recebidos.append(dados.decode())
        print(f"[RECEPTOR] Chegou: {dados.decode()}")
except socket.timeout:
    print("\nFim da transmissao (sem novos quadros por 2s).")
    print(f"Total de quadros recebidos: {len(recebidos)} de 20 enviados na origem.")