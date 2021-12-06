import java.util.*;
import java.io.*;

public class Day05 {
    public static void main(String[] args) throws IOException 
    {
        Scanner scan = new Scanner(new File("2021/Day05-Java/data.txt"));

        ArrayList<Line> lines = new ArrayList<Line>();
        while (scan.hasNext())
        {
            String next = scan.nextLine();
            String nextFormatted = next.replaceAll(" -> ", ",");
            String[] nextArray = nextFormatted.split(",");
            int x1 = Integer.parseInt(nextArray[0]);
            int y1 = Integer.parseInt(nextArray[1]);
            int x2 = Integer.parseInt(nextArray[2]);
            int y2 = Integer.parseInt(nextArray[3]);
            lines.add(new Line(x1, y1, x2, y2));
            
        }
        
        int part1Answer = part1(lines);
        System.out.println("Part1 answer: "+part1Answer);
        int part2Answer = part2(lines);
        System.out.println("Part2 answer: "+part2Answer);


    }

    public static int part1(ArrayList<Line> lines)
    {
        int[][] grid = new int[1000][1000];

        for(Line l: lines)
        {
            if (l.x1 == l.x2)
            {
                // we have a vertical line, x does not change
                for (int i = Math.min(l.y1,l.y2); i <= Math.max(l.y1,l.y2); i++)
                {
                    grid[i][l.x1] += 1;
                }

            }
            else if (l.y1 == l.y2)
            {
                // we have a horizontal line, y does not change
                for (int i = Math.min(l.x1,l.x2); i <= Math.max(l.x1,l.x2); i++)
                {
                    grid[l.y1][i] += 1;
                }
            }
        }

        int count = 0;
        for (int r = 0; r < grid.length; r ++)
        {
            for (int c = 0; c < grid[r].length; c++)
            {
                if (grid[r][c] > 1)
                    count++;
            }
        }
        return count;
    }

    public static int part2(ArrayList<Line> lines)
    {
        int[][] grid = new int[1000][1000];

        for(Line l: lines)
        {
            if (l.x1 == l.x2)
            {
                // we have a vertical line, x does not change
                for (int i = Math.min(l.y1,l.y2); i <= Math.max(l.y1,l.y2); i++)
                {
                    grid[i][l.x1] += 1;
                }

            }
            else if (l.y1 == l.y2)
            {
                // we have a horizontal line, y does not change
                for (int i = Math.min(l.x1,l.x2); i <= Math.max(l.x1,l.x2); i++)
                {
                    grid[l.y1][i] += 1;
                }
            }
            else {
                // we have a diagonal line... find the slope and see if it is -1 or 1
                int top = l.y1 - l.y2;
                int bottom = l.x1 - l.x2;
                int slope = top / bottom;

                if (slope == -1)
                {
                    // start at lowest left. remember that grid's bottom right is +,+ 
                    int amt = Math.abs(top); // figure out how many times to repeat.
                    if (l.x1 < l.x2)
                    {
                        // start at x1, y1
                        for(int i = 0; i <= amt; i++)
                            grid[l.y1-i][l.x1+i]++;
                    }
                    else 
                    {
                        // start at x2, y2
                        for(int i = 0; i <= amt; i++)
                            grid[l.y2-i][l.x2+i]++;
                    }
                }
                else // slope is 1
                {
                    // start at highest left. remember that grid's bottom right is +,+ 
                    int amt = Math.abs(top); // figure out how many times to repeat.
                    if (l.x1 < l.x2)
                    {
                        // start at x1, y1
                        for(int i = 0; i <= amt; i++)
                            grid[l.y1+i][l.x1+i]++;
                    }
                    else 
                    {
                        // start at x2, y2
                        for(int i = 0; i <= amt; i++)
                            grid[l.y2+i][l.x2+i]++;
                    }
                }
            }
        }

        int count = 0;
        for (int r = 0; r < grid.length; r ++)
        {
            for (int c = 0; c < grid[r].length; c++)
            {
                if (grid[r][c] > 1)
                    count++;
            }
        }
        return count;
    }
}
