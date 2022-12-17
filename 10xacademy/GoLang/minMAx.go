package main
import "fmt"
func main(){
   var size int
   fmt.Scanln(&size)
   var first int
   fmt.Scanln(&first)
   min :=first
   max :=first
//    var arr = make([]int, size)
   for i:=0; i<size-1; i++ {
	   var ele int
	   fmt.Scanln(&ele)
	   if ele<min{
		   min=ele
	   }
	   if ele>max{
		   max=ele
	   }
   }
   fmt.Println(max)
   fmt.Println(min)
}