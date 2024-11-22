class Solution(object):
    def canVisitAllRooms(self, rooms):
        visited = set()

        def dfs(room):
            visited.add(room)
            for key in rooms[room]:
                if key not in visited:
                    dfs(key)
        dfs(0)

        return len(visited) == len(rooms)
        