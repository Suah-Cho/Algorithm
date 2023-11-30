n = int(input())
coordinates = [list(map(int, input().split())) for _ in range(n)]

for coordinate in sorted(coordinates) :
    print(coordinate[0], coordinate[1])