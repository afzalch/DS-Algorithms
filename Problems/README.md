## Table of Contents
- [Table of Contents](#table-of-contents)
- [Patterns](#patterns)
  - [Sliding Window](#sliding-window)
  - [Two Pointers](#two-pointers)
  - [Fast and slow pointers](#fast-and-slow-pointers)
  - [Merge Intervals](#merge-intervals)
  - [Cyclic Sort](#cyclic-sort)
  - [In-place reversal of a linkedlist](#in-place-reversal-of-a-linkedlist)
  - [Tree Breadth First Search](#tree-breadth-first-search)
  - [Tree Depth First Search](#tree-depth-first-search)
  - [Two Heaps](#two-heaps)
  - [Subsets](#subsets)
  - [Modified Binary Search](#modified-binary-search)
  - [Bitwise XOR](#bitwise-xor)
  - [Top 'K' Elements](#top-k-elements)
  - [K-way merge](#k-way-merge)
  - [0/1 Knapsack (DP)](#01-knapsack-dp)
  - [Topological sort](#topological-sort)
- [Strings](#strings)


## Patterns

### Sliding Window
- For problems dealing with contiguous subarrays or sublists of a certain size
  - eg. Given an array, find the average of all the contiguous subarrays of size 'K' in it
- Sliding window would make it so that the amount of calculation is reduced as shown by image below
  - Would ensure that only the uncommon elements are calculated by subtracting the exiting value from window and adding the new value from the window

![Alt text](../images/sliding-window.PNG?raw=true "Sliding Window")

Java
```
public static double[] findAverages(int K, int[] arr) {
double[] result = new double[arr.length - K + 1];
double windowSum = 0;
int windowStart = 0;
for (int windowEnd = 0; windowEnd < arr.length; windowEnd++) {
    windowSum += arr[windowEnd]; // add the next element
    // slide the window, we don't need to slide if we've not hit the required window size of 'k'
    if (windowEnd >= K - 1) {
    result[windowStart] = windowSum / K; // calculate the average
    windowSum -= arr[windowStart]; // subtract the element going out
    windowStart++; // slide the window ahead
    }
}

return result;
}
```

Python
```
def find_averages_of_subarrays(K, arr):
  result = []
  windowSum, windowStart = 0.0, 0
  for windowEnd in range(len(arr)):
    windowSum += arr[windowEnd]  # add the next element
    # slide the window, we don't need to slide if we've not hit the required window size of 'k'
    if windowEnd >= K - 1:
      result.append(windowSum / K)  # calculate the average
      windowSum -= arr[windowStart]  # subtract the element going out
      windowStart += 1  # slide the window ahead

  return result
```

### Two Pointers


### Fast and slow pointers


### Merge Intervals


### Cyclic Sort


### In-place reversal of a linkedlist


### Tree Breadth First Search


### Tree Depth First Search

### Two Heaps


### Subsets


### Modified Binary Search


### Bitwise XOR


### Top 'K' Elements


### K-way merge


### 0/1 Knapsack (DP)


### Topological sort


## Strings