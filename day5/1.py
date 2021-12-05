import numpy as np

if __name__ == "__main__":
    x0 = list()
    y0 = list()
    x1 = list()
    y1 = list()
    with open("./inputs.txt", "r") as inputs:
        lines = inputs.readlines()
        for line in lines:
            for i, coord in enumerate(line.strip().split(" -> ")):
                if i == 0:
                    x0.append(int(coord.split(",")[0]))
                    y0.append(int(coord.split(",")[1]))
                elif i == 1: 
                    x1.append(int(coord.split(',')[0]))
                    y1.append(int(coord.split(",")[1]))

    grid = np.zeros((max(max(x0), max(x1)), max(max(y0), max(y1))))

    for line in zip(x0, y0, x1, y1):
        if not (line[0] == line[2] or line[1] == line[3]):
            continue
        
        if line[0] == line[2]:
            if line[1] > line [3]:
                grid[line[0], line[3]:line[1] + 1] += 1
            else:
                grid[line[0], line[1]:line[3] + 1] += 1
        elif line[1] == line[3]:
            if line[0] > line[2]:
                grid[line[2]:line[0] + 1, line[1]] += 1
            else:
                grid[line[0]:line[2] + 1, line[1]] += 1
        

    unique, counts = np.unique(grid, return_counts=True)
    occurances = dict(zip(unique, counts))
    print(occurances)
    del occurances[0.0]
    del occurances[1.0]

    print(sum(occurances.values()))
