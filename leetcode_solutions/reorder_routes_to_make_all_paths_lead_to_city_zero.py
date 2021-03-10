class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        facing = {0}
        num = 1
        res = 0
        while num != len(connections)+1:
            last = -1
            while num != last:
                for j in range(len(connections)):
                    start = connections[j][0]
                    end = connections[j][1]
                    if end in facing and not start in facing:
                        facing.add(start)
                        num+=1 
                last = num
            for j in range(len(connections)):
                start = connections[j][0]
                end = connections[j][1]
                if start in facing and not end in facing:
                    facing.add(end)
                    connections[j][1] = start
                    connections[j][0] = end
                    num+=1 
                    res+=1
        return res
