// https://adventofcode.com/2021/day/9

import java.io.*;
import java.util.*;

class Main 
{
  public static void main(String[] args) throws IOException
  {
    Scanner scan = new Scanner(new File("data.txt"));

    int[][] grid = new int[100][100];
    int row = 0;
    while (scan.hasNext())
    {
      String[] line = scan.nextLine().split("");
      // System.out.println(line);
      // printList(line);
      for (int i = 0; i < line.length; i++)
      {
        grid[row][i] = Integer.parseInt(line[i]);
      }

      row++;
    }

    // printGrid(grid);

    int part1Answer = part1(grid);
    System.out.println("Part1 Answer: "+part1Answer);

    
  }


  public static int part1(int[][] grid)
  {
    ArrayList <Integer> lowPoints = new ArrayList<Integer>();

    for (int r = 0; r < grid.length; r++)
    {
      for(int c = 0; c < grid[r].length; c++)
      {
        int cur = grid[r][c];

        // check left, right, up, down
        boolean isLow = true;
        if (c > 0 && grid[r][c-1] <= cur) // left
          isLow = false;
        if (c < grid[r].length-1 && grid[r][c+1] <= cur) // right
          isLow = false;
        if (r > 0 && grid[r-1][c] <= cur) // up
          isLow = false;
        if (r < grid.length-1 && grid[r+1][c] <= cur) // down
          isLow = false;

        if (isLow == true)
          lowPoints.add(cur);
      }
    }
    int sum = 0;
    for (Integer num: lowPoints)
      sum += num+1;
    return sum;
  }

  public static void printGrid(int[][] grid)
  {
    for(int r = 0; r < grid.length; r++)
      printList(grid[r]);
        
  }

  public static void printList(int[] list)
  {
    String result = "";
    for(int i: list)
      result += i + " ";
    
    System.out.println(result);
  }
}
