import java.util.ArrayList;

public class Board {
    int[][] board = new int[5][5];


    public Board(int[][] b)
    {
        this.board = b;
    }

    /**
     * this will check if board is a winner.
     * @param nums represents the called values in the bingo game
     * @return true if board is a winner, false otherwise
     */
    // 

    public boolean checkForWinner(ArrayList<Integer> nums)
    {
        // check each row and column to see if we have a winner
        if (checkRows(nums) == true || checkColumns(nums) == true)
            return true;
        else
            return false;
       
    }

    /**
     * Will check all the rows if there is a winner
     * @param nums represents the called values in the bingo game
     * @return true if any row wins, false otherwise
     */
    public boolean checkRows(ArrayList<Integer> nums)
    {
        // check each row 
        for (int r = 0; r < board.length; r++)
        {
            boolean isWinner = true;
            for (int c = 0; c < board[r].length; c++)
            {
                if (!nums.contains(board[r][c]))
                    isWinner = false;
            }
            // we checked the entire row. If isWinner is 
            // still true, then we found a winner.
            if (isWinner == true)
                return true;
        }
        // we checked each row and never found a winner. so return false.
        return false;
    }

     /**
     * Will check all the columns if there is a winner
     * @param nums represents the called values in the bingo game
     * @return true if any column wins, false otherwise
     */
    public boolean checkColumns(ArrayList<Integer> nums)
    {
        // check each column 
        for (int c = 0; c < board[0].length; c++)
        {
            boolean isWinner = true;
            for (int r = 0; r < board.length; r++)
            {
                if (!nums.contains(board[r][c]))
                    isWinner = false;
            }
            // we checked the entire column. If isWinner is 
            // still true, then we found a winner.
            if (isWinner == true)
                return true;
        }
        // we checked each column and never found a winner. so return false.
        return false;
    }

    /**
     * Finds the score of the game. 
     * The score is the sum of the numbers that are not called 
     * multiplied by the last number called
     * @param nums represents the called values in the bingo game
     * @return the score
     */
    public int getScore(ArrayList<Integer> nums)
    {
        int score = 0;
        for (int r = 0; r < board.length; r++)
        {
            for (int c = 0; c < board[r].length; c++)
            {
                if (!nums.contains(board[r][c]))
                    score += board[r][c];
            }
        }
        int last = nums.get(nums.size()-1);

        System.out.println("last calledNum: " + last + " score: " + score);
        return score * last;
    }

    public String toString()
    {
        String result = "";
        for (int r = 0; r< board.length; r++)
        {
            for (int c = 0; c < board[r].length; c++)
                result += board[r][c] + " ";
            result += "\n";
        }
        return result;
    }
    
}
