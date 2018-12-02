package main

import (
	"fmt"
	"io/ioutil"
	"strings"
)

func main() {
	input, err := ioutil.ReadFile("./data.txt")
	if err != nil {
		fmt.Println("ERROR ERROR!")
	}
	data := strings.Split(string(input), "\n")

	// Part 1
	var twos bool
	var threes bool
	twosTotal := 0
	threesTotal := 0

	for _, val := range data {
		twos, threes = getDuplicates(val)
		if twos == true {
			twosTotal++
		}
		if threes == true {
			threesTotal++
		}
	}

	fmt.Println("Answer part 1: ", twosTotal*threesTotal)
	fmt.Println("Answer part 2: ", getAlmostIdentical(data))
}

func getDuplicates(seq string) (bool, bool) {
	dict := make(map[int]int)
	// Populate dictionary with occurences
	for _, char := range seq {
		dict[int(char)]++
	}

	v := make([]int, 0, len(dict))
	for _, value := range dict {
		v = append(v, value)
	}

	// Now loop over the slice with counts to see if it matches 2 or 3 and set the flag appropriately
	twos := false
	threes := false
	for _, count := range v {
		if count == 2 {
			twos = true
		}
		if count == 3 {
			threes = true
		}

	}
	return twos, threes
}

func getAlmostIdentical(data []string) string {
	var diff int
	var result string
	for _, s1 := range data {
		for _, s2 := range data {
			if len(s1) != 26 || len(s2) != 26 {
				continue
			}

			diff = 0
			result = ""
			for index := range s1 {
				if s1[index] != s2[index] {
					diff++
				} else {
					result += string(s1[index])
				}
			}
			if diff == 1 {
				return result
			}
		}
	}
	return "None Found"
}
