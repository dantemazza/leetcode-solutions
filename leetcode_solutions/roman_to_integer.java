class Solution {
    public int romanToInt(String s) {
        int num = 0;
        ArrayList<Integer> nums = new ArrayList<Integer>();
        for(int a = 0; a<s.length(); a++){
            nums.add(this.convert(s.charAt(a)));    
        }
        
        num += nums.get(nums.size()-1);
        for(int b = nums.size()-1; b>0; b--){
            if(nums.get(b) <= nums.get(b-1)){
                num += nums.get(b-1);
            }else if(nums.get(b-1) < nums.get(b)){
              num -= nums.get(b-1);  
            }
        }
        
        
        
        return num;   

    }    
        
    public int convert(char s){
        if(s == 'I') return 1;
        else if(s == 'V') return 5;
        else if(s == 'X') return 10;
        else if(s == 'L') return 50;
        else if(s == 'C') return 100;
        else if(s == 'D') return 500;
        else if(s == 'M') return 1000;    
    return 0;
    }
}  
    
