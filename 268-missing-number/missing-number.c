int missingNumber(int* nums, int numsSize) {
    int xor = 0;
        int ans = 0;

        for (int i = 0; i <= numsSize; i++){
            ans ^= i;
        } for (int i = 0; i < numsSize; i++){
            xor ^= nums[i];
        }
           
        return (ans ^ xor);
}