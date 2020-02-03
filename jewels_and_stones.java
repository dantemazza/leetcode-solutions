class Solution {
    public int numJewelsInStones(String J, String S) {
        int num = 0;
        char jewels[] = J.toCharArray();
        
        for(int a=0; a<jewels.length; a++){
            for(int b=0; b<S.length(); b++){
                if(S.charAt(b) == jewels[a]) num += 1;
            }
        }
        return num;
    }
}
