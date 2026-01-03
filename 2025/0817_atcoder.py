# 	A - AtCoder Language
# S = input()

# if S == 'red':
#     print('SSS')
# elif S == 'blue':
#     print('FFF')
# elif S == 'green':
#     print('MMM')
# else:
#     print('Unknown')

# B - Get Min
# Q = int(input())
# list_box = []
# for i in range(Q):
#     n, *x = map(int, input().split())
#     if n == 1:
#         list_box.append(x[0])
#     if n == 2:
#         list_box.sort()
#         ans = list_box.pop(0)
#         print(ans)

# import heapq
# Q = int(input())
# heap = []

# for _ in range(Q):
#     n, *x = map(int, input().split())
#     if n == 1:
#         heapq.heappush(heap, x[0])
#     elif n == 2:
#         ans = heapq.heappop(heap)
#         print(ans)

# C - King's Summit
# N = int(input())
# INF = 10**10
# min_r = INF
# max_r = -INF
# min_c = INF
# max_c = -INF

# for n in range(N):
#     r, c = map(int, input().split())
#     min_r = min(min_r, r)
#     max_r = max(max_r, r)
#     min_c = min(min_c, c)
#     max_c = max(max_c, c)

# ans = (max(max_c-min_c, max_r-min_r)+1)//2
# print(ans)


# D - Substr Swap
# N, M = map(int, input().split())
# S = input()
# T = input()
# diff = [0]*(N+1)
# ans = []
# for m in range(M):
#     l, r = map(int, input().split())
#     diff[l-1] += 1
#     diff[r] -= 1

# for i in range(1, N+1):
#     diff[i] = diff[i]+diff[i-1]

# for i in range(N):
#     if diff[i] % 2 == 1:
#         ans.append(T[i])
#     else:
#         ans.append(S[i])
    
# print("".join(ans))

n, m, l = map(int, input().split())
a = list(map(int, input().split()))
a = [x % m for x in a]

cost = [[0]*m for _ in range(l)]
for g in range(l):
    cnt = [0]*m
    for i in range(g, n, l):
        cnt[a[i]] += 1

    tot = sum(cnt)
    S = sum(r0 * cnt[r0] for r0 in range(m))

    suff = [0]*(m+1)
    for r0 in range(m-1, -1, -1):
        suff[r0] = suff[r0+1] + cnt[r0]

    cg = cost[g]
    for k in range(m):
        cg[k] = k*tot - S+m*(suff[k+1] if k+1 <= m else 0)

INF = 10**8
dp = [INF]*m
dp[0] = 0

for g in range(l):
    old = dp
    new = [INF]*m
    cg = cost[g]
    for r in range(m):
        base = old[r]
        if base == INF:
            continue
        idx = r
        for k in range(m):
            val = base + cg[k]
            if val < new[idx]:
                new[idx] = val
            idx += 1
            if idx == m:
                idx = 0
    dp = new
print(dp[0])
