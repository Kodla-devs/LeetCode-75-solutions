from collections import deque


class Solution(object):
    def predictPartyVictory(self, senate):
        R_queue = deque()
        D_queue = deque()
        for i, s in enumerate(senate):
            if s == 'R':
                R_queue.append(i)
            else:
                D_queue.append(i)
        n = len(senate)

        while R_queue and D_queue:
            r_index = R_queue.popleft()
            d_index = D_queue.popleft()
            if r_index < d_index:
                R_queue.append(r_index + n)
            else:
                D_queue.append(d_index + n)
        return "Radiant" if R_queue else "Dire"