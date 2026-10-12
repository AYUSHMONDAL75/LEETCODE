/**
 * Note: The returned array must be malloced, assume caller calls free().
 */

void merge(int* nums, int left, int mid, int right, int* temp) {
    int i = left, j = mid + 1, k = left;

    while (i <= mid && j <= right) {
        if (nums[i] <= nums[j]) {
            temp[k++] = nums[i++];
        } else {
            temp[k++] = nums[j++];
        }
    }
    while (i <= mid) temp[k++] = nums[i++];
    while (j <= right) temp[k++] = nums[j++];

    for (i = left; i <= right; i++) {
        nums[i] = temp[i];
    }
}

void mergeSort(int* nums, int left, int right, int* temp) {
    if (left < right) {
        int mid = left + (right - left) / 2;
        mergeSort(nums, left, mid, temp);
        mergeSort(nums, mid + 1, right, temp);
        merge(nums, left, mid, right, temp);
    }
}

int* sortArray(int* nums, int numsSize, int* returnSize) {
    int* temp = (int*)malloc(numsSize * sizeof(int));
    mergeSort(nums, 0, numsSize - 1, temp);
    free(temp);

    *returnSize = numsSize;
    return nums;
}