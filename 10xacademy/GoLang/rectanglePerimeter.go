package main
import "fmt"
func main() {
	var first int
	fmt.Scanln(&first)
	var second int
	fmt.Scanln(&second)
	if first > 0 && second > 0 {
		fmt.Println(2*(first + second))
	} else {
		fmt.Println(0)
	}
}
