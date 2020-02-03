class Solution {
    public int[] dailyTemperatures(int[] T) {
        int days[] = new int[T.length];
        for(int i=0; i<T.length-1; i++){
            int a = i+1;
            while(!(a == T.length)){
               if(T[a] > T[i]) break;
               a++; 
            }
            
           days[i] = (a == T.length) ? 0 : (a-i);
        }
        
        days[T.length-1] = 0;
        return days;
    }
    
}
