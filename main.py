import random

x = [3, 8, 9]
u = [2, 5, 6]

a = [50, 8, 120]
B = 1
C = 2
D = 5
E = 5
F = 5
G = 5
s = sum(x)
d = s

T = 10
def cit(x, a, u):
    return (x - a) ** 2 + B*a**2 + C + u


def pt(d, i, v):
    return D - E*d[i] - F*d[i-1] - G*d[i - 2] + v[i]


if __name__ == "__main__":

    for t in range(T):
        
        s = sum(x)
        i = 3
        d = s
        v = [random.random(), random.random(), random.random()]

        pt = pt(d, i, v)

        pit_a =[]
        cit_a = []

        for i in range(3):
        cit_a.append(cit(x[i], a[i], u[i]))
        pit_a.append(pt * x[i] - cit)

        print(pit_a, cit_a)

    
    
