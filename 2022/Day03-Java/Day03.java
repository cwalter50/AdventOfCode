// Advent of Code 2022 Day 03
// https://adventofcode.com/2022/day/3

import java.util.*;
import java.io.*;

public class Day03 {
    public static void main(String[] args) throws IOException {

        String filePath = "/Users/chris/Library/CloudStorage/GoogleDrive-walt50@gmail.com/My Drive/AdventOfCode/2022/Day03-Java/data.txt";
        File data = new File(filePath);

        // File data = new File("2022/Day03-Java/data.txt");

        Scanner scan = new Scanner(data);
        ArrayList<String> allLines = new ArrayList<String>();

        while (scan.hasNext()) {
            String next = scan.nextLine();
            allLines.add(next);

        }

        System.out.println("The answer to Part 1 is : " + part1(allLines));
        System.out.println("The answer to Part 2 is : " + part2(allLines));

    }

    public static String getCommonLetter(String line) {

        String first = line.substring(0, line.length() / 2);
        String second = line.substring(line.length() / 2);

        for (int i = 0; i < first.length(); i++) {
            String current = first.substring(i, i + 1);
            if (second.contains(current))
                return current;
        }
        return "a";
    }

    public static int getPriority(String letter) {
        char a = letter.charAt(0);
        int num = 0;
        // System.out.println("Letter is " + a + ", " + "value is " + (int) a);
        if ((int) a >= 97)
            num = (int) a - 96;
        else
            num = (int) a - 38;
        return num;
    }

    public static String findCommonLetter(String a, String b, String c) {
        for (int i = 0; i < a.length(); i++) {
            String letter = a.substring(i, i + 1);
            if (b.contains(letter) && c.contains(letter))
                return letter;
        }
        return "a";
    }

    public static int part1(ArrayList<String> allLines) {
        int count = 0;
        for (String line : allLines) {
            String commonLetter = getCommonLetter(line);
            // System.out.println(commonLetter);
            int priority = getPriority(commonLetter);
            // System.out.println(priority);
            count += priority;
        }
        return count;
    }

    public static int part2(ArrayList<String> allLines) {

        int count = 0;

        for (int i = 0; i < allLines.size(); i += 3) {
            String first = allLines.get(i);
            String second = allLines.get(i + 1);
            String third = allLines.get(i + 2);
            String commonLetter = findCommonLetter(first, second, third);
            // System.out.println("Found Common Letter: " + commonLetter);
            int priority = getPriority(commonLetter);
            count += priority;
        }
        return count;
    }
}