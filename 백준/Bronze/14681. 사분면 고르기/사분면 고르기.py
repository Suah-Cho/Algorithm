x = int(input())
y = int(input())

if x > 0 :
    # 1,4분면
    if y > 0 :
        print("1")
    else :
        print("4")
else :
    # 2,3분면
    if y > 0 :
        print("2")
    else :
        print("3")