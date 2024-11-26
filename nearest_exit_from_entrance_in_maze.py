from collections import deque


class Solution(object):
    def nearestExit(self, maze, entrance):
        m, n = len(maze), len(maze[0])
        directions = [[0,1], [1,0], [0,-1], [-1,0]]
        q = deque([[entrance[0], entrance[1], 0]])
        maze[entrance[0]][entrance[1]] = '+'

        while q:
            xo, yo, steps = q.popleft()
            if (0 in [xo, yo] or xo==m-1 or yo==n-1) and [xo,yo] != entrance:
                return steps
            for xn, yn in directions:
                x,y = xo+xn, yo+yn
                if 0<=x<m and 0<=y<n and maze[x][y]=='.':
                    maze[x][y] = '+'
                    q.append([x,y,steps+1])
        return -1