a, b, c = map(int, input().split())

if (a == b) or (a == c) :
    sameNumber = a
else :
    sameNumber = b


if (a == b) and (b == c) and (a == c):
    print(10000 + sameNumber * 1000)
elif (a == b) or (b == c) or (a == c) :
    print(1000 + sameNumber * 100)
else :
    print(max(a, b, c) * 100)