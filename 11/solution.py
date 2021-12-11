arr = []
flash_counter = 0
with open('input.txt') as f:
    for i in f:
        arr.append([[int(e), False] for e in i.strip()])


def printStatus(array):
    print("#"*(len(array)*2-1))
    for i in array:
        for j in i:
            print(j[0], end=" ")
        print()
    print("#"*(len(array)*2-1))


def stage1(array):
    for i, e in enumerate(array):
        array[i] = [[j[0]+1, False] for j in e]


def stage2(array, pos=(0, 0)):
    global flash_counter
    x, y = pos
    if not 0 <= y < len(array) or not 0 <= x < len(array[y]):
        return
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


i = 0
while(True):
    # for i in range(200):
    i += 1
    print("Running step:", i)
    # printStatus(arr)
    stage1(arr)
    for y, j in enumerate(arr):
        for x, k in enumerate(j):
            stage2(arr, (x, y))
    if(stage3(arr)):
        print("All flashed at the same time")
        break
printStatus(arr)

print("Flash counter:", flash_counter)
