import numpy as np

def foldUp(top, bottom):
    foldedBottom = np.flip(bottom, 0)
    for i, row in enumerate(foldedBottom):
        for j, column in enumerate(foldedBottom[0]):
            if foldedBottom[i][j] == 1: top[i][j] = 1

    return top

def foldLeft(left, right): 
    foldedRight = np.flip(right, 1)
    for i, row in enumerate(foldedRight):
        for j, column in enumerate(foldedRight[0]):
            if foldedRight[i][j] == 1: left[i][j] = 1

    return left

def countDots(paper):
    count = 0
    for i, row in enumerate(paper):
        for j, column in enumerate(paper[0]):
            if paper[i][j] == 1: count += 1

    return count

if __name__ == "__main__":
    coords = list()
    folds = list()

    with open("./inputs.txt", "r") as inputs:
        lines = inputs.readlines()
        lines = [line.strip() for line in lines]

        for line in lines:
            if line.split(" ")[0] == "fold":
                folds.append((line.split(" ")[2].split("=")[0], int(line.split(" ")[2].split("=")[1])))
            elif line != "":
                coords.append((int(line.split(",")[0]), int(line.split(",")[1])))

        maxx = max(coords, key=lambda x: x[0])[0] + 1
        maxy = max(coords, key=lambda x: x[1])[1] + 1

        paper = np.zeros((maxy, maxx), dtype=int)
        for coord in coords:
            paper[coord[1]][coord[0]] = 1

        for fold in folds:
            if fold[0] == "y":
                halves = np.vsplit(paper, np.array([fold[1]]))
                paper = foldUp(halves[0], np.delete(halves[1], 0, 0))
            else:
                halves = np.hsplit(paper, np.array([fold[1]]))
                paper = foldLeft(halves[0], np.delete(halves[1], 0, 1))

            break

        print("\n\nfinal paper")
        print(paper)

        print(countDots(paper))



