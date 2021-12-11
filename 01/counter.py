array = []
last = 'start'
counter = 0
with open("input.txt", 'r') as f:
    for i in f:
        value = int(i)
        if last != 'start' and last < value:
            counter += 1
        last = value
        array.append(value)
print("Normal counter", counter)

last='start'
counter = 0
for i in range(len(array)-2):
    value = sum(array[i:i+3])
    if last != 'start' and last < value:
        counter += 1
    last = value

print("Sum counter", counter)
