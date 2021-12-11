
arr = []
with open('input.txt') as f:
    arr = [i.strip().split('|') for i in f]


def findDifferentCharacters(a, b):
    dif = []
    for i in a:
        if i not in b:
            dif.append(i)
    for i in b:
        if i not in a:
            dif.append(i)
    return dif[0] if len(dif) == 1 else dif


def detectSignatures(mess):
    mess = mess.split()

    signatures = {
        "1": [i for i in mess if len(i) == 2][0],
        "4": [i for i in mess if len(i) == 4][0],
        "7": [i for i in mess if len(i) == 3][0],
        "8": [i for i in mess if len(i) == 7][0],
    }
    for i in signatures.values():
        mess.remove(i)

    top, mid, bot = '', '', ''

    # Find top segment char
    top = [i for i in signatures['7'] if i not in signatures['1']][0]

    # Find bot segment char
    for i in [i for i in mess if len(i) == 6]:
        dif = findDifferentCharacters(signatures['4']+top, i)
        if len(dif) == 1:
            bot = dif
            break

    # Add the signature for 9
    for i in mess:
        if sorted(i) == sorted(signatures['4'] + top + bot):
            signatures['9'] = i
            mess.remove(i)
            break

    # Find middle segment char
    for i in mess:
        dif = findDifferentCharacters(i, signatures['7'] + bot)
        if len(dif) == 1:
            mid = dif
            break

    # Add the signature for 3
    for i in mess:
        if sorted(i) == sorted(signatures['7'] + bot + mid):
            signatures['3'] = i
            mess.remove(i)
            break

    # Add the signature for 0
    tmp = [c for c in signatures['8']]
    tmp.remove(mid)
    for i in mess:
        if sorted(i) == sorted(tmp):
            signatures['0'] = i
            mess.remove(i)
            break

    # Add the signature for 6
    signatures['6'] = [i for i in mess if len(i) == 6][0]
    mess.remove(signatures['6'])

    # Add the signature for 5
    for i in mess:
        dif = findDifferentCharacters(i, signatures['6'])
        if len(dif) == 1:
            signatures['5'] = i
            mess.remove(i)
            break

    signatures['2'] = mess[0]

    return signatures


sum = 0
for t, code in arr:
    decrypted = ""
    signatures = detectSignatures(t)
    res = dict((''.join(sorted(v)), k) for k, v in signatures.items())
    for i in code.split():
        decrypted += res[''.join(sorted(i))]
    sum += int(decrypted)

print(sum)
