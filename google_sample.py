class Solution:
    def solve(s: str):
        out = ""

        def dfs(products, l, r):
            if products == 0:
                return ""
            


        
        l = 0
        r = 0
        products = 0
        opencnt = 0
        while r < len(s):
            if r == '[':
                opencnt += 1
                products = int(s[l:r])
                l = r+1
            if r == ']':
                opencnt -= 1
                out += dfs(products, l, r)
            r += 1

