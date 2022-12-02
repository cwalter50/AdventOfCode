
// Advent of Code 2022 Day 2
// https://adventofcode.com/2022/day/2


// testing git at work computer


import UIKit

/*
 Computer Choices:
 A => Rock
 B => Paper
 C => Scissors
 
 Your Choices:
 X => Rock      1 pt
 Y => Paper     2 pts
 Z => Scissors  3 pts
 
 Win = 6 points
 Draw = 3 point
 Loss = 0
 
 */

struct Match
{
    var compChoice: String
    var userChoice: String
    
    var matchPoints: Int {
        var total = 0
        
        let userChoicePts = ["X": 1, "Y": 2, "Z": 3]
        total += userChoicePts[userChoice] ?? 0
        
        if userChoice == "X" && compChoice == "C"
        {
            total += 6
        }
        if userChoice == "Y" && compChoice == "A"
        {
            total += 6
        }
        if userChoice == "Z" && compChoice == "B"
        {
            total += 6
        }
        if (userChoice == "X" && compChoice == "A") || (userChoice == "Y" && compChoice == "B") || (userChoice == "Z" && compChoice == "C") {
            total += 3
        }
        
        
        return total
    }
}


func part1(matches: [Match], allMatchPoints: [Int]) -> Int
{
    var total = 0
    
    for i in allMatchPoints {
        total += i
    }
    
    return total
}

if let path = Bundle.main.path(forResource: "data", ofType: "txt") {
    do {
        let data = try String(contentsOfFile: path, encoding: .utf8)
        var myStrings: [String] = data.components(separatedBy: .newlines)
//         print(myStrings)
        myStrings.removeLast() // last string is ""
        print(myStrings)
        
        var matches = [Match]()
        var allMatchPoints = [Int]()
        for i in 0..<myStrings.count {
            let parts = myStrings[i].components(separatedBy: .whitespaces)
            
            if parts.count == 2 {
                let newMatch = Match(compChoice: parts[0], userChoice: parts[1])
                matches.append(newMatch)
                allMatchPoints.append(newMatch.matchPoints)
            }
        }
//
//
        let part1Answer = part1(matches: matches, allMatchPoints: allMatchPoints)
        print("Part1 Answer: \(part1Answer)")
//        let part2Answer = part2(myLines: lines)
//        print("Part2 Answer: \(part2Answer)")

        
    } catch {
        print(error)
    }
}
