package main

import (
	"fmt"
	"io/ioutil"
	"log"
	"strconv"
	"strings"
)

func main() {
	freq := 0

	input, err := ioutil.ReadFile("./data.txt")
	if err != nil {
		fmt.Println("ERROR ERROR!")
	}
	dataString := strings.Split(string(input), "\n") // every item in slice is of type string
	var data []int

	// Let's convert the string to int once, and re-use in part 1 and part 2 of this exercise
	for index, val := range dataString {
		if len(val) == 0 {
			continue
		}
		item, err := strconv.Atoi(val)
		if err != nil {
			fmt.Println("Problem with converting string to int: ", err, "at index ", index)
		} else {
			data = append(data, item)
		}
	}

	for _, i := range data {
		freq += i
	}
	fmt.Println("Final frequency: ", freq)

	// PART 2
	// Start while loop until frequency found twice
	// Increment value in map with key being current frequency
	// If value == 2 -> print current frequency and panic.
	freqMap := make(map[int]int)
	freqPt2 := 0

	for {
		for _, j := range data {
			freqMap[freqPt2]++

			if freqMap[freqPt2] == 2 {
				fmt.Println("Frequency to pass through twice is: ", freqPt2)
				log.Panic()
			}
			freqPt2 += j
		}
	}
}
