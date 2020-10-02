//Here is the source of the problem:
https://code.google.com/codejam/contest/4214486/dashboard#s=p2


// C++ program to find size of minimum possible array after 
// removing elements according to given rules 
#include <bits/stdc++.h> 
using namespace std; 
#define MAX 1000 

// dp[i][j] denotes the minimum number of elements left in 
// the subarray arr[i..j]. 
int dp[MAX][MAX]; 

int minSizeRec(int arr[], int low, int high, int k) 
{ 
	// If already evaluated 
	if (dp[low][high] != -1) 
		return dp[low][high]; 

	// If size of array is less than 3 
	if ( (high-low + 1) < 3) 
		return high-low +1; 

	// Initialize result as the case when first element is 
	// separated (not removed using given rules) 
	int res = 1 + minSizeRec(arr, low+1, high, k); 

	// Now consider all cases when first element forms a triplet 
	// and removed. Check for all possible triplets (low, i, j) 
	for (int i = low+1; i<=high-1; i++) 
	{ 
		for (int j = i+1; j <= high; j++ ) 
		{ 
			// Check if this triplet follows the given rules of 
			// removal. And elements between 'low' and 'i' , and 
			// between 'i' and 'j' can be recursively removed. 
			if (arr[i] == (arr[low] + k) && 
				arr[j] == (arr[low] + 2*k) && 
				minSizeRec(arr, low+1, i-1, k) == 0 && 
				minSizeRec(arr, i+1, j-1, k) == 0) 
			{ 
				res = min(res, minSizeRec(arr, j+1, high, k)); 
			} 
		} 
	} 

	// Insert value in table and return result 
	return (dp[low][high] = res); 
} 

// This function mainlu initializes dp table and calls 
// recursive function minSizeRec 
int minSize(int arr[], int n, int k) 
{ 
	memset(dp, -1, sizeof(dp)); 
	return minSizeRec(arr, 0, n-1, k); 
} 

// Driver prrogram to test above function 
int main() 
{ 
	int arr[] = {2, 3, 4, 5, 6, 4}; 
	int n = sizeof(arr)/sizeof(arr[0]); 
	int k = 1; 
	cout << minSize(arr, n, k) << endl; 
	return 0; 
} 
