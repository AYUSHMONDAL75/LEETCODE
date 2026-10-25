import java.util.*;
class Solution {
    public int digitFrequencyScore(int n) {

        HashMap<Integer, Integer> mp = new HashMap<>();
        
        while(n > 0){
            int d = n % 10;
            mp.put(d, mp.getOrDefault(d, 0) + 1);
            n /= 10;
        }
        int ans = 0;

        for (int d : mp.keySet()){
            ans += d * mp.get(d);
        }
        return ans;
    }
}
