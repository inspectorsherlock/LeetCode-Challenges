#Python not Python3
class Solution :
    def  maxIncreaseKeepingSkyline(self, grid) :
        w = len(grid[0])
        h = len(grid)
        lTR = [0] * (h)
        tTB = [0] * (w)
        i = 0
        while (i < w) :
            j = 0
            while (j < h) :
                tTB[i] = max(tTB[i],grid[j][i])
                lTR[j] = max(lTR[j],grid[j][i])
                j += 1
            i += 1
        res = 0
        i = 0
        while (i < h) :
            j = 0
            while (j < w) :
                temp = grid[i][j]
                res += min(lTR[i],tTB[j]) - temp
                j += 1
            i += 1
        return res
