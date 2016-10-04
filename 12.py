__author__ = 'student'
f = open('input.txt', 'r')
a = list(map(int, f.read().split('\n')))
f.close()
m = n = 0
n_max = 0
S = 0
res = 0
for i in range(len(a)):
    if(a[i] == 0):
        S = (m*n)
        if S > res:
            res = S
            n_max = n
        m = 0
        n = 0
        continue
    m += 1
    if(a[i] >= n):
        n0 = n
        S = m*n
        n = a[i]
        if n > res:
            res = n
            n_max = n
    else:
        n0 = n
        n = a[i]
        if(m*n > S):
            S = m*n
            n_max = n
            res = S
f = open('output.txt', 'm')
print(S, file=f)
print(n_max, file=f)
f.close()
