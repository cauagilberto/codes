import socket
import sys

HOST, PORT = "127.0.0.1", 9999

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.settimeout(3)

mensagem = sys.argv[1] if len(sys.argv) > 1 else "Ola, servidor!"
sock.sendto(mensagem.encode(), (HOST, PORT))
print("Mensagem enviada. Nenhum handshake foi realizado antes deste envio.")

try:
    resposta, _ = sock.recvfrom(2048)
    print(f"Resposta recebida: {resposta.decode()}")
except socket.timeout:
    print("Timeout: nenhuma resposta recebida (o UDP nao teria como avisar).")