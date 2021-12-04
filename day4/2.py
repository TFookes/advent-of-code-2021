import numpy as np

def searchBoard(board, called):
    result = np.where(board == called)
    found = list(zip(result[0], result[1]))

    for coord in found:
        board[coord[0]][coord[1]] = -1

    return board

def checkForWinner(boards):
    winners = set()
    for j, board in enumerate(boards):
        for i in range(board.shape[0]):
            if np.all(board[i] == board[i][0]):
                winners.add(j)

        trans_board = board.T
        for i in range(trans_board.shape[0]):
            if np.all(trans_board[i] == trans_board[i][0]):
                winners.add(j)

    return winners

def countUnmarked(board):
    sum = 0
    result = np.where(board != '-1')
    found = list(zip(result[0], result[1]))

    for coord in found:
        sum += int(board[coord[0], coord[1]])

    return sum


if __name__ == "__main__":
    called = list()
    boards = list()
    buffer = list()
    with open("./inputs.txt", "r") as input:
        lines = input.readlines()
        for i, line in enumerate(lines):
            if i == 0: 
                called = line.strip().split(",")
                continue
            
            if line.strip() == "":
                if i == 1: continue
                boards.append(np.array(buffer))
                buffer = list()
                continue

            buffer.append(line.split())

    for number in called:

        for board in boards:
            board = searchBoard(board, number)

        winners = checkForWinner(boards)
        if len(winners) > 0:
            if len(boards) == 1:
                print(countUnmarked(boards[0]) * int(number))
            
            for winner in sorted(winners, reverse=True):
                del(boards[winner])
            

    