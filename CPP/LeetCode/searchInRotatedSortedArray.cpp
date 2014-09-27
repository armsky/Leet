/*
 * Suppose a sorted array is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.
*/


class Solution {
public:
    int search(int A[], int n, int target) {
        int left = 0;
        int right = n-1;
        int mid;
        while (left <= right){
          mid = (right + left) / 2;
          if (A[mid] == target){
            return mid;
          }else if (A[mid] >= A[left]){
            //Biggest number in right side
            if (A[left] <= target && target < A[mid]){
              //search left wing
              right = mid - 1;
            }else{
              //search right wing
              left = mid + 1;
            }
          }else{
            //Biggest number in left side
            if (A[mid] < target && target <= A[right])
              //search right wing
              left = mid + 1;
            else
              //search left wing
              right = mid -1;
          }
        }
        return -1;
    }
};
