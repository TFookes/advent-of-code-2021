import numpy as np

numFlashes = 0
octopusses = None
alreadyFlashed = list()
readyToFlash = list()

def increaseSingleOctopus(octopus):
    try:
        if octopus[0] >= 0 and octopus[1] >= 0:
            octopusses[octopus[0]][octopus[1]] += 1
            if octopusses[octopus[0]][octopus[1]] > 9 and octopus not in alreadyFlashed and octopus not in readyToFlash: 
                readyToFlash.append(octopus)
                return 1
    except: 
        # print("Octopus out of bounds exception", octopus)
        pass
    
    return 0

def flash():
    for flasher in readyToFlash:
        if not flasher in alreadyFlashed:
            alreadyFlashed.append(flasher)

            ## increase 3 above
            increaseSingleOctopus((flasher[0] - 1, flasher[1] - 1))
            increaseSingleOctopus((flasher[0], flasher[1] - 1))
            increaseSingleOctopus((flasher[0] + 1, flasher[1] - 1))
            ## increase 2 adjacent
            increaseSingleOctopus((flasher[0] - 1, flasher[1]))
            increaseSingleOctopus((flasher[0] + 1, flasher[1]))
            ## increase 3 below
            increaseSingleOctopus((flasher[0] - 1, flasher[1] + 1))
            increaseSingleOctopus((flasher[0], flasher[1] + 1))
            increaseSingleOctopus((flasher[0] + 1, flasher[1] + 1))

        readyToFlash.remove(flasher)

def increaseEnergy():
    for i, octopusRow in enumerate(octopusses):
        for j, octopus in enumerate(octopusRow):
            octopusses[i][j] += 1
            if octopusses[i][j] > 9: readyToFlash.append((i, j))

    while len(readyToFlash) > 0:
        flash()

    for octopus in alreadyFlashed:
        octopusses[octopus[0]][octopus[1]] = 0

    global numFlashes
    numFlashes += len(alreadyFlashed)
    alreadyFlashed.clear()
    readyToFlash.clear()

if __name__ == "__main__":
    with open("./inputs.txt", "r") as inputs:
        lines = inputs.readlines()
        lines = [line.strip() for line in lines]
        octopusses = np.array([int(char) for char in lines[0]])

        for i, line in enumerate(lines):
            if i == 0:
                continue

            octopusses = np.vstack([octopusses, [int(char) for char in line]])

        for i in range(0, 100):
            increaseEnergy()
            print(numFlashes)