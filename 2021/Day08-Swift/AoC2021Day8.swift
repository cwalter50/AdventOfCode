/*
Here are the details about the challenge:
https://adventofcode.com/2021/day/8
*/

import Foundation

struct Line
{
    var input : [String]
    var output : [String]
}

func part1(myLines: [Line]) -> Int
{
    var count = 0
    for line in myLines
    {
        for out in line.output
        {
            if out.count == 2 || out.count == 3 || out.count == 4 || out.count == 7
            {
                count += 1
            }
        }
    }
    
    return count
}

// Helper Function to figure out 2,3,5 and 0, 6, 9
func AlettersAreInB(A: String, B: String) -> Bool
{
    for letter in A
    {
        if !B.contains(letter) {
            return false
        }
    }
    return true
}

// Helper returns true is num is a 2, false if num is 5
func isTwoOrFiveHelper(four: String, part: String) -> Bool
{
    // if the number is 5 then 3 of the 4 characters in 4 should be in the part.
    // if the number is 2 then 2 of the 4 characters in 4 should be in the part
    var count = 0
    for letter in four
    {
        if part.contains(letter)
        {
            count += 1
        }
    }
    if count == 3
    {
        return false
    }
    else
    {
        return true
    }
}

// Helper returns true is num is a 0, false if num is 9
func isZeroOrNineHelper(four: String, part: String) -> Bool
{
    // if the number is 0 then 3 of the 4 characters in 4 should be in the part.
    // if the number is 9 then 4 of the 4 characters in 4 should be in the part
    var count = 0
    for letter in four
    {
        if part.contains(letter)
        {
            count += 1
        }
    }
    if count == 3
    {
        return true
    }
    else
    {
        return false
    }
}
func createLineDictionary(line: Line) -> [Int: String]
{
    var lineDict : [Int: String] = [Int: String]()
    for part in line.input
    {
        switch part.count {
        case 2:
            lineDict.updateValue(part, forKey: 1)
        case 4:
            lineDict.updateValue(part, forKey: 4)
        case 7:
            lineDict.updateValue(part, forKey: 8)
        case 3:
            lineDict.updateValue(part, forKey: 7)
        default:
            // num is 0,2,3,5,6, or 9... We need to loop again to figure it out, because we need the clues from the other numbers to determine which one it is.
            if part.count > 8 {
                print("found a part whose length is \(part.count)")
            }
            
        }
    }
    for part in line.input
    {
        switch part.count {
        case 5:
            // num is 2, 3, or 5
            let one = lineDict[1] ?? ""
            let four = lineDict[4] ?? ""
            if AlettersAreInB(A: one, B: part)
            {
                lineDict.updateValue(part, forKey: 3)
            }
            else if isTwoOrFiveHelper(four: four, part: part)
            {
                lineDict.updateValue(part, forKey: 2)
            }
            else
            {
                lineDict.updateValue(part, forKey: 5)
            }

        case 6:
            // num is 0, 6, or 9
            let one = lineDict[1] ?? ""
            let four = lineDict[4] ?? ""
            if AlettersAreInB(A: one, B: part)
            {
                // part is 0 or 9
                if isZeroOrNineHelper(four: four, part: part)
                {
                    lineDict.updateValue(part, forKey: 0)
                }
                else
                {
                    lineDict.updateValue(part, forKey: 9)
                }
            }
            else
            {
                lineDict.updateValue(part, forKey: 6)
            }
        default:
            if part.count > 8{
                print("error") // i needed some default
            }
            
        }
    }
    
    return lineDict
}


// this will return a number for a string that matches in the dictionary
func matchOutputWithDictionary(myDict: [Int: String], part:String) -> Int
{
    for (key,value) in myDict
    {
        var foundMatch = true
        // make sure numbers are the same length
        if part.count == value.count {
            for letter in part
            {
                if !value.contains(letter)
                {
                    foundMatch = false
                }
            }
        }
        else {
            foundMatch = false
        }
        if foundMatch == true
        {
            return key
        }
    }
    print("did not find match for \(part) in \(myDict)")
    return 0
}

func part2(myLines: [Line]) -> Int
{

    var total = 0
    for line in myLines
    {
        // make a dictionary for each line connecting a number to a String
        let lineDictionary = createLineDictionary(line: line)
//        print(lineDictionary)
        
        // go through the output and match each set of characters with a number
        let thousDig = matchOutputWithDictionary(myDict: lineDictionary, part: line.output[0])
        let hundDig = matchOutputWithDictionary(myDict: lineDictionary, part: line.output[1])
        let tenDig = matchOutputWithDictionary(myDict: lineDictionary, part: line.output[2])
        let oneDig = matchOutputWithDictionary(myDict: lineDictionary, part: line.output[3])
        
        let num = 1000*thousDig + 100*hundDig + 10*tenDig + oneDig
        total += num
    }
    
    return total
}




if let path = Bundle.main.path(forResource: "data", ofType: "txt") {
    do {
        let data = try String(contentsOfFile: path, encoding: .utf8)
        var myStrings: [String] = data.components(separatedBy: .newlines)
//         print(myStrings)
        myStrings.removeLast() // last string is ""
        var lines = [Line]()
        for i in 0..<(myStrings.count)
        {
            let parts = myStrings[i].components(separatedBy: " | ")
            let input = parts[0].components(separatedBy: " ")
            let output = parts[1].components(separatedBy: " ")
            let newLine = Line(input: input, output: output)
            lines.append(newLine)
        }
        
       
        let part1Answer = part1(myLines: lines)
        print("Part1 Answer: \(part1Answer)")
        let part2Answer = part2(myLines: lines)
        print("Part2 Answer: \(part2Answer)")

        
    } catch {
        print(error)
    }
}

