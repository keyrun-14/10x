from array import array


arr=list(map(int,input().split()))
maxx=arr[0]
for i in arr:
    if i%3==0:
        if i>maxx:
            maxx=i
print(maxx)


# public static int largest(int[] arr) {
#     int largest = Integer.MIN_VALUE;
#     for (int i : arr)
#         if (i > largest)
#             largest = i;
#     return largest;
# }

# public int Largest( int[] array )
# {
#   if ( array == null || array.length == 0 ) return -1; // null or empty

#   int largest = 0;
#   for ( int i = 1; i < array.length; i++ )
#   {
#     if( array[i]%3==0){
#            if ( array[i] > array[largest] ) largest = i;
#     }
     
#   }
#   return largest; // position of the first largest found
# }

# public class largestElement {
#     // grepper largest element in array java
#     public static int largest(int[] arr) {
#         int largest = Integer.MIN_VALUE;
#         for (int i : arr)
#         {
#             if( i%3==0){
#              if (i > largest)
#                 largest = i;
#             }
#         }
#         return largest;
#     }
#     // end grepper
#     public static void main(String[] args) {
#         int[] arr = { 5, 1, 2, 9, 6, 4, 8, 7, 1, 3 };
#         System.out.println(largest(arr));
#     }
# }