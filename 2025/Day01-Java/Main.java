// Advent of Code 2025 Day 01
// https://adventofcode.com/2025/day/1


import java.util.*;
import java.io.*;


class Main {
    public static void main(String[] args) throws IOException {
        File inputFile = new File("/Users/cwalter/Desktop/AdventOfCode/2025/Day01-Java/data.txt");
        Scanner scanner = new Scanner(inputFile);

        ArrayList<String> allLines = new ArrayList<String>();
        
        while (scanner.hasNextLine()) {
            String line = scanner.nextLine();
            allLines.add(line);
        }

        int val = 50; // start at 50

        int zeroCount = 0;
        int zeroCount2 = 0;
        // Process the input lines as needed
        for (String line : allLines) {
            if (line.substring(0,1).equals("L")) {
                // System.out.println(line.substring(1));
                int move = Integer.parseInt(line.substring(1));
                //move left 1 step at a time and make sure val is always between 0 and 99
                while (move > 0) {
                    val -= 1;
                    move--;
                    if (val == 0) {
                        zeroCount2 += 1;
                    } else if (val == -1) {
                        val = 99;
                    } else if (val == 100) {
                        val = 0;
                        zeroCount2 += 1;
                    }
                }
                 

            } else if (line.substring(0,1).equals("R")) {
                int move = Integer.parseInt(line.substring(1));
                //move right 1 step at a time and make sure val is always between 0 and 99
                while (move > 0) {
                    val += 1;
                    move--;
                    if (val == 0) {
                        zeroCount2 += 1;
                    } else if (val == -1) {
                        val = 99;
                    } else if (val == 100) {
                        val = 0;
                        zeroCount2 += 1;
                    }
                }


            }
            // make sure val is between 0 and 99 all the time
            while (val < 0){
                val += 100;
            }



            val %= 100;

            if (val == 0) {
                zeroCount += 1;
            }
            System.out.println(line + " val is at: " + val +  " zero count is " + zeroCount2);

        }

        System.out.println("Part 1: " + zeroCount);
        System.out.println("Part 2: " + (zeroCount2));


        scanner.close();
    }


}