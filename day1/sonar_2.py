if __name__ == "__main__":
    windows = list()
    with open("./sonar_inputs.txt", "r") as inputs:
        lines = inputs.readlines()
        for i, line in enumerate(lines):
            try:
                windows.append([int(lines[i].strip()), int(lines[i+1].strip()), int(lines[i+2].strip())])
            except:
                pass

        print(windows)

    sums = list()
    for window in windows:
        sums.append(sum(window))
            
    print(sums)

    count = 0
    previous = None

    for line in sums:
        if not previous == None:
            if int(previous) < int(line):
                print(previous, line)
                count += 1

        previous = line

    print(count)