# Compare the triplets

##Problem Statement

Alice and Bob each created one problem for HackerRank. A reviewer rates the two challenges, awarding points on a scale from 1 to 100 for three categories: problem clarity, originality, and difficulty.
We define the rating for Alice's challenge to be the triplet A = (a<sub>0</sub>,a<sub>1</sub>,a<sub>2</sub>), and the rating for Bob's challenge to be the triplet B = (b<sub>0</sub>, b<sub>1</sub>. b<sub>2</sub>).

Your task is to find their comparison scores by comparing a<sub>0</sub> with b<sub>0</sub>, a<sub>1</sub> with b<sub>1</sub>, and a<sub>2</sub> with b<sub>2</sub>.

If a<sub>i</sub> > b<sub>i</sub>, then Alice is awarded  point.
If a<sub>i</sub> < b<sub>i</sub>, then Bob is awarded  point.
If a<sub>i</sub> = b<sub>i</sub>, then neither person receives a point.

Given A and B, can you compare the two challenges and print their respective comparison points?

###Input format
The first line contains 3 space-separated integers, a<sub>0</sub>, a<sub>1</sub>, and a<sub>2</sub>, describing the respective values in triplet A. 
The second line contains 3 space-separated integers, b<sub>0</sub>, b<sub>1</sub>, and b<sub>2</sub>, describing the respective values in triplet B.

####Constraints

* 1 <= a<sub>i</sub> <= 100
* 1 <= b<sub>i</sub> <= 100

###Sample Input

```
5 6 7

3 6 10
```

###Sample Output

```
1 1 
```
