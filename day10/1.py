pairs = {
    ")" : "(", 
    "]" : "[", 
    ">" : "<",
    "}" : "{"
}

values = {
    ")" : 3, 
    "]" : 57, 
    ">" : 25137,
    "}" : 1197
}

corruptedBits = list()
openers = list()

def parseChunks(line):
    print(line)
    for i, char in enumerate(line):
        if char in pairs.values(): 
            print(line[i:])
            openers.append(char)
        
        if char in pairs.keys():
            match = openers.pop()
            print(match, char, line)
            if match != pairs[char]: 
                corruptedBits.append(values[char])
                return None

if __name__ == "__main__":
    with open("./inputs.txt", "r") as inputs:
        lines = inputs.readlines()
        for line in lines:
            parseChunks(line)

        print(sum(corruptedBits))
