// https://open.kattis.com/problems/doorman
package main

import (
	"fmt"
)

type Node struct {
	prev *Node
	next *Node
	data string
}

type List struct {
	head *Node
	tail *Node
}

func (node *Node) GetData() string {
	return node.data
}

func (club *List) Append(data string) {		// append to last
	human := &Node{
		data: data,
	}
	if club.head == nil {
		club.head = human
		club.tail = human
	} else {
		club.tail.next = human
		tmp := club.tail
		club.tail = human
		club.tail.prev = tmp
		club.tail.next = nil
	}
}

func (club *List) RemoveFirst() {
	 if club.head.next == nil {				// 1 node
		club.head = nil
		club.tail = nil
	} else if club.head.next.next == nil {	// 2 nodes
		club.tail = club.head.next
		club.head = club.head.next
	} else {
		club.head = club.head.next
		club.head.next.prev = nil
	}
}

func (club *List) HasSecond() bool {			// check if has at least 2 nodes
	if club.head == nil || club.head.next == nil {
		return false
	}
	return true
}

func (club *List) RemoveSecond() {
	if club.head.next.next != nil {
		club.head.next = club.head.next.next // first is now pointed to third instead of second
		club.head.next.next.prev = club.head.next.next
	} else {
		club.head.next = nil				// nothing to point anymore
		club.tail = club.head
	}
}

func (club *List) Display() {
	if club.head == nil {
		fmt.Println("( )")
	} else {
		return_list := club.head
		toReturn := ""
		for return_list.next != nil {
			toReturn += "(" + return_list.data + ") -> "
			return_list = return_list.next
		}
		toReturn += "(" + return_list.data + ")"
		fmt.Println(toReturn)
	}
}

func Abs(n int) int {
	if n > 0 {
		return n
	} else {
		return -n
	}
}

func main() {
	var club List
	var smart int
	var queue string

	fmt.Scan(&smart)
	fmt.Scan(&queue)
	for _, human := range queue {
		club.Append(string(human))
	}
	diff := 0
	entered := 0
	for Abs(diff) <= smart {
		if club.head == nil { 		// club is empty
			break
		}
		if Abs(diff) < smart {
			entered++
			if club.head.GetData() == "M" {
				diff++
			} else {
				diff--
			}
			club.RemoveFirst()
		} else {
			if diff > 0 {			// too many men
				if club.head.GetData() == "W" {
					diff--
					entered++
					club.RemoveFirst()
				} else if club.head.next.GetData() == "W" {
					diff--
					entered++
					club.RemoveSecond()
				} else {
					break
				}
			} else {				// too many women
				if club.head.GetData() == "M" {
					diff++
					entered++
					club.RemoveFirst()
				} else if club.head.next.GetData() == "M" {
					diff++
					entered++
					club.RemoveSecond()
				} else {
					break
				}
			}
		}
	}
	fmt.Print(entered)
}