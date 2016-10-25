#!/bin/python

"""
Given a square matrix of size N x N, calculate the absolute difference between the sums of its diagonals.

Input Format
The first line contains a single integer, N. The next  lines denote the matrix's rows, with each line containing N space-separated integers describing the columns.

Output Format
Print the absolute difference between the two sums of the matrix's diagonals as a single integer.

"""

N = int(raw_input())
total = 0
for i in range(N):
    row = raw_input().split()
    total += int(row[i])-int(row[-(i+1)])
print(abs(total))