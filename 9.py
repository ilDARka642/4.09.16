__author__ = 'student'
n = int(input())
A = list(map(int, input().split()))
k = int(input())
s = 0
for i in range(n-k):
    if sum(A[i:i+k])> s:
        s = sum(A[i:i+k])
print(s)