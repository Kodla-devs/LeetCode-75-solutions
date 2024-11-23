class Solution(object):
    def findCircleNum(self, isConnected):
        def dfs(city):
            for neighbor in range(len(isConnected)):
                if isConnected[city][neighbor] == 1 and not visited[neighbor]:
                    visited[neighbor] = True
                    dfs(neighbor)
    
        n = len(isConnected)
        visited = [False] * n
        provinces = 0

        for i in range(n):
            if not visited[i]:
                provinces += 1
                visited[i] = True
                dfs(i)
        return provinces
        