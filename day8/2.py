digits = {
    2: 1,
    4: 4,
    3: 7,
    7: 8
}

shared = {
        0: {
            "len": 6,
            1: 2,
            4: 3,
            7: 3
        },
        2: {
            "len": 5,
            1: 1,
            4: 2,
            7: 2
        },
        3: {
            "len": 5, 
            1: 2,
            4: 3,
            7: 3
        }, 
        5: {
            "len": 5,
            1: 1,
            4: 3,
            7: 2
        },
        6: {
            "len": 6,
            1: 1,
            4: 3,
            7: 2
        },
        9: {
            "len": 6, 
            1: 2,
            4: 4,
            7: 3
        }
    }

def determineNumber(numbers, letters):
    finalNumber = ""
    for letter in letters:
        for number in numbers:
            if sorted(letter) == sorted(list(number.keys())[0]): 
                finalNumber += str(list(number.values())[0])
                break
            elif len(letter) in digits:
                finalNumber += str(digits[len(letter)])
                break

    return finalNumber

def determinePossibilities(digit, matches, length):
    possibilities = set(shared.keys())
    possibilities = set(filter(lambda x: shared[x]["len"] == length, possibilities))
    possibilities = set(filter(lambda x: shared[x][digit] == matches, possibilities))
    
    return possibilities


def checkSimilarity(digit, letters, sample):
    matches = 0
    for letter in sample:
        if letter in letters: matches += 1

    return matches


if __name__ == "__main__":
    with open("./inputs.txt", "r") as input:
        lines = input.readlines()
        count = 0
        for line in lines:
            knownSegments = set(filter(lambda x: len(x.strip()) in [2, 3, 4, 7], line.replace(" | ", " ").strip().split(" ")))
            unknownSegments = set(filter(lambda x: not len(x.strip()) in [2, 3, 4, 7], line.replace(" | ", " ").strip().split(" ")))
            letters = list(line.split("|")[1].strip().split(" "))
            numbers = list()

            for unknownDigit in unknownSegments:
                possibilities = set(shared.keys())
                for knownDigit in knownSegments:
                    if len(knownDigit) != 7: 
                        matches = checkSimilarity(digits[len(knownDigit)], knownDigit, unknownDigit)
                        possibilities = possibilities.intersection(determinePossibilities(digits[len(knownDigit)], matches, len(unknownDigit)))

                if len(possibilities) != 1: 
                    print("Wtf all my logic for this if off I hate life")
                    break 

                numbers.append({unknownDigit: possibilities.pop()})
            
            num = determineNumber(numbers, letters)
            count += int(num)

        print(count)
            