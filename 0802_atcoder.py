# N, A, B = map(int, input().split())
# S = input()

# ans = S[A:N-B]
# print(ans)

# N, M = map(int, input().split())
# A = list(map(int, input().split()))
# B = list(map(int, input().split()))


# for b in B:
#     if b in A:
#         A.remove(b) 

# if A:  
#     print(*A)

# from collections import defaultdict
# N = int(input())
# A = list(map(int, input().split()))

# count = defaultdict(int)
# result = 0

# for i in range(N):
#     target = i - A[i]
    
#     result += count[target]

#     count[i+A[i]] += 1

# print(result)


import sys
from bisect import bisect_right
input = sys.stdin.readline

n = int(input())

p, a, b = [], [], []
for _ in range(n):                       # ← ここは “読み込み専用”
    pi, ai, bi = map(int, input().split())
    p.append(pi)
    a.append(ai)
    b.append(bi)

M = 1001                                 # ← ここから読み込みループの外
dp = [[0] * M for _ in range(n + 1)]

for j in range(M):
    dp[n][j] = j                         # ベースケース

for i in range(n - 1, -1, -1):           # 後ろ向き DP
    for j in range(M):
        nxt = j + a[i] if j <= p[i] else max(0, j - b[i])
        dp[i][j] = dp[i + 1][nxt]

bs = [0] * (n + 1)                       # b の累積和
for i in range(n):
    bs[i + 1] = bs[i] + b[i]

q = int(input())
out = []
for _ in range(q):                       # ← クエリループ
    x = int(input())
    if x >= M:
        i = bisect_right(bs, x - M, 0, n)
        x -= bs[i]
        ans = dp[i][x] if i < n else x
    else:
        ans = dp[0][x]
    out.append(str(ans))                 # ← ここはクエリごとに append

sys.stdout.write("\n".join(out))
