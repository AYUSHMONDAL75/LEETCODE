/**
 * @param {number} x
 * @return {number}
 */
var sumOfTheDigitsOfHarshadNumber = function(x) {
    let sum = 0;
    let num = x;
    while(x > 0){
        let rem = x % 10;
        sum += rem;
        x = Math.floor(x / 10);
    }
    if(num % sum == 0){
        return sum;
    }else{
        return -1;
    }
};