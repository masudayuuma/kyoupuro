
# A - Armor
# A, D = map(int, input().split())

# if A > D:
#     print('No')
# else:
#     print('Yes')

# B - The Honest Woodcutters
# N = int(input())

# A = list(map(int, input().split()))
# B = list(map(int, input().split()))
# ans = 'Yes'
# for i, b in enumerate(B):
#     if A[b-1] == i+1:
#         continue
#     else:
#         ans = 'No'

# print(ans)

# C - Variety
# import heapq
# N, K, M = map(int, input().split())
# heap = []
# skip_heap = []

# for i in range(N):
#     c, v = map(int, input().split())

#     heapq.heappush(heap, (-v, c))

# color_cnt = set()
# ans = 0
# ans_cnt = 0
# while heap:
#     val, color = heapq.heappop(heap)

#     if color in color_cnt:
#         heapq.heappush(skip_heap, (val, color))
#         continue
    
#     color_cnt.add(color)
#     ans -= val
#     ans_cnt += 1
#     if len(color_cnt) == M:
#         break

# while heap or skip_heap:
#     if ans_cnt == K:
#         break
#     if skip_heap:
#         val, color = heapq.heappop(skip_heap)
#     else:
#         val, color = heapq.heappop(heap)

#     ans -= val
#     ans_cnt += 1
#     if ans_cnt == K:
#         break

# print(ans)


# D - Count Subgrid Sum = K
# from collections import defaultdict
# H, W, K = map(int, input().split())

# grid = [list(map(int, input().strip())) for _ in range(H)]
# prefix = [[0]*(W+1) for _ in range(H+1)]

# for i in range(1, H+1):
#     for j in range(1, W+1):
#         prefix[i][j] = prefix[i][j-1] + prefix[i-1][j] + grid[i-1][j-1] - prefix[i-1][j-1]

# ans = 0
# for r1 in range(1, H+1):
#     for r2 in range(r1, H+1):
#         cnt = defaultdict(int)
#         cnt[0] = 1
#         for j in range(1, W+1):
#             s = prefix[r2][j] - prefix[r1-1][j]
#             ans += cnt[s - K]
#             cnt[s] += 1

# print(ans)


# C - Variety
# N, K, M = map(int, input().split())
# t = [[] for _ in range(N+1)]

# for i in range(N):
#     C, V = map(int, input().split())
#     t[C].append(V)

# top = []
# tail = []
# for r in t:
#     if len(r) > 0:
#         r.sort(reverse=True)
#         top.append(r[0])
#         tail += r[1:]

# top.sort(reverse=True)
# tail += top[M:]
# tail.sort(reverse=True)
# print(sum(top[:M]) + sum(tail[: K - M]))


# D - Count Subgrid Sum = K
# H, W, K = map(int, input().split())

# grid = [list(map(int, input())) for _ in range(H)]


# prefix = [[0]*(W+1) for _ in range(H+1)]

# for i in range(1, H+1):
#     for j in range(1, W+1):
#         prefix[i][j] = prefix[i][j-1] + prefix[i-1][j] + grid[i-1][j-1] - prefix[i-1][j-1]

# ans = 0
# for h1 in range(1, H+1):
#     for h2 in range(h1, H+1):
#         cnt = {}
#         cnt[0] = 1
#         for w in range(1, W+1):
#             s = prefix[h2][w] - prefix[h1-1][w]
#             ans += cnt.get(s-K, 0)
#             cnt[s] = cnt.get(s, 0)+1
        
# print(ans)

# D - Count Subgrid Sum = K
H, W, K = map(int, input().split())

grid = [list(map(int, input())) for _ in range(H)]

prefix = [[0]*(W+1) for _ in range(H+1)]

for i in range(1, H+1):
    for j in range(1, W+1):
        prefix[i][j] = prefix[i-1][j]+prefix[i][j-1]+grid[i-1][j-1]-prefix[i-1][j-1]
ans = 0

for h1 in range(1, H+1):
    for h2 in range(h1, H+1):
        total = dict()
        total[0] = 1
        for w in range(1, W+1):
            s = prefix[h2][w]-prefix[h1-1][w]
            ans += total.get(s-K, 0)
            total[s] = total.get(s, 0)+1

print(ans)

