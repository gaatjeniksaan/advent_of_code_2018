package main

import (
	"fmt"
	"io/ioutil"
	"strconv"
	"strings"
)

type claim struct {
	id     string
	left   int
	top    int
	width  int
	length int
}

func main() {
	input, _ := ioutil.ReadFile("./data.txt")
	tmp := string(input)

	var replacer = strings.NewReplacer("#", "", "@", "", ",", " ", ":", "", "x", " ")
	tmp = replacer.Replace(tmp)
	tmp = strings.Replace(tmp, "  ", " ", -1)
	data := strings.Split(tmp, "\n")
	data = data[:len(data)-1] // Remove annoying last entry

	var claims []claim
	for _, val := range data {
		item := strings.Split(val, " ")
		l, _ := strconv.Atoi(item[1])
		t, _ := strconv.Atoi(item[2])
		w, _ := strconv.Atoi(item[3])
		lng, _ := strconv.Atoi(item[4])
		claims = append(claims, claim{item[0], l, t, w, lng})
	}

	coords := make(map[string][]string)
	for _, c := range claims {
		// Loop over all coordinates of c
		for i := 0; i < c.length; i++ {
			for j := 0; j < c.width; j++ {
				row := strconv.Itoa(i + c.top)
				col := strconv.Itoa(j + c.left)
				key := row + "-" + col
				coords[key] = append(coords[key], c.id)
			}
		}
	}

	overlap := 0
	for _, v := range coords {
		if len(v) > 1 {
			overlap++
		}
	}
	fmt.Println("Answer 1: ", overlap)

	// Part 2
	// Loop over every id, and check if it appears in a coord array with len > 1, if so, skip, else: print ID
	// Terribly slow this one...
	for _, c := range claims {
		skip := false
		for _, coord := range coords {
			if Contains(coord, c.id) && len(coord) > 1 {
				skip = true
				continue
			}
		}
		if skip == false {
			fmt.Println("Answer part 2: ", c.id)
			break
		}
	}
}

// Contains tells whether a contains x.
func Contains(a []string, x string) bool {
	for _, n := range a {
		if x == n {
			return true
		}
	}
	return false
}
