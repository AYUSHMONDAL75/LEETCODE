/**
 * @param {number} num
 * @return {number}
 */
var countDigits = function(num) {
    let count = 0;
        let nums = num;
        while(num > 0){
            let rem = num % 10;
            if(nums % rem == 0){
                count += 1;
            }
            num = Math.floor(num / 10);
        }
        return count;
};