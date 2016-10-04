__author__ = 'student'
n = int(input())
A=[]
B=[]
for i in range(n):
    C=list(map(int, input().split()))
    A.append(C[0])
    B.append(C[1])

t = int(input())
k=0
for i in range(n):
    if (A[i]<=t) and (B[i]>=t):
        k+=1
print(k)