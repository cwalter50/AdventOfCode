import UIKit
import Foundation

/*
 About the challenge: Advent of Code Day 8
 https://adventofcode.com/2020/day/8
 */

var myStrings = [String]()
if let path = Bundle.main.path(forResource: "data", ofType: "txt") {
    do {
        let data = try String(contentsOfFile: path, encoding: .utf8)
        // Split based on characters.
        myStrings = data.components(separatedBy: .newlines)
    
    } catch {
        print(error)
    }
}

myStrings.removeLast()
//print(myStrings)


class Instruction: CustomStringConvertible
{
    var name: String
    var value: Int
    var hasRun: Bool
    
    var description: String {
        return "name: \(name), value: \(value)"
    }
    
    init (original: String)
    {
        let components = original.components(separatedBy: " ")
        name = components[0]
        let valueString = components[1]
        if valueString.hasPrefix("+")
        {
            value = Int(valueString.dropFirst()) ?? 0
        }
        else if valueString.hasPrefix("-")
        {
            value = Int(valueString.dropFirst()) ?? 0
            value = value * -1
        }
        else
        {
            value = 0
        }
        
        hasRun = false
        
    }
}

var instructions = [Instruction]()
for item in myStrings
{
    let newInstruction = Instruction(original: item)
//    print(newInstruction.description)
    instructions.append(newInstruction)
}


// instructions have everything needed

func runProgram(values: [Instruction])
{
    var counter = 0
    var accumulator = 0
    var current = values[counter]

    while (counter < values.count && values[counter].hasRun == false)
    {
        current = values[counter]
            
        if current.name == "acc"
        {
            accumulator += current.value
            counter += 1
        }
        else if current.name == "jmp"
        {
            counter += current.value
        }
        else // name is nop
        {
            counter += 1
        }
        current.hasRun = true
        if counter >= values.count
        {
            print("FOUND Correct change: \(accumulator)")
        }

    }
    
    print(accumulator)
}

runProgram(values: instructions)


func runSimulation()
{
    // run the program over and over again, making only one change in instructions with each simulation. it will print all of the changes.... including the winning change
    

    for i in 0..<instructions.count
    {
        // make a copy of the instructions each time we run the simulation
        if instructions[instructions.count - 1 - i].name != "acc"
        {
            var changedInstruction = [Instruction]()
            for item in myStrings
            {
                let newInstruction = Instruction(original: item)
            //    print(newInstruction.description)
                changedInstruction.append(newInstruction)
            }
    //        changedInstruction = instructions
            
            if changedInstruction[instructions.count - 1 - i].name == "jmp"
            {
                changedInstruction[instructions.count - 1 - i].name = "nop"
            }
            else if changedInstruction[instructions.count - 1 - i].name == "nop"
            {
                changedInstruction[instructions.count - 1 - i].name = "jmp"
            }
            if (changedInstruction[instructions.count - 1 - i].name != "acc")
            {
                runProgram(values: changedInstruction)
            }
        }

        
    }
}

runSimulation()



