import io
from functools import reduce

with open('input.txt', 'r') as file:
    message = file.readline().strip()

code_bin ={}
with open('binarycode.txt', 'r') as file:
    for line in file:
        hexadecimal, binary_message = line.split(' = ')
        code_bin[hexadecimal] = binary_message.strip()

binary_message = ''
for hexa in message:
    binary_message += (code_bin[hexa])
binary_message = io.StringIO(binary_message)

def ID4 (string):
    i = int(string.read(1))
    literal = string.read(4)
    while i == 1:
        i = int(string.read(1))
        literal += string.read(4)
    return int(literal, 2)


def read_packet (string):
    version = int(string.read(3), 2)
    typeID = int(string.read(3), 2)
    subpackets = []
    if typeID == 4:
        literal = ID4(string)
        return (typeID, literal)
    else:
        i = int(string.read(1))
        if i == 0:
            length_packets = int(string.read(15), 2)
            endtell = string.tell() + length_packets
            while string.tell() < endtell:
                subpackets.append(read_packet(string))
        elif i == 1:
            number_packets = int(string.read(11), 2)
            for _ in range(number_packets):
                subpackets.append(read_packet(string))
        return (typeID, subpackets)


def calculate_expression (packet):
    typeID, subpackets = packet
    if typeID == 0:
        return sum(calculate_expression(subpacket) for subpacket in subpackets)
    if typeID == 1:
        return reduce(lambda x, y: x*y, [calculate_expression(subpacket) for subpacket in subpackets])
    if typeID == 2:
        return min(calculate_expression(subpacket) for subpacket in subpackets)
    if typeID == 3:
        return max(calculate_expression(subpacket) for subpacket in subpackets)
    if typeID == 4:
        return subpackets
    if typeID == 5:
        return 1 if calculate_expression(subpackets[0]) > calculate_expression(subpackets[1]) else 0
    if typeID == 6:
        return 1 if calculate_expression(subpackets[0]) < calculate_expression(subpackets[1]) else 0
    if typeID == 7:
        return 1 if calculate_expression(subpackets[0]) == calculate_expression(subpackets[1]) else 0


packet = read_packet(binary_message)
value = calculate_expression(packet)

print(value)