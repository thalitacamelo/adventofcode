import io

with open('input.txt', 'r') as file:
    message = file.readline().strip()

code_bin ={}
with open('binarycode.txt', 'r') as file:
    for line in file:
        hexadecimal, binary = line.split(' = ')
        code_bin[hexadecimal] = binary.strip()

binary = ''
for hexa in message:
    binary += (code_bin[hexa])
binary = io.StringIO(binary)

def ID4 (string):
    i = int(string.read(1))
    literal = string.read(4)
    while i == 1:
        i = int(string.read(1))
        literal += string.read(4)
    return int(literal, 2)


packets = []
literals = []
def packet (string):
    version = int(string.read(3), 2)
    typeID = int(string.read(3), 2)
    packets.append((version, typeID))
    if typeID == 4:
        literal = ID4(string)
        literals.append((version, typeID, literal))
    else:
        i = int(string.read(1))
        if i == 0:
            length_packets = int(string.read(15), 2)
            endtell = string.tell() + length_packets
            while string.tell() < endtell:
                packet(string)
        elif i == 1:
            number_packets = int(string.read(11), 2)
            for _ in range(number_packets):
                packet(string)

packet(binary)

versionsum = sum(version for version, _ in packets)

print(versionsum)

