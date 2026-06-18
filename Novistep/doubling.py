# A57 - Doubling
# N, Q = map(int, input().split())

# A = list(map(int, input().split()))

# dp = [[0]*len(A) for _ in range(30)]

# for i in range(len(A)):
#     dp[0][i] = A[i]

# for i in range(29):
#     for j in range(len(A)):
#         dp[i+1][j] = dp[i][dp[i][j]-1]

# for _ in range(Q):
#     x, y = map(int, input().split())

#     for i in range(30):
#         if 1 << i & y:
#             x = dp[i][x-1]

#     print(x)

# D - Teleporter
# N, K = map(int, input().split())

# A = list(map(int, input().split()))

# dp = [[0]*len(A) for _ in range(60)]

# for i in range(len(A)):
#     dp[0][i] = A[i]

# for i in range(59):
#     for j in range(len(A)):
#         dp[i+1][j] = dp[i][dp[i][j]-1]
# now = 1
# for i in range(60):
#     if 1 << i & K:
#         now = dp[i][now-1]

# print(now)

# 058 - Original Calculator（★4）
N, K = map(int, input().split())

dp = [[0]*(10**5) for _ in range(60)]

for i in range(1, 10**5):
    nxt = i
    target = i
    while i > 0:
        nxt += i%10
        i //= 10
    nxt %= 10**5
    dp[0][target] = nxt

for i in range(59):
    for j in range(10**5):
        dp[i+1][j] = dp[i][dp[i][j]]

for i in range(60):
    if 1 << i & K:
        N = dp[i][N]

print(N)