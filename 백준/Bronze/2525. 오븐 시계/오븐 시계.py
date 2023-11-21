h, m = map(int, input().split())
time = int(input())
minute = m + time

if minute >= 60 :
    while (minute >= 60 ) :
        minute = minute - 60
        h += 1
        if h > 23 :
            h = 0
# else :
#     minute = minute

print(h, minute)