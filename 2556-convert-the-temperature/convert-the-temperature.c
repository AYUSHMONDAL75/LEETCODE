/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
double* convertTemperature(double celsius, int* returnSize) {
    double kelvin = celsius + 273.15;
    double fahrenheit = (celsius * 9.0 / 5.0) + 32.0;

    double* ans = malloc(2 * sizeof(double));

    ans[0] = kelvin;
    ans[1] = fahrenheit;

    *returnSize = 2;
    return ans;
}