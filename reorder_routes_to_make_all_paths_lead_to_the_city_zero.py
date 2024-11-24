class Solution:
    def dfs(self, graph, visited, city):
        changes = 0
        visited[city] = True
        for neighbor in graph[city]:
            if not visited[abs(neighbor)]:
                changes += self.dfs(graph, visited, abs(neighbor))
                changes += 1 if neighbor > 0 else 0
        return changes 

    def minReorder(self, n, roads):
        graph = [[] for _ in range(n)]
        for a, b in roads:
            graph[a].append(b)
            graph[b].append(-a)
        visited = [False] * n
        return self.dfs(graph, visited, 0)
