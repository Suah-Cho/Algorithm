a, b, c = map(int, input().split())
A = (a == b)
B = (b == c)
C = (a == c)
sameNumber = 0

if A or C :
    sameNumber = a
else :
    sameNumber = b


if A and B and C:
    print(10000 + sameNumber * 1000)
elif A or B or C :
    print(1000 + sameNumber * 100)
else :
    print(max(a, b, c) * 100)