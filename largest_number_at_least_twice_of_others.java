class Solution {
    public int dominantIndex(int[] nums) {
        int largest = 0;
        
        for(int i=0; i<nums.length; i++){
            if(nums[i] > nums[largest]) largest = i; 
        }
        
        for(int i=0; i<nums.length; i++){
            if((i == largest) || nums[i] == 0) continue;
            if(nums[largest] / nums[i] < 2) return -1;
        }
        return largest;
    }
}
