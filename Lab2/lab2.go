package main

import (
	"fmt"
	"log"
	"regexp"
	"strconv"
)

func main() {
	symbolCode := make([]int, 7)
	{
		var buffString string
		fmt.Print("Введите 7-ми символьный код: ")
		_, err := fmt.Scanf("%s", &buffString)
		match, _ := regexp.Match("^[0-1]+$", []byte(buffString))
		if err != nil || len(buffString) != 7 || !match {
			log.Fatalln("неправильный формат ввода -> " + buffString)
		}
		for i, v := range buffString {
			symbolCode[i], _ = strconv.Atoi(string(v))
		}
	}
	bitmap := map[int]string{
		0: "r1",
		1: "r2",
		2: "i1",
		3: "r3",
		4: "i2",
		5: "i3",
		6: "i4"}
	var s1, s2, s3 int
	s1 = symbolCode[0] ^ symbolCode[2] ^ symbolCode[4] ^ symbolCode[6]
	s2 = symbolCode[1] ^ symbolCode[2] ^ symbolCode[5] ^ symbolCode[6]
	s3 = symbolCode[3] ^ symbolCode[4] ^ symbolCode[5] ^ symbolCode[6]
	binConvertedToInt, err := strconv.ParseInt(fmt.Sprintf("%d%d%d", s3, s2, s1), 2, 8)
	if err != nil {
		log.Fatalln("unable to convert bin to int")
	}
	if binConvertedToInt == 0 {
		fmt.Println("Ошибок не обнаружено")
		return
	}
	fmt.Printf("Ошибка в бите с номером %d (%s)\n", binConvertedToInt, bitmap[int(binConvertedToInt-1)])
	if symbolCode[int(binConvertedToInt-1)] == 0 {
		symbolCode[int(binConvertedToInt-1)] = 1
	} else {
		symbolCode[int(binConvertedToInt-1)] = 0
	}
	fmt.Print("Правильное сообщение: ")
	for _, v := range symbolCode {
		fmt.Printf("%d", v)
	}
}
