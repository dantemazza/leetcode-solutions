class Solution {
    public String intToRoman(int num) { 
        String finalNum = "";
        int nums[] = new int[13];
        nums[0] = 1000;
        nums[1] = 900;
        nums[2] = 500; 
        nums[3] = 400;  
        nums[4] = 100;
        nums[5] = 90;
        nums[6] = 50;
        nums[7] = 40;
        nums[8] = 10;
        nums[9] = 9;
        nums[10] = 5;
        nums[11] = 4;
        nums[12] = 1;
        
        HashMap<Integer, String> roman = new HashMap<Integer, String>();
        roman.put(1000, "M");
        roman.put(900, "CM");
        roman.put(500, "D");
        roman.put(400, "CD");
        roman.put(100, "C");
        roman.put(90, "XC");
        roman.put(50, "L");
        roman.put(40, "XL");
        roman.put(10, "X");
        roman.put(9, "IX");
        roman.put(5, "V");
        roman.put(4, "IV");
        roman.put(1, "I");
        int a = num;
        for(int k=0; k<13; k++){
            int c = a;
            a %= nums[k];
            if(a == num) continue;
            
            for(int b=0; b<((c-a)/nums[k]); b++){
                finalNum += roman.get(nums[k]);
            }
            
            if(a == 0) return finalNum;
            
        }    
        return finalNum;
    }
    
    
}
