h, m = map(int, input().split())

if m < 45:
    if h == 0 :
        h = 23
        m = 60 + m - 45
    else :
        h = h - 1
        m = 60 + m - 45
else :
    m = m - 45

print(h, m)