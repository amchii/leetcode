package main

import "fmt"

type ListNode struct {
	Val  int
	Next *ListNode
}

func addAndCarry(x, y, carry int) (int, int) {
	sum := x + y + carry
	if sum >= 10 {
		return sum % 10, sum / 10
	}
	return sum, 0
}

func addTwoNumbers(l1 *ListNode, l2 *ListNode) *ListNode {
	var r = &ListNode{}
	var head = r
	var carry, x, y, e int
	for l1 != nil || l2 != nil {
		//fmt.Println(l1)
		//fmt.Println(l2)
		if l1 == nil {
			x = 0
			y = l2.Val
		} else {
			x = l1.Val
			if l2 == nil {
				y = 0
			} else {
				y = l2.Val
			}
		}
		e, carry = addAndCarry(x, y, carry)
		head.Next = &ListNode{Val: e}
		if l1 != nil {
			l1 = l1.Next
		}
		if l2 != nil {
			l2 = l2.Next
		}
		head = head.Next
	}
	if carry != 0 {
		head.Next = &ListNode{Val: carry}
	}
	return r.Next
}

func main() {
	l1 := &ListNode{
		Val: 3,
		Next: &ListNode{
			Val: 5,
			Next: &ListNode{
				Val:  6,
				Next: nil,
			},
		},
	}
	l2 := &ListNode{
		Val: 4,
		Next: &ListNode{
			Val: 5,
			Next: &ListNode{
				Val: 7,
				Next: &ListNode{
					Val:  8,
					Next: nil,
				},
			},
		},
	}
	r := addTwoNumbers(l1, l2)
	for r != nil {
		fmt.Println(r.Val)
		r = r.Next
	}

}
