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
