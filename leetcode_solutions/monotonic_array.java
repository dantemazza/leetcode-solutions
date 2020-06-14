class Solution {
    public boolean isMonotonic(int[] A) {
        int b = 0;
        while(b<A.length-1){
            if(A[b] == A[b+1]) b++;
            else{b = (b==0) ? 0 : b--; break;}
        }     
        if(b==A.length-1) return true;
        boolean isDec = A[b+1] < A[b];
        for(int a = b; a<A.length-1; a++) if(isDec && A[a] < A[a+1] || !isDec && A[a] > A[a+1]) return false;
        return true;
    }
}
