arr = []
flash_counter = 0
step_counter = 0
with open('input.txt') as f:
    for i in f:
        arr.append([[int(e), False] for e in i.strip()])


def stage2(array, pos=(0, 0)):
    global flash_counter
    x, y = pos
    if array[y][x][1]:
        array[y][x][0] += 1
        return
    elif array[y][x][0] > 9:
        flash_counter += 1
        array[y][x] = [0, True]
        for i in range(y-1, y+2):
            if 0 <= i < len(array):
                for j in range(x-1, x+2):
                    if 0 <= j < len(array[i]):
                        array[i][j][0] += 1
                        if array[i][j][0] > 9 and not array[i][j][1]:
                            stage2(array, (j, i))


def stage3(array):
    rows = []
    for y, i in enumerate(array):
        rows.append(all([k[1] for k in i]))
        for x, j in enumerate(i):
            if j[1]:
                array[y][x] = [0, False]
    return all(rows)


while(True):
    step_counter += 1
    for i, e in enumerate(arr):
        arr[i] = [[j[0]+1, False] for j in e]

    for y, j in enumerate(arr):
        for x, k in enumerate(j):
            stage2(arr, (x, y))
    if(stage3(arr)):
        break

print(f"Flash counter:\t{flash_counter}\nStep counter:\t{step_counter}")
