class Solution:
   def canFinish(self, N, edges):
        pre = defaultdict(list)
        for x, y in edges: pre[x].append(y)

        status = [0] * N
        def canTake(i):
            if status[i] in {1, -1}: return status[i] == 1
            status[i] = -1
            if any(not canTake(j) for j in pre[i]): return False
            status[i] = 1
            return True

        return all(canTake(i) for i in range(N))
        