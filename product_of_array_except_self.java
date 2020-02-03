class Solution {
    public int[] productExceptSelf(int[] nums) {
        int left[] = new int[nums.length];
        int leftProduct = 1; 
        int rightProduct = 1; 
        left[0] = 1;
        for(int i=1; i<nums.length; ++i){
            leftProduct *= nums[i-1];
            left[i] = leftProduct;    
        }
        for(int j=nums.length-2; j>=0; --j){
            rightProduct *= nums[j+1];
            left[j] *= rightProduct; 
        }
        return left;       
    }
}
