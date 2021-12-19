with open('input.txt', 'r') as file:
    positions = list(map(int, file.readline().split(',')))

def cost (i):
    return sum(abs(p - i) for p in positions)

maxposition = max(positions)

print(min(map(cost, range(maxposition))))