from collections import deque
import sys

input = sys.stdin.readline

def bfs():
    global maxs
    while q:
        i,j,c = q.popleft()
        c+=1
        for k in range(4):
            nx = i+dx[k]
            ny = j+dy[k]
            if 0<=nx<n and 0<=ny<m and not vist[nx][ny] and s[nx][ny]=='L':
                vist[nx][ny] = True
                q.append([nx,ny,c])
                maxs = max(maxs,c)

n,m= map(int,input().split())
s =[]
for i in range(n):
    s2 = sys.stdin.readline()
    s.append(s2)

dx  =[1,-1,0,0]
dy = [0,0,1,-1]
q = deque()
re = 0
for i in range(n):
    for j in range(m):
        if s[i][j]=='L':
            maxs = 0
            q.append([i,j,1])
            vist = [[False]*m for _ in range(n)]
            vist[i][j] = True
            bfs()
            re = max(re,maxs-1)
print(re)