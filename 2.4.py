__author__ = 'student'
A = list(map(int, input().split()))
kol = A.count(A[1])
for i in range(len(A)):
    if A.count(A[i])>kol:
        kol = A.count(A[i])
        ch = A[i]
print(ch)