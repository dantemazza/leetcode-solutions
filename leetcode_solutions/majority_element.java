class Solution {
    public int majorityElement(int[] nums) {
        if(nums.length == 1) return nums[0];
        Arrays.sort(nums);
        int a = 0; int b = 1;
        
        while(true){
         if(nums[a+1] == nums[a]){ 
             b++;
             if(b>nums.length/2) return nums[a];
         }else b = 1;
            
       a++; 
    }
}
}
