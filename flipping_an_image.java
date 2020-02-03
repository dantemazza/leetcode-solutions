class Solution {
    public int[][] flipAndInvertImage(int[][] A) {
        int B[][] = new int[A.length][A.length];
        
        for(int a = A.length - 1; a>=0; a--){
            for(int b = A.length - 1; b>=0; b--){
                if(A[b][a] == 0) B[b][A.length - 1 - a] = 1;
                else B[b][A.length - 1 - a] = 0;
            }}
        return B;
    }}
