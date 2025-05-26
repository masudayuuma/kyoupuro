#C - K-bonacci 
# N, K = map(int, input().split())
# list = [0 for _ in range(N+1)]
# pref = [0 for _ in range(N+1)]

# if N < K:
#     print(1)
#     exit()

# for i in range(K):
#     list[i] = 1
#     pref[i] = (pref[i-1] + list[i])

# for i in range(K, N+1):
#     list[i] = (pref[i-1] - pref[i-K-1]) % (10**9)
#     pref[i] = (pref[i-1] + list[i]) % (10**9)

# print(list[N])

#C - Sum of Product
# N = int(input())
# A = list(map(int, input().split()))

# total = 0
# presum = 0
# for i in A:
#     total += i*presum
#     presum += i

# print(total)

#C - ~
# N = int(input())
# P = list(map(int, input().split()))

# count_tani = 0
# count_yama = 0
# tani_yama_list = []

# for n in range(N-1):
#     if P[n] < P[n+1]:
#         tani_yama_list.append(1)
#     else:
#         tani_yama_list.append(-1)

# zikkou = []
# cur = tani_yama_list[0]
# length = 1
# for l in range(1, len(tani_yama_list)):
#     if tani_yama_list[l] == cur:
#         length += 1
#     else:
#         zikkou.append((cur, length))
#         cur = tani_yama_list[l]
#         length = 1
# zikkou.append((cur, length))

# ans = 0
# for i in range(len(zikkou)-2):
#     (sg1, a), (sg2, b), (sg3, c) =zikkou[i],zikkou[i+1],zikkou[i+2]
#     if sg1 == 1 and sg2 == -1 and sg3 == 1:     # + - +
#         add = a * c
#         if b == 1:                              # 最短区間 (長さ3) を除く
#             add -= 1
#         ans += add

# print(ans)


#C - Security 2
S = input()

A_count = len(S)
n = len(S)
B_count = int(S[-1])


for i in range(1, n+1):
    str_B = str(B_count)
    if S[n - i] >= str_B[-1]:
        B_count += int(S[n - i]) - int(str_B[-1])
    else:
        B_count += (int(S[n-i])+10) - int(str_B[-1])
    

print(B_count+A_count)
