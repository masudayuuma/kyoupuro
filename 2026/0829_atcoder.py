# A - Second Half Sum
# N = int(input())
# A = list(map(int, input().split()))
# harf = N//2
# print(sum(A[harf:]))

# B - Old Maid
# N = int(input())
# A = list(map(int, input().split()))
# cnt = set()
# for a in A:
#     if a in cnt:
#         cnt.remove(a)
#     else:
#         cnt.add(a)

# print(sum(cnt))

# C - Change Schools
# from collections import Counter
# N, K = map(int, input().split())
# A = list(map(int, input().split()))

# cnt_a = Counter(A)

# max_cnt = max(cnt_a.values())
# # print(max_cnt, cnt_a)
# ans = 0
# for key, val in cnt_a.items():
#     if val == max_cnt or val == max_cnt-1:
#         ans += 1

# print(ans)

# D - Coefficient Stair
# import sys
# sys.setrecursionlimit(10**6)
# N, K = map(int, input().split())

# ans = [0] * N

# def dfs(i, rest):
#     if i == N-1:
#         if rest % N == 0:
#             ans[i] = rest //N
#             print(*ans)
#         return

#     nxt = i + 1

#     for x in range(rest // nxt + 1):
#         ans[i] = x
#         dfs(i + 1, rest - nxt * x)

# dfs(0, K)

# E - K-Divisible Subarrays
# Kの倍数が見つからない限り、tmpのlistに分割場所
#二分探索的に解を見つける

#累積和の二分探索で解を見つけていける？前から順に見てあれば、左のwindowを切っていく。
# from collections import Counter
# N, K = map(int, input().split())
# A = list(map(int, input().split()))
# p = [0]*(N+1)
# for i in range(N):
#     p[i+1] += (p[i]+A[i])%K

# print(max(Counter(p[1:]).values()))

# D - Coefficient Stair
# N, K = map(int, input().split())

# ans = [0]*N
# res = []
# def dfs(i, rest):
#     if i == 0:
#         ans[0] = rest
#         res.append(ans.copy())
#         return

#     for nxt in range((rest//(i+1))+1):
#         ans[i] = nxt
#         dfs(i-1, rest-nxt*(i+1))


# dfs(N-1, K)

# res.sort()

# for a in res:
#     print(' '.join(map(str, a)))

# E - K-Divisible Subarrays
# N, K = map(int, input().split())

# A = list(map(int, input().split()))

# dp = {0: 0}
# now = -1
# best = 0
# total = 0
# for a in A:
#     total = (total + a)%K
#     now = dp.get(total, -1)+1
#     best = max(now, best)
#     # print(best,now, total)
#     dp[total] = best

# print(best)

