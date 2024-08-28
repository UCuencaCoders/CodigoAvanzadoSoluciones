class Solution:
    def minimumDistance(self, points) -> int:
        s = list()
        d = list()
        distances = list()

        for pair in points:
            s.append(pair[0] + pair[1])
            d.append(pair[0] - pair[1])

        i = [s.index(max(s)), s.index(min(s)), d.index(max(d)), d.index(min(d))]
        for j in i:
            distances.append(self.getMaxDistance(s, d, j))
        
        return min(distances)
            
points = [[3,10],[5,15],[10,2],[4,4]]

Solution = Solution()
print(Solution.minimumDistance(points))