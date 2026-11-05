class Solution {
    public int differenceOfSum(int[] nums) {
        int x = 0;
        
        for(int i = 0; i < nums.length; i++){
            x += nums[i];
        }

        int sum = 0;

        for(int i = 0; i < nums.length; i++){
            while (nums[i] > 0){
                int digit = nums[i] % 10;
                sum += digit;
                nums[i] = nums[i] / 10;
            }      
        }
        
        return Math.abs(sum - x);
    }
}