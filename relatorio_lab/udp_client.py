import socket, sys

porta_origem = int(sys.argv[1])
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('127.0.0.1', porta_origem))
sock.sendto(b"Mensagem de teste", ('127.0.0.1', 9999))