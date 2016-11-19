A = [int(x) for x in raw_input().split()]
A.sort()
print sum(A[:-1]), sum(A[1:])
