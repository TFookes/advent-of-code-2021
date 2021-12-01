if __name__ == "__main__":
    count = 0
    previous = None
    with open("./sonar_inputs.txt", "r") as inputs:
        for line in inputs:
            line = line.strip()
            if not previous == None:
                if int(previous) < int(line):
                    print(previous, line)
                    count += 1

            previous = line

    print(count)