bool isPalindrome(int x) {
    long long sum=0;
    int temp = x;
    while(x>0){
        int rem = x % 10;
        sum = sum * 10 + rem;
        x = x / 10;
    }if(temp == sum){
        printf("%d number is pallindrom number",x);
    }else{
        printf("%d is not pallindrome numbner",x);
    }
    return temp == sum;
}