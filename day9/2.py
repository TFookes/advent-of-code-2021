import numpy as np

def checkBasin(x, y, matrix):
    basin = set()
    basin.add(checkAdjacent(x, y, matrix, basin))
    basin = set(filter(None, basin))
    return basin

def checkAdjacent(x, y, matrix, basin):
    try:
        if ((x, y) not in basin) and matrix[x][y] != 9 and x >= 0 and y >= 0:
            basin.add((x, y))
            checkAdjacent(x, y - 1, matrix, basin)
            checkAdjacent(x, y + 1, matrix, basin)
            checkAdjacent(x - 1, y, matrix, basin)
            checkAdjacent(x + 1, y, matrix, basin)
    except:
        return None
        

if __name__ == "__main__":
    with open("./inputs.txt", "r") as inputs:
        lines = inputs.readlines()
        lines = [line.strip() for line in lines]
        basins = list()
        matrix = np.array([int(char) for char in lines[0]])
        
        for i, line in enumerate(lines):
            if i == 0:
                continue

            matrix = np.vstack([matrix, [int(char) for char in line]])

        for x, row in enumerate(matrix):
            for y, column in enumerate(row):
                if matrix[x][y] == 9:
                    continue
                
                basin = checkBasin(x, y, matrix)
                for coord in basin:
                    matrix[coord[0]][coord[1]] = 9

                basins.append(len(basin))

        size = 1
        for i in range(0, 3):
            size = size * max(basins)
            basins.remove(max(basins))

        print(size)

        
