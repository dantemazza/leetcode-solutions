class Solution {
    public int searchInsert(int[] nums, int target) {
        int a = 0; 
        int c = nums.length-1;
        int b;
        
        if(nums.length == 0) return 0;
        if(nums.length == 1){
            return nums[0] < target ? 1 : 0;
        }
        if(target> nums[nums.length-1]) return nums.length;
        if(target == nums[nums.length-1]) return nums.length-1;
        if(target <= nums[0]) return 0;
        

        if(nums.length == 2){
            if(nums[0] == target) return 0;
            if(nums[1] == target) return 1;
        }
        
        while(a<c){
            b = (a+c)/2;
            if(nums[b] > target) c = b;
            else if(nums[b] < target) a = b;
            else return b;
            b = (a+c)/2;
            
            if(c-a == 1) {
                if(nums[c] != target && nums[a] != target)
                return c;
            }
        }
        return 0;
    }
}
