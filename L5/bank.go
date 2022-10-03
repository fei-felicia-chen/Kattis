// https://open.kattis.com/problems/bank
package main

import "fmt"


func main() {
    var N int
    var T int
    var cash int
    var time int
    var q [47]int
    fmt.Scan(&N, &T);
    for i := 0; i < N; i++ {
        fmt.Scan(&cash, &time);
        if q[time] == 0 {
            q[time] = cash;
        } else {
            for j := time; j >= 0; j-- {
                if (q[j] < cash) {
                    q[j], cash = cash, q[j]
                }
            }
        }
    }
    sum := 0;
    for i := 0; i < T; i++ {
        sum += q[i];
    }
    fmt.Printf("%v", sum)
}