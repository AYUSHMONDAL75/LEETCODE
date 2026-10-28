class Solution {
    public int countDigits(int num) {
        int count = 0;
        int nums = num;
        while(num > 0){
            int rem = num % 10;
            if(nums % rem == 0){
                count += 1;
            }
            num /= 10;
        }
        return count;
    }
}