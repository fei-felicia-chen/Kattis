import java.util.Scanner;

public class bachetsgame {
    // https://open.kattis.com/problems/bachetsgame
    
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        while (sc.hasNext()) {
            int n = sc.nextInt();
            int m = sc.nextInt();
            int[] moves = new int[m];
            for (int i = 0; i < m; i++) {
                moves[i] = sc.nextInt();
            }
            boolean[] stan = new boolean[n + 1];
            for (int i = 1; i <= n; i++) {
                for (int j = 0; j < m; j++) {
                    if (i - moves[j] >= 0 && !stan[i - moves[j]]) {
                        stan[i] = true;
                        break;
                    }
                }
            }
            if (stan[n]) {
                System.out.println("Stan wins");
            } else {
                System.out.println("Ollie wins");
            }
        }
        sc.close();
    }
}