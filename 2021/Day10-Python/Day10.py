# Advent of Code 2021 Day 10
# https://adventofcode.com/2021/day/10

def readData():
    with open('2021/Day10-Python/data.txt') as f:
        lines = f.read().splitlines()
    #   nums = f.read().split(",")
      
        # lines = f.read().splitlines()
      
    return lines

def isCorrupted(line):
    openDelims = []
    for delimiter in line:
        if delimiter in {"{", "[","(","<"}:
            openDelims.append(delimiter)
        elif delimiter in {"}", "]",")",">"}:
            # check if it is corrupt by comparing to the last value in open
            last = openDelims[len(openDelims)-1]
            # print("Delimiter: "+delimiter + " last: "+ last)
            if delimiter == "}":
                if last == "{":
                    # remove last and keep going
                    openDelims.pop()
                else:
                    # its corrupt, add 1197
                    return 1197
            elif delimiter == "]":
                if last == "[":
                # remove last and keep going
                    openDelims.pop()
                else:
                    #its corrupt, add
                    return 57
            elif delimiter == ">":
                if last == "<":
                    # remove last and keep going
                    openDelims.pop()
                else:
                    #its corrupt, add 25137
                    return 25137
            elif delimiter == ")":
                if last == "(":
                    # remove last and keep going
                    openDelims.pop()
                else:
                    #its corrupt, add 25137
                    return 3
    # the line is not corrupt
    return 0

    
# solution is to keep track of the most recent open, 
# then if we get a close delimeter, check if it matches
# If it does not match, then it is corrupted
def part1(lines):
    score = 0
    for line in lines:
        score += isCorrupted(line)
    return score


def getCompletionDelimitersScore(line):
    # Use this to store all of the open delimeters at the end of the loop
    openDelims = []
    for delimiter in line:
        if delimiter in {"{", "[","(","<"}:
            openDelims.append(delimiter)
        elif delimiter in {"}", "]",")",">"}:
            # check if it is corrupt by comparing to the last value in open
            last = openDelims[len(openDelims)-1]
            # print("Delimiter: "+delimiter + " last: "+ last)
            if delimiter == "}" and last == "{":
                # remove last and keep going
                openDelims.pop() 
            elif delimiter == "]" and last == "[":
                # remove last and keep going
                openDelims.pop()
            elif delimiter == ">" and last == "<":
                # remove last and keep going
                openDelims.pop()
            elif delimiter == ")" and last == "(":
                # remove last and keep going
                openDelims.pop()
    # openDelims, store the open delims that we need to close. 
    # Loop backwards and add them one at a time in reverse
    closeDelims = []
    score = 0
    for i in range(len(openDelims) - 1,-1,-1):
        last = openDelims[i]
        if last == "{":
            closeDelims.append("}")
            score = score * 5 + 3
        elif last == "(":
            closeDelims.append(")")
            score = score * 5 + 1
        elif last == "<":
            closeDelims.append(">")
            score = score * 5 + 4
        elif last == "[":
            closeDelims.append("]")
            score = score * 5 + 2

    return score

def part2(lines):
    scores = []
    print("Part2 lineCount at Start: " + str(len(lines)))
    for i in range(len(lines)-1, -1, -1):
        if isCorrupted(lines[i]) > 0:
            lines.remove(lines[i])
    print("Part2 lineCount after removing corrupt: " + str(len(lines)))
    # all lines that are left are incomplete.
    for line in lines:
        score = getCompletionDelimitersScore(line)
        scores.append(score)

    scores.sort()
    # print(scores)
    middle = len(scores) // 2
    # print(middle)
    return scores[middle]


theLines = readData()  
# print(nums)

part1Answer = part1(theLines)
print("Part 1 Answer: " + str(part1Answer))

# reset Nums
# nums = readData()
part2Answer = part2(theLines)
print("Part2 Answer: " + str(part2Answer))
