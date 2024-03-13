from collections import deque
import sys
input = sys.stdin.readline

n, m = [int(x) for x in input().split(' ')]
start_x, start_y, d = [int(r) for r in input().split(' ')]
room = [[int(i) for i in input().split(' ')] for y in range(n)]

def solution(start_x, start_y, d, room):

    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    visited = [[False for _ in range(len(room[0]))] for _ in range(len(room))]

    q = deque()
    q.append((start_x, start_y))

    visited[start_x][start_y] = True

    result = 1

    while q:
        x, y = q.popleft()
        flag = 0

        for _ in range(4):
            d = (d + 3) % 4
            nx = x + dx[d]
            ny = y + dy[d]

            if 0 <= nx < len(room) and 0 <= ny < len(room[0]) and not room[nx][ny]:

                if not visited[nx][ny]:
                    visited[nx][ny] = True
                    result += 1
                    q.append((nx, ny))
                    flag = 1

                    break
                

        if flag == 0:
            if room[x - dx[d]][y - dy[d]] == 0:
                q.append((x - dx[d], y - dy[d]))
            else:
                return result

    return result

print(solution(start_x, start_y, d, room))