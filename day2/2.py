if __name__ == "__main__":
    x = 0
    y = 0
    aim = 0
    with open("./input.txt", "r") as inputs:
        lines = inputs.readlines()
        for line in lines:
            instruction = line.split()[0]
            value = int(line.split()[1])
            if instruction == "forward":
                x += value
                y += value * aim
            elif instruction == "up":
                aim -= value
            else:
                aim += value

        print(x, y)
        print(x * y)
