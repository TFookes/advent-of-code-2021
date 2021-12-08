if __name__ == "__main__":
    with open("./inputs.txt", "r") as input:
        lines = input.readlines()
        count = 0
        for line in lines:
            count += len(list(filter(lambda x: len(x.strip()) in [2, 3, 4, 7], line.split('|')[1].split(" "))))

        print(count)