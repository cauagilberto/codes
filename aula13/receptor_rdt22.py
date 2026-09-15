import socket
from common import parse_pkt, make_pkt

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('127.0.0.1', 6001))
ack_dest = ('127.0.0.1', 6002)

esperado = 0  # próximo número de sequência esperado (0 ou 1)
print("[Receptor rdt2.2] aguardando pacotes...")

while True:
    pkt, addr = sock.recvfrom(2048)
    integro, seq, dados = parse_pkt(pkt)

    if not integro:
        print("[Receptor] pacote corrompido detectado! Reenviando ACK do último OK.")
        # TODO 1: envie um ACK para o número de sequência ANTERIOR (esperado XOR 1)
        # dica: sock.sendto(make_pkt(<seq_do_ack>, b'ACK'), ack_dest)
        seq_anterior = 1 - esperado
        sock.sendto(make_pkt(seq_anterior, b""), ack_dest)
        #sendto envia bytes brutos do pacote diretamente para o destino
        continue

    if seq == esperado:
        print(f"[Receptor] pacote {seq} OK: {dados.decode(errors='replace')!r}")
        # TODO 2: envie ACK confirmando este seq
        sock.sendto(make_pkt(seq, b""), ack_dest)
        # TODO 3: alterne o valor de 'esperado' (0 -> 1 ou 1 -> 0)
        esperado = 1 - esperado
    else:
        print(f"[Receptor] pacote duplicado (seq={seq}), descartando dado mas reenviando ACK")
        # TODO 4: reenvie o ACK do seq recebido (mesmo sendo duplicado),
        sock.sendto(make_pkt(seq, b""), ack_dest)
        # pois o emissor não recebeu o ACK anterior