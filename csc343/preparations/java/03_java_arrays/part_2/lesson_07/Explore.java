import java.util.Arrays;

public class Explore {
    public static void main(String[] args) {
        int[][] scoreBoards = {
            {1,2,4,2,6,5,4},
            {2,3,5,1,1,2,3},
            {4,4,2,1,2,2,1}
        };

        for (int i = 0; i < scoreBoards.length; i++) {
            for (int j = 0; j < scoreBoards[i].length; j++) {
                System.out.println(scoreBoards[i][j]);
            }
        }
    }
}