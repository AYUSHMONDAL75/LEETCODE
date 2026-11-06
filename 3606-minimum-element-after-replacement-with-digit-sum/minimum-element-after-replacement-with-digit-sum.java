class Solution {
    public int minElement(int[] nums) {
        int[] arr = new int[nums.length];
        for (int i = 0; i < nums.length; i++) {
            int sum = 0;
            int num = nums[i];
            while (num > 0) {
                int rem = num % 10;
                sum += rem;
                num /= 10;
            }
            arr[i] = sum;
        }
        int min = arr[0];
        for (int i = 1; i < arr.length; i++) {
            if (arr[i] < min) {
                min = arr[i];
            }
        }
        return min;
    }
}