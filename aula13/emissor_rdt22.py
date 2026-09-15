
import socket, time
from common import make_pkt, parse_pkt

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('127.0.0.1', 6003))
sock.settimeout(2.0)
canal_addr = ('127.0.0.1', 6000)

mensagens = ["Ola", "Mundo", "Redes", "de", "Computadores"]
seq = 0

for msg in mensagens:
    confirmado = False
    tentativas = 0
    while not confirmado:
        tentativas += 1
        pkt = make_pkt(seq, msg.encode())
        sock.sendto(pkt, canal_addr)
        print(f"[Emissor] enviando seq={seq} tentativa={tentativas}: {msg!r}")
        try:
            resposta, _ = sock.recvfrom(2048)
            integro, ack_seq, _ = parse_pkt(resposta)
            # TODO 5: só considere 'confirmado = True' se o ACK for íntegro
            # E o ack_seq for igual ao 'seq' atual (senão, é ACK duplicado/errado -> reenviar)
            if integro and ack_seq == seq:
                confirmado = True
            else:
                confirmado = False
        except socket.timeout:
            print("[Emissor] timeout aguardando ACK, reenviando...")
    # TODO 6: alterne o valor de 'seq' (0 -> 1 ou 1 -> 0) antes de ir para a próxima mensagem
    seq = 1 - seq

print("[Emissor] todas as mensagens confirmadas.")