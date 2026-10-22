class Solution {
    public int missingNumber(int[] nums) {
        int xor = 0;
        int ans = 0;

        for (int i = 0; i <= nums.length; i++){
            ans ^= i;
        } for (int i = 0; i < nums.length; i++){
            xor ^= nums[i];
        }
           
        return (ans ^ xor);
    }
}