// https://open.kattis.com/problems/nikola
package main

import (
	"fmt"
	"math"
)

var n int
var fees []int
var arr [1001][1001]int

func Min(a int, b int) int {
    if a < b {
		return a
	} else {
		return b
	}
}

func solve(x int, y int) int {
	if (n-1 == x) {
		return fees[x]
	} else if (x >= n || x < 0) {
		return math.MaxInt32
	} else if (arr[x][y] != 0) {
		return arr[x][y]
	} else {
		arr[x][y] = Min(solve(x+y+1, y+1), solve(x-y, y)) + fees[x]
		return arr[x][y]
	}
}

func main() {
	fmt.Scan(&n)
	for i := 0; i < n; i++ {
		var fee int
		fmt.Scan(&fee)
		fees = append(fees, fee)
	}
	fmt.Print(solve(1, 1))
}
