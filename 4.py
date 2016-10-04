__author__ = 'student'
A=list(map(int, input().split()))
ch=int(input())
dl=len(A)
for i in range(ch):
    A.insert(dl-A[dl-1]-1, A[dl-1])
print(*A[:dl])