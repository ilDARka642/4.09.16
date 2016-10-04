__author__ = 'student'
A=list(map(int, input().split()))
for i in range(len(A)//2+1):
    if len(A)%2==0 and i==len(A)//2:
       break
    if A[i] == A[len(A)-i-1]:
       print(A[i], end=' ')
    else:
       print(A[i], A[len(A)-i-1], end =' ')