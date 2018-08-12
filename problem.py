#!bin/usr/env python3
T=int(input())
while T:
    Ans=[]
    n=int(input())
    a = list(map(int, input().rstrip().split()))
    for i in range(0,n):
        for j in range(i,n):
            if a[i] > a[j]:
                Ans.append(Ans[i:j])
    T=T-1
    print(len(max(Ans, key=len)))


