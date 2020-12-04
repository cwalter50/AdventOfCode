import UIKit
import Foundation

/*
 About the challenge: Advent of Code Day 4
 https://adventofcode.com/2020/day/4
 */

var myStrings = [String]()
if let path = Bundle.main.path(forResource: "data", ofType: "txt") {
    do {
        let data = try String(contentsOfFile: path, encoding: .utf8)
        // Split based on characters.
//        let parts = line.components(separatedBy: separators)
        myStrings = data.components(separatedBy: "\n\n")
        
//        print(myStrings)
        // TextView.text = myStrings.joined(separator: ", ")
    } catch {
        print(error)
    }
}

// we now have each row in a [String] called myStrings
// break each string up into parts.

var ids : [[String: String]] = [[String:String]]() // this will contain the final dictionary values

for id in myStrings
{
    var newID : [String: String] = [String:String]()
    let separators = CharacterSet(charactersIn: ":,\n, ")
    let newIDArray = id.components(separatedBy: separators)
//    print(newIDArray)
    for i in 0..<newIDArray.count/2
    {
        newID[newIDArray[2*i]] = newIDArray[2*i+1]
    }
//    print(newID)
    ids.append(newID)
    
    
}
//print(ids)
// ids now contains all of the ids in the correct format.

// loop through and count valid ids: PART 1
var count = 0
for id in ids
{
    //id is a dictionary
    if ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"].allSatisfy(id.keys.contains)
    {
//        print("\(id) is valid")
      count += 1
    }
}

print(count)

//print(ids)
// PART 2
var count2 = 0
for id in ids
{
    var isValid = true
    let byr = Int(id["byr"] ?? "0") ?? 0
    let iyr = Int(id["iyr"] ?? "0") ?? 0
    let eyr = Int(id["eyr"] ?? "0") ?? 0
    let height = id["hgt"] ?? "no height"
    let hcl = id["hcl"] ?? "no HCL"
    let eyeColor = id["ecl"] ?? "no ECL"
    let passID = id["pid"] ?? "-1"
    
//    print(id)
//    print(eyeColor)
//    print(passID)
    if passID.count == 9
    {
        let passIDNum = Int(passID) ?? -1
        if passIDNum < 0 || passIDNum > 999999999
        {
//            print("failed 1")
            isValid = false
        }
    }
    else
    {
//        print("failed 2")
        isValid = false
    }
    
    
    if !(eyeColor == "amb" || eyeColor == "blu" || eyeColor == "brn" || eyeColor == "gry" || eyeColor == "grn" || eyeColor == "hzl" || eyeColor == "oth")
    {
//        print("failed 3")
        isValid = false
    }
    
//    print("\(byr), \(iyr), \(eyr)")
    
    if hcl.count == 7
    {
        let first = hcl[hcl.startIndex]
//        print(first)
        if first != "#"
        {
//            print("failed 4")
            isValid = false
        }
        let chars = CharacterSet(charactersIn: "0123456789abcdef")
        
        // count valid chars
        var validChars = 0
        for char in hcl
        {
            if let range = String(char).rangeOfCharacter(from: chars)
            {
                validChars += 1
            }
        }
//        print(validChars)
        if validChars != 6
        {
//            print("failed 5")
            isValid = false
        }
    }
    else {
//        print("failed 6")
        isValid = false
    }
    
    
    // figure out height...
    if byr < 1920 || byr > 2002 {
//        print("failed 7")
        isValid = false
    }
    if iyr < 2010 || iyr > 2020 {
//        print("failed 8")
        isValid = false
    }
    if eyr < 2020 || eyr > 2030 {
//        print("failed 9")
        isValid = false
    }
    
    // height will contain "cm" or "in"
    if let range = height.range(of: "cm")
    {
        let value = Int(height[height.startIndex..<range.lowerBound]) ?? 0
//        print("\(value) cm")
        if value < 150 || value > 193
        {
//            print("failed 10")
            isValid = false
        }
    }

    if let range = height.range(of: "in")
    {
        let value = Int(height[height.startIndex..<range.lowerBound]) ?? 0
//        print("\(value) in")
        if value < 59 || value > 76
        {
//            print("failed 11")
            isValid = false
        }
    }
    
    if !(height.contains("cm") || height.contains("in"))
    {
        isValid = false
    }
    
    if isValid
    {
        count2 += 1
    }

}

print(count2)



