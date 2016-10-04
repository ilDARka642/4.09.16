__author__ = 'student'
def r(n):
    m=[]
    for i in range(n):
        if i==0 or i==n-1:
            m.append(1)
        else:
            k=r(n-1)
            m.append(k[i-1]+k[i])
    return m
def triangle(x):
    for i in range(x):
        print(r(i+1))
print(triangle(6))
