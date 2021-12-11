number_order = []
boards = []
with open("input.txt", 'r') as f:
    for i in f:
        i = i.strip()
        if number_order == []:
            number_order = i.split(',')
        else:
            if i == "":
                boards.append([])
            else:
                boards[-1].append([(j, 'o') for j in i.split()])


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


def prettyPrint(board, board_index, last_value=0):
    print('#'*33, f'{board_index}:{last_value}', '#'*33)
    for i in board:
        for j in i:
            print(f'{j}\t', end="")
        print()
    print('#'*33, calculateScore(board, last_value), '#'*33, end="\n\n")


def calculateScore(board, last_number):
    sum = 0
    for i in board:
        for j in i:
            if j[1] == 'o':
                sum += int(j[0])
    return sum * int(last_number)


def playGame(active_boards):
    for drawn_number in number_order:
        for board_index, j in enumerate(active_boards):
            if isInBoard(drawn_number, j):
                if hasWon(j):
                    return j, drawn_number, board_index


while len(boards) > 0:
    winner, last_number, board_index = playGame(boards)
    prettyPrint(winner, board_index, last_number)
    boards.pop(board_index)
