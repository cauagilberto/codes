import struct

def checksum(data: bytes) -> int:
    if len(data) % 2 == 1:
        data += b'\x00'
    s = 0
    for i in range(0, len(data), 2):
        w = (data[i] << 8) + data[i + 1]
        s += w
        s = (s & 0xffff) + (s >> 16)
    return (~s) & 0xffff

def make_pkt(seq: int, data: bytes) -> bytes:
    """Monta um pacote: [checksum(2B)][seq(4B)][dados]"""
    payload = struct.pack('!I', seq) + data
    c = checksum(payload)
    return struct.pack('!H', c) + payload

def parse_pkt(pkt: bytes):
    """Retorna (integro: bool, seq: int, dados: bytes)"""
    c_recv = struct.unpack('!H', pkt[:2])[0]
    payload = pkt[2:]
    c_calc = checksum(payload)
    seq = struct.unpack('!I', payload[:4])[0]
    data = payload[4:]
    return (c_recv == c_calc), seq, data