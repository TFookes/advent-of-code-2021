if __name__ == "__main__":
    with open("./inputs.txt", "r") as inputs:
        positions = inputs.readlines()[0].split(",")
        positions = [int(x) for x in positions]
        totals = list()

        for i in range(min(positions), max(positions) + 1):
            total = 0
            for pos in positions:
                total += sum(range(1, abs(pos - i) + 1))
        
            totals.append(total)

        print(min(totals))