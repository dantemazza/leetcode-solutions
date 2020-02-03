class Solution {
    public int lengthOfLongestSubstring(String s) {
        int length = 0;
        
        for(int i=0; i<s.length(); i++){
            int b = i;
            List<Character> charsTemp = new ArrayList<Character>();
            while(b<s.length()){
                
                if(!charsTemp.contains(s.charAt(b))) charsTemp.add(s.charAt(b));
                else break;
                if(charsTemp.size() > length) length = charsTemp.size();
                b++; 
            }
        }
        
        
        
        
        
        
        
        
        
        
        return length;
    }
}
