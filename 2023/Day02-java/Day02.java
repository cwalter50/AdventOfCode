// Advent of Code 2023 Day 02
// https://adventofcode.com/2023/day/2

import java.util.*;
import java.io.*;

public class Day02 {
    public static void main(String[] args) throws IOException {
        // String filePath = "/Users/chris/Library/CloudStorage/GoogleDrive-walt50@gmail.com/My Drive/AdventOfCode/2022/Day03-Java/data.txt";
        String filePath = "/Users/cwalter/Desktop/AdventOfCode/2023/Day02-Java/data.txt";
        File data = new File(filePath);

        Scanner scan = new Scanner(data);
        ArrayList<String> allLines = new ArrayList<String>();

        while (scan.hasNext()) {
            String next = scan.nextLine();
            allLines.add(next);

        }
        System.out.println("The answer to Part 1 is : " + part1(allLines));
        System.out.println("The answer to Part 2 is : " + part2(allLines));

    }

    public static ArrayList<Game> getGames(ArrayList<String> lines) {
        ArrayList<Game> games = new ArrayList<Game>();
        for (String line: lines) {
            String[] parts = line.split(":");
            String idString = parts[0].substring(5);
            int id = Integer.parseInt(idString);
            String[] setsString = parts[1].split(";");
            ArrayList<Set> sets = new ArrayList<Set>();
            for(int i = 0; i < setsString.length; i++)
            {
                sets.add(new Set(setsString[i]));
            }
            Game newGame = new Game(id, sets);
            games.add(newGame); 
        }

        return games;

    }

   

    public static int part1(ArrayList<String> allLines) {
        int count = 0;
        ArrayList<Game> games = getGames(allLines);
        // Red max is 12, green max is 13, blue max is 14, 
        for (Game game: games){
            boolean isGameGood = true;
            for (Set set: game.sets) {
                if (set.red > 12 || set.green > 13 || set.blue > 14)
                    isGameGood = false;
            }
            if (isGameGood)
                count += game.id;
        }
        return count;
    }

    public static int part2(ArrayList<String> allLines) {
        int count = 0;
        ArrayList<Game> games = getGames(allLines);
        for (Game game: games){
            int maxRed = 0;
            int maxGreen = 0;
            int maxBlue = 0;
            for (Set set: game.sets) {
                if (set.red > maxRed)
                    maxRed = set.red;
                if (set.green > maxGreen)
                    maxGreen = set.green;
                if (set.blue > maxBlue)
                    maxBlue = set.blue;
            }
            int gamePower = maxRed * maxGreen * maxBlue;
            count += gamePower;
        }

        return count;
    }
}
