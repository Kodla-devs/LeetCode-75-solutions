from collections import defaultdict


class Solution(object):
    def calcEquation(self, equations, values, queries):
        graph = defaultdict(dict)
        for (a, b), value in zip(equations, values):
            graph[a][b] = value
            graph[b][a] = 1 / value
        
        def dfs(start, end, visited):
            if start not in graph or end not in graph:
                return -1.0
            if start == end:
                return 1.0
            visited.add(start)
            for neighbor, weight in graph[start].items():
                if neighbor not in visited:
                    result = dfs(neighbor, end, visited)
                    if result != -1.0:
                        return result * weight
            return -1.0

        results = []
        for x, y in queries:
            results.append(dfs(x, y, set()))
        return results