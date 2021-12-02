if __name__ == "__main__":
    x = 0
    y = 0
    with open("./input.txt", "r") as inputs:
        lines = inputs.readlines()
        for line in lines:
            instruction = line.split()[0]
            value = int(line.split()[1])
            print(instruction, value)
            if instruction == "forward":
                x += value
            elif instruction == "up":
                y -= value
            else:
                y += value

        print(x, y)
        print(x * y)
