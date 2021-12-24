with open('input.txt', 'r') as file:
    x, y = file.readline().split(': ')[1].split(', ')
    xmin, xmax = tuple(map(int, x[2:].split('..')))
    ymin, ymax = tuple(map(int, y[2:].split('..')))

target_region = {(x,y) for x in range(xmin, xmax + 1) for y in range(ymin, ymax + 1)}

target_hits = set()

for y in range(1, 200):
    for x in range(-200, 200):
        vx, vy, xi, yi = x, y, 0, 0
        while xi <= xmax and yi >= ymin:
            xi, yi = xi + vx, yi + vy
            if (xi, yi) in target_region:
                target_hits.add((x,y))
            vx = max(vx - 1, 0)
            vy -= 1

print(len(target_hits))