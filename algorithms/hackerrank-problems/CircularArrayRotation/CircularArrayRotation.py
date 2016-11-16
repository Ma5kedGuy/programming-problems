n,k,q = raw_input().split()
n,k,q = [int(n),int(k),int(q)]
res_map = raw_input()
res_map = map(int,res_map.split())
for i in range(q,0,-1):
    m = input()
    print res_map[(m - k) % n]
