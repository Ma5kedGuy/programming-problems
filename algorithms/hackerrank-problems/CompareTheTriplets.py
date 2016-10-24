#!/bin/python

"""
Alice and Bob each created one problem for HackerRank. A reviewer rates the two challenges, awarding points on a scale from 1 to 100 for three categories: problem clarity, originality, and difficulty.
We define the rating for Alice's challenge to be the triplet A = (a0,a1,a2), and the rating for Bob's challenge to be the triplet B = (b0, b1. b2).
Your task is to find their comparison scores by comparing a0 with b0, a1 with b1, and a2 with b2.
If ai > bi, then Alice is awarded  point.
If ai < bi, then Bob is awarded  point.
If ai = bi, then neither person receives a point.
Given A and B, can you compare the two challenges and print their respective comparison points?

"""

A = [int(x) for x in raw_input().split()]
B = [int(x) for x in raw_input().split()]

Ascore = len([1 for a,b in zip(A,B) if a > b])
Bscore = len([1 for a,b in zip(A,B) if a < b])

print Ascore,Bscore