#Kangaroo

##Problem Statement
There are two kangaroos on an x-axis ready to jump in the positive direction (i.e, toward positive infinity). The first kangaroo starts at location x<sub>1</sub> and moves at a rate of v<sub>1</sub> meters per jump. The second kangaroo starts at location x<sub>2</sub> and moves at a rate of v<sub>2</sub> meters per jump. Given the starting locations and movement rates for each kangaroo, can you determine if they'll ever land at the same location at the same time?

###Input Format

A single line of four space-separated integers denoting the respective values of x<sub>1</sub>, v<sub>1</sub>, x<sub>2</sub>, and v<sub>2</sub>.

###Constraints
* 0 <= x<sub>1</sub> < x<sub>2</sub> <= 10000
* 1 < v<sub>1</sub> <= 10000
* 1 < v<sub>2</sub> <= 10000

###Output Format

Print `YES` if they can land on the same location at the same time; otherwise, print `NO`.

**Note**: The two kangaroos must land at the same location after making the same number of jumps.

###Sample Input 0

```
0 3 4 2
```

###Sample Output 0

```
YES
```