// Advent of Code 2021 Day 04
// https://adventofcode.com/2021/day/4

import java.util.*;
import java.io.*;

public class Day04
{
    public static void main(String[] args) throws IOException
    {
        Scanner scan = new Scanner(new File("2021/Day04-Java/data.txt"));
        String allNumsString = scan.nextLine();
        String[] allNumsStringArray = allNumsString.split(",");
        ArrayList<Integer> allNums = new ArrayList<Integer>();

        for (int i = 0; i < allNumsStringArray.length; i ++)
        {
            allNums.add(Integer.parseInt(allNumsStringArray[i]));
        }
        // System.out.println(allNums);

        ArrayList<Board> boards = new ArrayList<Board>();

        while (scan.hasNext())
        {
            // get 25 numbers, to make a board, and keep repeating
            int[][] board = new int[5][5];
            for(int i = 0; i < 25; i++)
            {
                board[i/5][i%5] = scan.nextInt();
            }
            Board b = new Board(board);
            boards.add(b);
        }

        // boards are made and so is the allNums Array. 
        // We are now ready to find the winner
        Board part1 = findWinningBoardPart1(allNums, boards);
        System.out.println();

        Board part2 = findLastWinningBoard(allNums, boards);

        
    }
    public static Board findWinningBoardPart1(ArrayList<Integer> nums, ArrayList<Board> boards)
    {
        ArrayList<Integer> calledNums = new ArrayList<Integer>();

        for (Integer num: nums)
        {
            // add a number
            calledNums.add(num);
            // check each board for a winner
            for (Board b: boards)
            {
                if (b.checkForWinner(calledNums) == true)
                {
                    // we found a winner
                    System.out.println("Winner\n"+b);
                    System.out.println("Winner score: " + b.getScore(calledNums));
                    return b;
                }
            }
        }
        System.out.println("Never found a winner, so we are returning first board");
        return boards.get(0);
    }

    public static Board findLastWinningBoard(ArrayList<Integer> nums, ArrayList<Board> boards)
    {
        ArrayList<Integer> calledNums = new ArrayList<Integer>();

        for (Integer num: nums)
        {
            // add a number to the called numsList
            calledNums.add(num);
            // check each board for a winner and throw out the winners
            for (int i = boards.size()-1; i >= 0; i--)
            {
                Board b = boards.get(i);
                
                if (b.checkForWinner(calledNums) == true)
                {
                    if (boards.size() == 1)
                    {
                        System.out.println("Part2: LastWinner\n"+b);
                        System.out.println("LastWinner score: " + b.getScore(calledNums));
                        return b;
                    }
                    
                    boards.remove(i);
                }
            }
        }
        System.out.println("Never found a winner, so we are returning first board");
        return boards.get(0);
    }
}
