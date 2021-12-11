fish_groups = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 'tmp': 0}
with open('input.txt') as f:
    for i in f:
        for j in [int(e) for e in i.strip().split(',')]:
            fish_groups[j] += 1

for i in range(256):
    fish_groups['tmp'] = fish_groups[0]
    for i in range(8):
        fish_groups[i] = fish_groups[i+1]
    fish_groups[6] += fish_groups['tmp']
    fish_groups[8] = fish_groups['tmp']

counter = 0
for i in range(9):
    counter += fish_groups[i]
print(counter)
