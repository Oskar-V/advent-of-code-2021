arr = []
with open('input.txt') as f:
    for i in f:
        arr.append([[int(j), False, 0] for j in i.strip()])


def isSmallest(array, index):
    x, y = index
    if x-1 >= 0 and array[y][x-1] <= array[y][x]:
        return False
    elif x+1 < len(array[y]) and array[y][x+1] <= array[y][x]:
        return False
    elif y-1 >= 0 and array[y-1][x] <= array[y][x]:
        return False
    elif y+1 < len(array) and array[y+1][x] <= array[y][x]:
        return False
    return True


def crawl(array, index=(0, 0), id=1):
    x, y = index
    if 0 > y or y >= len(array) or 0 > x or x >= len(
            array[y]) or array[y][x][0] == 9 or array[y][x][2] != 0:
        return 0
    else:
        array[y][x][2] = id
        return 1 + sum([crawl(array, (x + 1, y),
                              id),
                       crawl(array, (x - 1, y),
                             id),
                       crawl(array, (x, y + 1),
                             id),
                       crawl(array, (x, y - 1),
                             id)])


counter = 0
sum_of_lows = 0
last_id = 1
largest_bastions = [0, 0, 0]
for y, i in enumerate(arr):
    for x, j in enumerate(i):
        # Find the smallest points
        if isSmallest(arr, (x, y)):
            arr[y][x][1] = True
            counter += 1
            sum_of_lows += arr[y][x][0]+1

        # Map the basins
        bastion_size = crawl(arr, (x, y), last_id)
        if bastion_size != 0:
            largest_bastions = sorted(largest_bastions)
            if bastion_size > largest_bastions[0]:
                largest_bastions[0] = bastion_size
            last_id += 1

# for i in arr:
#     for j in i:
#         print(j[2], end=" ")
#     print()

sum_of_basins = 1
for i in largest_bastions:
    sum_of_basins *= i


print("Counter:", counter)
print("Risk factor:", sum_of_lows)
print("Sum of basins:", sum_of_basins)
