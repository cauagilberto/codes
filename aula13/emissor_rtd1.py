
import socket, time

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
destino = ('127.0.0.1', 6001)

for i in range(5):
    msg = f"pacote {i}".encode()
    sock.sendto(msg, destino)
    print(f"[Emissor] enviado: {msg!r}")
    time.sleep(0.5)