if __name__ == "__main__":
    lanternFishes = {
        0: 0,
        1: 0,
        2: 0,
        3: 0,
        4: 0,
        5: 0,
        6: 0,
        7: 0, 
        8: 0
    }
    with open("./inputs.txt", "r") as inputs:
        for fish in inputs.readlines()[0].split(','):
            lanternFishes[int(fish)] += 1

    for i in range (0, 256):
        bufferFishes = 0
        for days in lanternFishes:
            if days == 0:
                bufferFishes = lanternFishes[days]
            else:
                lanternFishes[days - 1] += lanternFishes[days]
            
            lanternFishes[days] = 0 

        lanternFishes[8] += bufferFishes 
        lanternFishes[6] += bufferFishes


    print(sum(lanternFishes.values()))