
/**
 * @param {number[]} nums
 * @return {number}
 */
var missingNumber = function(nums) {
    let xor = 0;
    let ans = 0;

    for (let i = 0; i <= nums.length; i++) {
        ans ^= i;
    }

    for (let i = 0; i < nums.length; i++) {
        xor ^= nums[i];
    }

    return ans ^ xor;
};
