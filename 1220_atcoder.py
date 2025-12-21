# A - Feet
# A, B = map(int, input().split())

# print(12*A+B)

# B - Tombola
# from collections import defaultdict
# H, W, N = map(int, input().split())
# A_dict = [set() for _ in range(H)]
# cnt_dict = defaultdict(int)
# for i in range(H):
#     tmp = set(list(map(int, input().split())))
#     A_dict[i] = tmp
#     cnt_dict[i] = 0

# for n in range(N):
#     b = int(input())
#     for j in range(H):
#         if b in A_dict[j]:
#             cnt_dict[j] += 1

# print(max(cnt_dict.values()))


# C - Reindeer and Sleigh 2
# T = int(input())

# for _ in range(T):
#     N = int(input())
#     rider = []
#     for i in range(N):
#         W, P = map(int, input().split())
#         rider.append((W, P))

#     rider.sort(key= lambda x: x[0] + x[1], reverse=True)
#     pull_p = 0
#     total_w = sum(w for w, p in rider)
#     puller = 0

#     for w, p in rider:
#         if pull_p >= total_w:
#             break

#         pull_p += w
#         total_w -= p
#         puller += 1

#     if pull_p >= total_w:
#         print(N-puller)
#     else:
#         print(0)

# T = int(input())

# for _ in range(T):
#     N = int(input())
#     rest_animal = []
#     total_weigh = 0
#     total_power = 0
#     for i in range(N):
#         w, p = map(int, input().split())
#         rest_animal.append((w, p))
#         total_weigh += w

#     rest_animal.sort(key=lambda x: x[0]+x[1], reverse=True)
#     move_cnt = 0
#     for nw, np in rest_animal:
#         if total_weigh <= total_power:
#             break
        
#         move_cnt += 1
#         total_weigh -= nw
#         total_power += np

#     print(N-move_cnt)

# D - Sum of Differences
from bisect import bisect_left
MOD = 998244353
N, M = map(int, input().split())

A = sorted(list(map(int, input().split())))
B = sorted(list(map(int, input().split())))

prefix = [0]*(M+1)

for i in range(M):
    prefix[i+1] = prefix[i]+B[i]
ans = 0

for a in A:
    t_a = bisect_left(B, a)
    total_smallers = prefix[t_a]
    total_largers = prefix[-1] - prefix[t_a]

    result = (t_a*a - total_smallers + total_largers - a*(M-t_a))%MOD

    ans = (ans+result)%MOD

print(ans)
