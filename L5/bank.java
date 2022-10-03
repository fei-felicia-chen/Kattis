// https://open.kattis.com/problems/bank
package L5;

import java.util.Scanner;
import java.util.stream.IntStream;

public class bank {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int T = sc.nextInt();
        int[] q = new int[T];
        for (int i = 0; i < N; i++) {
            int cash = sc.nextInt();
            int time = sc.nextInt();
            if (q[time] == 0)
                q[time] = cash;
            else {
                for (int j = time; j >= 0; j--) {
                    if (q[j] < cash) {
                        int tmp = q[j];
                        q[j] = cash;
                        cash = tmp;
                    }
                }
            }
        }
        System.out.println(IntStream.of(q).sum());
        sc.close();
    }
}