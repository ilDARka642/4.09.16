__author__ = 'student'
A = list(map(int, input().split()))
n = len(A)
for i in range(n-1):
    if (A[i]==2):
        if A[i+1]!=2:
            A[i] = 0
            n -=1
print(sum(A)//n)