with open('input.txt', 'r') as file:
    positions = list(map(int, file.readline().split(',')))

def f(n):
    return (n + 1) * n // 2

def cost (i):
    return sum(f(abs(p - i)) for p in positions)

maxposition = max(positions)

print(min(map(cost, range(maxposition))))
