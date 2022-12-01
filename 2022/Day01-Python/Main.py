# Advent of Code 2022 Day 1
# https://adventofcode.com/2022/day/1

def readData():
    with open('2022/Day01-Python/data.txt') as f:
        # lines = f.readlines()
        lines = f.read().splitlines()
        print(lines)
        return lines


def getElves(lines):
    elves = []
    count = 0
    for line in lines:
        if line == "":
            elves.append(count)
            count = 0
        else:
            count += int(line)

    elves.append(count)

    return elves
    


def part1(lines):
    elves = getElves(lines) # This will get the total calories of each elve and store them in an array

    part1Answer = max(elves)
    print("Part1 answer is: " + str(part1Answer))

def part2(lines):
    elves = getElves(lines)

    first = max(elves)
    elves.remove(first)
    second = max(elves)
    elves.remove(second)
    third = max(elves)

    part2Answer = first + second + third
    print("Part2 answer is: " + str(part2Answer))
    

lines = readData() 

part1(lines) 
part2(lines)
