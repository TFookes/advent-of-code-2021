def determineBitMode(input, index):
    ones, zeroes = 0, 0
    for binary in input:
        if binary[index] == "1": ones += 1
        else: zeroes += 1
    
    return ones >= zeroes

if __name__ == "__main__": 
    oxygen = list()
    co2 = list()

    with open("./inputs.txt", "r") as inputs:
        lines = inputs.readlines()
        for line in lines:
            oxygen.append(str(line.strip()))
            co2.append(str(line.strip()))

    for i in range(0, 12):
        if len(oxygen) > 1:
            if determineBitMode(oxygen, i): oxygen = filter(lambda x: x[i] == "1", oxygen)
            else:                           oxygen = filter(lambda x: x[i] == "0", oxygen)
        
        if len(co2) > 1:
            if determineBitMode(co2, i):    co2 = filter(lambda x: x[i] == "0", co2)
            else:                           co2 = filter(lambda x: x[i] == "1", co2)

    print(int(oxygen[0], 2) * int(co2[0], 2))

