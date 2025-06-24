#A 問題
# N = int(input())
# h = list(map(int, input().split()))

# dp = [0]*N
# dp[0] = 0
# dp[1] =abs(h[1] - h[0])

# for i in range(2, N):
#     dp[i] = min(dp[i-2] + abs(h[i] - h[i-2]), dp[i-1]+abs(h[i]-h[i-1]))

# print(dp[N-1])


#B 問題
# N, K = map(int, input().split())
# h = list(map(int, input().split()))

# dp = [0]*(N)

# dp[0] = 0
# dp[1] = abs(h[0] -h[1])

# for i in range(2, N):
#     dp[i] = dp[i-1]+abs(h[i]-h[i-1])

#     for j in range(2, K+1):
#         if i-j >= 0:
#             dp[i] = min(dp[i-j]+abs(h[i]-h[i-j]), dp[i])
#         else:
#             break

# print(dp[N-1])

#C 問題
# N = int(input())
# dp = [0, 0, 0]
# for i in range(N):
#     a,b,c = map(int, input().split())
#     temp_a = max(dp[1]+a, dp[2]+a)
#     temp_b = max(dp[0]+b, dp[2]+b)
#     temp_c = max(dp[1]+c, dp[0]+c)

#     dp = temp_a, temp_b, temp_c


# max_happy = max(dp[0], dp[1], dp[2])
# print(max_happy)

#D 問題（ナップサック問題1）
# N, W = map(int, input().split())

# dp = [[0]*(W+1) for _ in range(N+1)]

# for i in range(1, N+1):
#     w,v = map(int, input().split())
#     for j in range(W+1):
#         dp[i][j] = dp[i-1][j]

#         if j >= w:
#             dp[i][j] = max(v+dp[i-1][j-w], dp[i-1][j])

# print(dp[N][W])

#E 問題（ナップサック問題2）
# inf = 10**20
# N, W = map(int, input().split())

# dp = [[inf]*(100001) for _ in range(N+1)]
# dp[0][0] = 0


# for i in range(1,N+1):
#     w, v = map(int, input().split())
#     for j in range(100001):
#         if j - v >= 0:
#             dp[i][j] = min(dp[i-1][j-v]+w, dp[i-1][j])
#         else:
#             dp[i][j] = dp[i-1][j]

# for i, d in enumerate(dp[N]):
#     if d <= W:
#         maxv = i

# print(maxv)


#F 問題（LCS）
S = input()
T = input()

dp = [[0] *(len(T)+1) for _ in range((len(S)+1))]

for i in range(len(S)):
    for j in range(len(T)):
        if S[i] == T[j]:
            dp[i+1][j+1] = dp[i][j]+1
        else:
            dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])

ans = []
i = len(S)
j = len(T)
l = dp[i][j]

while l > 0:
    if S[i-1] == T[j-1]:
        ans.append(S[i-1])
        i -= 1
        j -= 1
        l -= 1
    elif dp[i][j] == dp[i-1][j]:
        i -= 1
    else:
        j -= 1
    if l <= 0:
        break

print(''.join(reversed(ans)))

