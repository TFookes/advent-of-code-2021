if __name__ == "__main__":
    with open("./inputs.txt", "r") as inputs:
        positions = inputs.readlines()[0].split(",")
        positions = [int(x) for x in positions]
        totals = list()

        for i in range(min(positions), max(positions) + 1):
            sum = 0
            for pos in positions:
                sum += abs(pos - i)
        
            totals.append(sum)

        print(min(totals))