import socket
import time
import random

HOST, PORT = "127.0.0.1", 9998
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

TAXA_PERDA = 0.2  # 20% de chance de "perda" simulada

for quadro in range(1, 21):
    if random.random() < TAXA_PERDA:
        print(f"[EMISSOR] Quadro {quadro} descartado (simulando perda de rede)")
        continue
    mensagem = f"QUADRO {quadro:02d}".encode()
    sock.sendto(mensagem, (HOST, PORT))
    print(f"[EMISSOR] Enviado: {mensagem.decode()}")
    time.sleep(0.1)