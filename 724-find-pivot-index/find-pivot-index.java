class Solution {
    public int pivotIndex(int[] nums) {
        int totalsome = 0;
        for (int i = 0; i < nums.length; i++){
            totalsome += nums[i];
        }
        
        int leftside = 0;
        for (int i = 0; i < nums.length; i++){
            int rightside = totalsome - leftside - nums[i];
            
            if (leftside == rightside) {
                return i;
            }
            
            leftside += nums[i];
        }
        
        return -1;
    }
}