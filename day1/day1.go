package main

import (
	"fmt"
	"io/ioutil"
	"strconv"
	"strings"
)

func main() {
	freq := 0

	input, err := ioutil.ReadFile("./data.txt")
	if err != nil {
		fmt.Println("ERROR ERROR!")
	}
	strInput := string(input)
	data := strings.Split(strInput, "\n") // every item in slice is of type string

	for index, val := range data {
		i, err := strconv.Atoi(val)
		if err != nil {
			fmt.Println("Problem with converting string to int: ", err, "at index ", index)
		}
		freq += i
	}
	fmt.Println("Final frequency: ", freq)
}
