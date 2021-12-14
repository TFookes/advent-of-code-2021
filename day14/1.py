import math

def insertionPass(template, rules):
    bufferTemplate = dict(template)
    for key in template.keys():
        if key in rules.keys():
            pair = [char for char in key]
            try: bufferTemplate[pair[0] + rules[key]][1] += template[key][0]
            except:  bufferTemplate[pair[0] + rules[key]] = [0, template[key][0]]

            try: bufferTemplate[rules[key] + pair[1]][1] += template[key][0]
            except: bufferTemplate[rules[key] + pair[1]] = [0, template[key][0]]
                
    for pair in bufferTemplate: 
        bufferTemplate[pair][0] = bufferTemplate[pair][1]
        bufferTemplate[pair][1] = 0

    
    return bufferTemplate

if __name__ == "__main__":
    template = {}
    rules = {}
    og_string_start = None
    og_string_end = None

    with open("./inputs.txt", "r") as inputs:
        lines = inputs.readlines()
        lines = [line.strip() for line in lines]

        for i, line in enumerate(lines):
            if i == 0:
                pairs = [chars for chars in line.strip()]
                for j, i in enumerate(range(0, len(pairs) - 1)): 
                    if j == 0: 
                        og_string_start = pairs[i]
                    elif j == len(pairs) - 2: 
                        og_string_end = pairs[i + 1]
                    template[pairs[i] + pairs[i + 1]] = [1, 0]

            elif line != "":
                rules[line.strip().split(" -> ")[0]] = line.strip().split(" -> ")[1]

        for i in range (0, 40):
            template = insertionPass(template, rules)
        
        counts = {}
        for pair in template:
            for char in pair:
                try: counts[char] += template[pair][0]
                except: counts[char] = template[pair][0]

        for letter in counts:
            if og_string_start == letter or og_string_end == letter:
                counts[letter] = math.ceil(counts[letter] / 2)
            else:
                counts[letter] = counts[letter] / 2

        print(counts)

        max = max(counts, key=counts.get)
        min = min(counts, key=counts.get)

        print(max, min)
        print(counts[max], "-", counts[min], '=', counts[max] - counts[min])
    