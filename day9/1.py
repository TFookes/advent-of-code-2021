import numpy as np

def checkAdjacent(x, y, matrix):
    xi = [9, 9, 9, 9]
    for i, xn in enumerate(xi):
        try:
            if i == 0:
                xi[i] = matrix[x][y - 1]
            elif i == 1:
                xi[i] = matrix[x][y + 1]
            elif i == 2:
                xi[i] = matrix[x - 1][y]
            elif i == 3:
                xi[i] = matrix[x + 1][y]
        except:
            pass

    return comparePoints(int(matrix[x][y]), xi[0], xi[1], xi[2], xi[3])

def comparePoints(x0, x1, x2, x3, x4):
    return x0 + 1 if x0 < x1 and x0 < x2 and x0 < x3 and x0 < x4 else 0


if __name__ == "__main__":
    with open("./inputs.txt", "r") as inputs:
        lines = inputs.readlines()
        lines = [line.strip() for line in lines]
        risk = 0
        matrix = np.array([int(char) for char in lines[0]])
        
        for i, line in enumerate(lines):
            if i == 0:
                continue

            matrix = np.vstack([matrix, [int(char) for char in line]])

        for x, row in enumerate(matrix):
            for y, column in enumerate(row):
                if matrix[x][y] == 9:
                    continue

                risk += checkAdjacent(x, y, matrix)

        print(risk)

        
