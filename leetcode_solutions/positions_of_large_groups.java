class Solution {
    public List<List<Integer>> largeGroupPositions(String S) {
        List<List<Integer>> result = new ArrayList<List<Integer>>();
        char[] s = S.toCharArray();
        int startIndex=0;
        for(int a=0; a<S.length()-1; a++){
            if(s[a] != s[a+1]){
                if((a-startIndex)>1){
                    List<Integer> pair = new ArrayList<Integer>();
                    pair.add(startIndex);
                    pair.add(a);
                    result.add(pair);
                }
                
                startIndex = a+1;
            }
        }
        
        if(S.length()-1-startIndex > 1){
            List<Integer> pair = new ArrayList<Integer>();
            pair.add(startIndex);
            pair.add(S.length()-1);
            result.add(pair);
        }
        
      return result;  
    }
}
