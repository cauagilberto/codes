import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('127.0.0.1', 6001))
print("[Receptor rdt1.0] aguardando em 127.0.0.1:6001 ...")

while True:
    data, addr = sock.recvfrom(2048)
    print(f"[Receptor] recebido: {data.decode()!r} de {addr}")