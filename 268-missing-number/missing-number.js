/**
 * @param {number[]} nums
 * @return {number}
 */
var missingNumber = function(nums) {
    let Xor = 0;
    let ans = 0;
    for (let i = 0; i <= nums.length; i++){
        ans ^= i;
    } for (let i = 0; i < nums.length; i++){
        Xor ^= nums[i];
    }
        
    return (ans ^ Xor);
}