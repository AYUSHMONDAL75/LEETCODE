int smallestIndex(int* nums, int numsSize) {
    for(int i = 0; i < numsSize; i++){
            int sum = 0;
            while (nums[i] > 0){
                int rem = nums[i] % 10;
                sum += rem;
                nums[i] /= 10;
            }
            if(sum == i){
                return i;
            }
        }
        
        return -1;
}