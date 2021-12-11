from math import copysign

lines = []
intersect_counter = 0
MATRIX_SIZE = 1000

grid = [[0] * MATRIX_SIZE for _ in range(MATRIX_SIZE)]

with open("input.txt", 'r') as f:
    for i in f:
        values = [int(e) for e in i.strip().replace(' -> ', ',').split(',')]
        lines.append([{'x': values[0], 'y': values[1]}, {
                     'x': values[2], 'y': values[3]}])


def addLineToGrid(line, grid):
    if line[0]['x'] > line[1]['x'] or line[0]['y'] > line[1]['y']:
        line[0], line[1] = line[1], line[0]
    x_dif = line[1]['x']-line[0]['x']
    y_dif = line[1]['y']-line[0]['y']
    # grid[line[0]['y']][line[0]['x']] = 5
    # grid[line[1]['y']][line[1]['x']] = 5
    if abs(x_dif) == abs(y_dif):
        if x_dif == 0:
            grid[line[0]['y']][line[1]['x']] += 1
            return
        for i in range(abs(x_dif)+1):
            grid[int(line[0]['y']+copysign(i, y_dif))
                 ][int(line[0]['x']+copysign(i, x_dif))] += 1
    elif x_dif != 0:
        for i in range(line[0]['x'], abs(x_dif)+line[0]['x']+1):
            grid[line[0]['y']][i] += 1
    elif y_dif != 0:
        for i in range(line[0]['y'], abs(y_dif)+line[0]['y']+1):
            grid[i][line[0]['x']] += 1


for i in lines:
    addLineToGrid(i, grid)

for i in grid:
    for j in i:
        if j > 1:
            intersect_counter += 1

if MATRIX_SIZE < 20:
    for i in grid:
        for j in i:
            print(j, end=" ")
        print()

print(intersect_counter)
