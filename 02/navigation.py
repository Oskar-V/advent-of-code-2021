aim, forward, depth = 0, 0, 0

with open("input.txt") as f:
    for i in f:
        i = i.strip()
        value = int(i[-1])
        if i[0] == "f":
            forward += value
            depth += value * aim
        else:
            aim += (value if i[0] == 'd' else -value)

print("final horizontal position * final depth =", depth * forward)
