package main
import "fmt"
func main(){
	
	array := make([]int, 0)
	var n int
	fmt.Scanln((&n))
	for i:=0;i<n;i++{
		var ele int 
	fmt.Scanln(&ele)
	array=append(array, ele)
	}
	fmt.Println(array)
	
	
}