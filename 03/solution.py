counters = {'0': [0]*12, '1': [0]*12}
array = []
with open("input.txt", 'r') as f:
    for i in f:
        array.append(i.strip())
        for index, j in enumerate(i.strip()):
            counters[j][index] += 1


def findMostCommon(arr, index):
    counters = {'0': 0, '1': 0}
    for i in arr:
        counters[i[index]] += 1
    return '0' if counters['0'] > counters['1'] else '1'


oxygen = array
c02 = array
index = 0

while True:
    if len(oxygen) == 1 and len(c02) == 1:
        break
    if len(oxygen) > 1:
        most_common = findMostCommon(oxygen, index)
        oxygen = [i for i in oxygen if i[index] == most_common]
    if len(c02) > 1:
        least_common = findMostCommon(c02, index)
        c02 = [i for i in c02 if i[index] != least_common]
    index += 1


print(oxygen[0], c02[0])
print(int(oxygen[0], base=2), int(c02[0], base=2))

print("Health system", int(oxygen[0], base=2) * int(c02[0], base=2))

most = ""
least = ""
for i in range(12):
    if counters['0'][i] > counters['1'][i]:
        most += '0'
        least += '1'
    else:
        most += '1'
        least += '0'

most = int(most, base=2)
least = int(least, base=2)
print("Power consumption:", most * least)
