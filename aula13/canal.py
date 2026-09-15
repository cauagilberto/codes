# Simula um canal com corrupção e perda configuráveis entre emissor (porta 6000)
# e receptor (porta 6001). Repassa também os ACKs no sentido inverso.
import socket, random, sys

P_CORROMPER_DADOS = 0.3   # probabilidade de corromper um pacote de dados
P_PERDER_DADOS    = 0.0   # usada na Atividade 2
P_CORROMPER_ACK   = 0.0
P_PERDER_ACK      = 0.0

EMISSOR_ADDR = None
RECEPTOR = ('127.0.0.1', 6001)

canal_in = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)   # recebe do emissor
canal_in.bind(('127.0.0.1', 6000))
canal_out = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # recebe do receptor (ACKs)
canal_out.bind(('127.0.0.1', 6002))

canal_in.settimeout(0.2)
canal_out.settimeout(0.2)

print("[Canal] repassando 6000(emissor)->6001(receptor) e 6002(receptor)->emissor")
print(f"[Canal] P_CORROMPER_DADOS={P_CORROMPER_DADOS} P_PERDER_DADOS={P_PERDER_DADOS} "
      f"P_CORROMPER_ACK={P_CORROMPER_ACK} P_PERDER_ACK={P_PERDER_ACK}")

while True:
    try:
        data, addr = canal_in.recvfrom(2048)
        EMISSOR_ADDR = addr
        if random.random() < P_PERDER_DADOS:
            print("[Canal] >>> pacote de DADOS PERDIDO")
            continue
        if random.random() < P_CORROMPER_DADOS and len(data) > 3:
            data = bytearray(data)
            data[3] ^= 0xFF
            data = bytes(data)
            print("[Canal] >>> pacote de DADOS CORROMPIDO")
        canal_in.sendto(data, RECEPTOR)
    except socket.timeout:
        pass
    try:
        ack, addr2 = canal_out.recvfrom(2048)
        if random.random() < P_PERDER_ACK:
            print("[Canal] <<< ACK PERDIDO")
            continue
        if random.random() < P_CORROMPER_ACK and len(ack) > 3:
            ack = bytearray(ack)
            ack[3] ^= 0xFF
            ack = bytes(ack)
            print("[Canal] <<< ACK CORROMPIDO")
        if EMISSOR_ADDR:
            canal_out.sendto(ack, EMISSOR_ADDR)
    except socket.timeout:
        pass