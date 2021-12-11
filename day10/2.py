import math

pairs = {
    ")" : "(", 
    "]" : "[", 
    ">" : "<",
    "}" : "{",
}

values = {
    "(" : 1, 
    "[" : 2, 
    "<" : 4,
    "{" : 3
}

goodLines = list()
scores = list()

def parseChunks(line):
    openers = list()
    for char in line:
        if char in pairs.values(): openers.append(char)
        elif openers.pop() != pairs[char]: return None

    goodLines.append(line)

def parseChunksGoodLinesOnly(line):
    print(line)
    score = 0
    openers = list()
    for char in line:
        if char in pairs.values(): openers.append(char)
        else: openers.pop()

    for char in reversed(openers):
        score = (score * 5) + values[char]

    scores.append(score)

if __name__ == "__main__":
    with open("./inputs.txt", "r") as inputs:
        lines = inputs.readlines()
        for line in lines:
            parseChunks(line.strip())

        for line in goodLines:
            parseChunksGoodLinesOnly(line.strip())

    print(scores)
    print(sorted(scores)[math.floor(len(scores) / 2)])