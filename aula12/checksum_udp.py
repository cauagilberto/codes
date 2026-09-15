def checksum16(data: bytes) -> int:
    if len(data) % 2:
        data += b'\x00'
    total = 0
    for i in range(0, len(data), 2):
        word = (data[i] << 8) + data[i + 1]
        total += word
        total = (total & 0xFFFF) + (total >> 16)  # soma o vai-um (carry)
    return (~total) & 0xFFFF  # complemento de 1


def verificar_checksum16(data: bytes, checksum: int) -> int:
    if len(data) % 2:
        data += b'\x00'
    data += checksum.to_bytes(2, 'big')
    total = 0
    for i in range(0, len(data), 2):
        word = (data[i] << 8) + data[i + 1]
        total += word
        total = (total & 0xFFFF) + (total >> 16)
    return total & 0xFFFF


payload = b"Ola, este e um datagrama UDP de teste"
cs = checksum16(payload)
print(f"Checksum calculado: {hex(cs)}")

# Verificacao: somando o payload + checksum, o resultado deve ser 0xFFFF
verificacao = verificar_checksum16(payload, cs)
print(f"Verificacao (deve ser 0xffff): {hex(verificacao)}")

# Simulando corrupcao de 1 bit no payload
payload_corrompido = bytearray(payload)
payload_corrompido[0] ^= 0b00000001
resultado_corrompido = verificar_checksum16(
    bytes(payload_corrompido), cs
)
print(f"Verificacao com bit corrompido (nao deve ser 0xffff): {hex(resultado_corrompido)}")