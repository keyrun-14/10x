package main
import "fmt"
func main() {
	var n int
	fmt.Scanln(&n)
	count := 0
	if n == 1 {
		fmt.Println("False")
	} else {
		for i := 2; i < n; i++ {
			if n%i == 0 {
				count += 1
			}
		}
		if count == 0 {
			fmt.Println("True")
		} else {
			fmt.Println("False")
		}
	}
}
