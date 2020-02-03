class Solution {
    public int repeatedNTimes(int[] A) {
       int N = A.length / 2;
       Arrays.sort(A); 
       int j = 1;
       for(int a = 0; a<A.length-1; a++){
          if(A[a] == A[a+1]){
              j++;
              if(j == N) return A[a];
           }else j=1;
       } return 0;
    } 
}
