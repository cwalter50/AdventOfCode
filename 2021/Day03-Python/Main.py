
# Advent of Code 2021 Day 3
# https://adventofcode.com/2021/day/3

def readData():
    with open('data.txt') as f:
        # lines = f.readlines()
        lines = f.read().splitlines()
        return lines

def getGamma(lines):
    gamma = ""
    for i in range(len(lines[0])):
        count1 = 0
        count0 = 0
        for line in lines:
            if line[i] == "1":
                count1 += 1
            else:
                count0 += 1
                
        if count1 > count0:
            gamma += "1"
        else:
            gamma += "0"
    # print(gamma)
    return gamma

def getEpsilon(gamma):
    result = ""
    for letter in gamma:
        if letter == "1":
            result += "0"
        else:
            result += "1"
    return result

# this will convert a binary String to a Decimal Number
def binaryToDecimal(binary):
    decimal = 0
    for i in range(len(binary)):
        # print("decimal " + str(decimal) + " + "+ binary[i]+"*"+str(pow(2,len(binary)-1-i)))
        decimal += int(binary[i]) * pow(2,len(binary)-1-i)

    return decimal


def getCO2(data):
    for i in range(len(data[0])):
        count1 = 0
        count0 = 0
        for line in data:
            if line[i] == "1":
                count1 += 1
            else:
                count0 += 1
        if len(data) > 1:
            if count0 <= count1:
                removeLines(data,"1",i)
            else:
                removeLines(data,"0",i)
        else:
            break
    return data[0]

def getOxygen(data):
    for i in range(len(data[0])):
        count1 = 0
        count0 = 0
        for line in data:
            if line[i] == "1":
                count1 += 1
            else:
                count0 += 1
        if len(data) > 1:
            if count1 >= count0:
                removeLines(data,"0",i)
            else:
                removeLines(data,"1",i)
        else:
            break
    return data[0]

def removeLines(lines, letter, position):
    for i in range(len(lines)-1,-1,-1):
        if lines[i][position] == letter:
            lines.pop(i)


   

def part1(lines):

    gamma = getGamma(lines)
    epsilon = getEpsilon(gamma)

    # print(gamma)
    gammaDecimal = binaryToDecimal(gamma)
    # print(gammaDecimal)
    # print(epsilon)
    epsilonDecimal = binaryToDecimal(epsilon)
    # print(epsilonDecimal)
    answer = gammaDecimal * epsilonDecimal
    print("Part1 answer is " + str(answer))


def part2(lines):

    oxygen = getOxygen(lines)
    # print("Oxygen: " + oxygen)
    oxygenDecimal = binaryToDecimal(oxygen)
    # print("OxygenDecimal: " + str(oxygenDecimal))

    # reload lines because we removed them all in the getOxygen
    lines = readData()
    co2 = getCO2(lines)
    # print("CO2: "+co2)
    co2Decimal = binaryToDecimal(co2)
    # print("co2Decimal: "+ str(co2Decimal))
    answer = oxygenDecimal * co2Decimal
    print("Part2 answer is " + str(answer))



lines = readData()  

part1(lines)
part2(lines)








