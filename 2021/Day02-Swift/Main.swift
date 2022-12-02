/*
Here are the details about the challenge:
https://adventofcode.com/2021/day/2
*/
import swift
import Foundation

if let path = Bundle.main.path(forResource: "data", ofType: "txt") {
    do {
        let data = try String(contentsOfFile: path, encoding: .utf8)
        let myStrings: [String] = data.components(separatedBy: .newlines)
//         print(myStrings)
       
        let part1Answer = part1(myStrings: myStrings)
        print(part1Answer)
        
        let part2Answer = part2(myStrings: myStrings)
        print(part2Answer)
        
    } catch {
        print(error)
    }
}


func part1(myStrings: [String]) -> Int
{
    var horizontal = 0
    var vertical = 0
    for part in myStrings
    {
        let parts = part.components(separatedBy: " ")
//            print(parts)
        switch parts[0] {
        case "forward":
            horizontal += Int(parts[1])!
        case "up":
            vertical -= Int(parts[1])!
        case "down":
            vertical += Int(parts[1])!
        default:
            print(parts[0])
        }
    }
    print(horizontal)
    print(vertical)
    let answer = horizontal*vertical
    return answer
}

func part2(myStrings: [String]) -> Int
{
    var horizontal = 0
    var vertical = 0
    var aim = 0
    for part in myStrings
    {
        let parts = part.components(separatedBy: " ")
        
//            print(parts)
        switch parts[0] {
        case "forward":
            horizontal += Int(parts[1])!
            vertical += aim * Int(parts[1])!
        case "up":
            aim -= Int(parts[1])!
        case "down":
            aim += Int(parts[1])!
        default:
            print(parts[0])
        }
    }
    print(horizontal)
    print(vertical)
    let answer = horizontal*vertical
    
    return answer
}

