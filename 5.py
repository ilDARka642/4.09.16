__author__ = 'student'
k = int(input())
n = int(input())
A = [1]*k
for i in range(k, n+1):
    A.append(sum(A[i-k:i]))
print(A[n])