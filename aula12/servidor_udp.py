import socket
from datetime import datetime

HOST, PORT = "0.0.0.0", 9999

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((HOST, PORT))
print(f"Servidor UDP escutando em {HOST}:{PORT}")

while True:
    dados, endereco = sock.recvfrom(2048)
    agora = datetime.now().strftime("%H:%M:%S.%f")
    print(f"[{agora}] Recebido de {endereco}: {dados.decode()}")
    resposta = f"ACK da aplicacao: '{dados.decode()}' recebido".encode()
    sock.sendto(resposta, endereco)