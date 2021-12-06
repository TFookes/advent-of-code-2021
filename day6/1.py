if __name__ == "__main__":
    lanternFishes = list()
    with open("./inputs.txt", "r") as inputs:
        lanternFishes = inputs.readlines()[0].split(',')

    lanternFishes = [int(fish) for fish in lanternFishes]

    for i in range (0, 80):
        bufferFishes = 0
        for j, fish in enumerate(lanternFishes):
            if fish != 0:
                lanternFishes[j] -= 1
            else:
                lanternFishes[j] = 6
                bufferFishes += 1

        for newFish in range(0, bufferFishes): lanternFishes.append(8) 

    print(len(lanternFishes))