if __name__ == "__main__": 
    gamma = ""
    epsilon = ""

    with open("./inputs.txt", "r") as inputs:
        lines = inputs.readlines()
        ones = list()
        zeroes = list()
        for j, line in enumerate(lines):
            for i, bit in enumerate(str(line.strip())):
                if j == 0:
                    if bit == "1":
                        ones.append(1)
                        zeroes.append(0)
                    else:
                        zeroes.append(1)
                        ones.append(0)
                else:
                    if bit == "1":
                        ones[i] += 1
                    else:
                        zeroes[i] += 1

    print(ones, zeroes)
    for i, bit in enumerate(ones):
        if ones[i] > zeroes[i]:
            gamma += "1"
            epsilon += "0"
        else:
            gamma += "0"
            epsilon += "1"

    print(int(gamma, 2) * int(epsilon, 2))