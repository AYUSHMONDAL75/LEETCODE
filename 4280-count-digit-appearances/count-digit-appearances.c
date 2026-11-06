int countDigitOccurrences(int* nums, int numsSize, int digit) {
    int count = 0;
        int num = 0;
        for(int i = 0; i < numsSize; i++){
            while(nums[i] > 0){
                int rem = nums[i] % 10;
                nums[i] /= 10;
                if(rem == digit){
                    count++;
                }
            }
        }
        
        return count;
}