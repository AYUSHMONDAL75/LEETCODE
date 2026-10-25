import java.util.*;

class Solution {
    public int[] frequencySort(int[] nums) {
        int[] arr = new int[nums.length];
        HashMap<Integer, Integer> mp = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            mp.put(nums[i], mp.getOrDefault(nums[i], 0) + 1);
        }
        Integer[] temp = new Integer[nums.length];
        for (int i = 0; i < nums.length; i++) {
            temp[i] = nums[i];
        }
        Arrays.sort(temp, (a, b) -> {
            if (mp.get(a).equals(mp.get(b))) {
                return b - a;
            }
            return mp.get(a) - mp.get(b);
        });
        for (int i = 0; i < nums.length; i++) {
            arr[i] = temp[i];
        }

        return arr;
    }
}