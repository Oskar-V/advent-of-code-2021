number_order, boards, first_winner, last_winner = [], [], '', ''
with open("input.txt") as f:
    number_order = f.readline().strip().split(',')
    for i in f.readlines():
        if i.strip() == "":
            boards.append([])
        else:
            boards[-1].append([(j, 'o') for j in i.strip().split()])


def isInBoard(value, board):
    for i in board:
        if (value, 'o') in i:
            i[i.index((value, 'o'))] = (value, '+')
            return True
    return False


def hasWon(board):
    for i in board:
        if all(e[1] == '+'for e in i):
            return True
    for i in list(zip(*board[::-1])):
        if all(e[1] == '+'for e in i):
            return True
    return False


def calculateScore(board, last_number):
    summed_value = 0
    for i in board:
        summed_value += sum(int(j[0]) for j in i if j[1] == 'o')
    return summed_value * int(last_number)


def playGame(active_boards):
    for drawn_number in number_order:
        for board_index, j in enumerate(active_boards):
            if isInBoard(drawn_number, j) and hasWon(j):
                return j, drawn_number, board_index


while len(boards) > 0:
    winner, last_number, board_index = playGame(boards)
    if first_winner == '':
        first_winner = [winner, last_number, board_index]
    boards.pop(board_index)
    last_winner = [winner, last_number, board_index]

print(
    f"First winner: {first_winner[2]}, with a score of: {calculateScore(first_winner[0], first_winner[1])}")
print(
    f"First winner: {last_winner[2]}, with a score of: {calculateScore(last_winner[0], last_winner[1])}")
