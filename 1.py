__author__ = 'student'
A = list(map(int, input().split()))
print(' '.join(map(str, A[::2])))
print(max(A), A.index(max(A)))
print(' '.join(map(str, A[::-1])))