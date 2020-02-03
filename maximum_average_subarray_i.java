class Solution {
    public double findMaxAverage(int[] nums, int k) {
        double sum = 0;
        double currMax = 0;
        for(int i=0; i<k; i++){
            sum += nums[i];
        } 
        currMax = sum / k; 
        for(int i=k; i<nums.length; i++){
            sum -= nums[i-k];  
            sum += nums[i];
            currMax = (sum / k > currMax) ? (sum / k) : currMax;
        }
        return currMax;
    }
}
