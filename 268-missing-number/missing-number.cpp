class Solution {
public:
    int missingNumber(vector<int>& nums) {
        int Xor = 0;
        int ans = 0;

        for (int i = 0; i <= nums.size(); i++){
            ans ^= i;
        } for (int i = 0; i < nums.size(); i++){
            Xor ^= nums[i];
        }
           
        return (ans ^ Xor);
    }
};