#Circular Array Rotation

##Problem Statement
John Watson performs an operation called a *right circular rotation* on an array of integers, [a<sub>0</sub>,a<sub>1</sub>,...a<sub>n-1</sub>]. After performing one *right circular rotation* operation, the array is transformed from a<sub>0</sub>,a<sub>1</sub>,...a<sub>n-1</sub>] to a<sub>n-1</sub>,a<sub>0</sub>,...a<sub>n-2</sub>].

Watson performs this operation k times. To test Sherlock's ability to identify the current element at a particular position in the rotated array, Watson asks q queries, where each query consists of a single integer, m, for which you must print the element at index m in the rotated array (i.e., the value of a<sub>m</sub>).

##Input Format

The first line contains 3 space-separated integers, n, k, and q, respectively. 
The second line contains n space-separated integers, where each integer i describes array element a<sub>i</sub> (where 0 <= i < n). 

Each of the q subsequent lines contains a single integer denoting m.

###Constraints
* 1 <= n <= 10<sup>5</sup>
* 1 <= a<sub>i</sub> <= 10<sup>5</sup>
* 1 <= k <= 10<sup>5</sup>
* 1 <= q <= 500
* 0 <= m <= N - 1 

###Output Format

For each query, print the value of the element at index m of the rotated array on a new line.

###Sample Input

```
3 2 3
1 2 3
0
1
2
```

###Sample Output

```
2
3
1
```