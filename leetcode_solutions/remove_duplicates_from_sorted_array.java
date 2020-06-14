class Solution {
    public int removeDuplicates(int[] nums) {
        int i=0; 
        int j=0; 
        if(nums.length == 0) return 0;
        if(nums.length == 1) return 1;
        
        if(nums.length == 2){
            if(nums[0] == nums[1]) return 1;
            else return 2;
        }
        
yes:{    while(i < nums.length-1){
            while(nums[i] == nums[i+1]){
                i++;
                if(i>=nums.length-1) break yes;
            }
        nums[j] = nums[i];
            i++;
            j++;
        }}
        
        if(j==0) return 1;
        if(j < 2){ 
            if(nums[i] == nums[j-1]) return 1;
            else{nums[1] = nums[i]; return 2;}
        }
        
        if(nums[i-1] != nums[j-2]){ nums[j] = nums[i]; j++;}
        
        return j;
    }
}
