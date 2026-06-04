# 倉庫の在庫管理
# N, M = map(int, input().split())

# limit_list = []
# now_list = []

# for i in range(N):
#     w, l = map(int, input().split())

#     limit_list.append(l)
#     now_list.append(w)

# for i in range(M):
#     p, c = map(int, input().split())

#     now_list[p-1] += c

# ans = 0
# for i in range(N):
#     now = now_list[i]
#     limit = limit_list[i]

#     if now > limit:
#         ans += 1

# print(ans)


# B - お買い物プラン
from collections import Counter
categoly_dict = {}
N, M = map(int, input().split())

T = list(map(int, input().split()))
# list(map(int, input().split()))
cnt_t = Counter(T)

for i in range(M):
    s, c = map(int, input().split())
    if s in categoly_dict:
        categoly_dict[s] = min(c, categoly_dict[s])
    else:
        categoly_dict[s] = c

ans = 0
flag = True
for key, val in cnt_t.items():
    if key not in categoly_dict:
        flag = False
        break
    ans += categoly_dict[key]*val

if flag == True:
    print(ans)
else:
    print(-1) 

# C - 迷路の最短経路
# bfsです



# D - 美術館の巡回
