package main

import "fmt"

func hasKey(hashmap map[int]int, key int) bool {
	_, ok := hashmap[key]
	return ok
}

func twoSum(nums []int, target int) []int {
	hashmap := make(map[int]int)
	var anotherNum int
	for i, v := range nums {
		anotherNum = target - v
		if hasKey(hashmap, anotherNum) {
			return []int{hashmap[anotherNum], i}
		}
		hashmap[v] = i
	}
	return []int{0, 0}
}

func main() {
	fmt.Println(twoSum([]int{2, 7, 11, 15}, 9))
}
