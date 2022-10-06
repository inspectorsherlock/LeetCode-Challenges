class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        ans = []
        for qx, qy, qr in queries:
            count = 0
            
            qr= qr * qr
            for x, y in points:
                if (qx - x) ** 2 + (qy - y) ** 2 <= qr:
                    count += 1
            ans.append(count)
        return ans
        
