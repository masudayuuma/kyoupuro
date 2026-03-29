# A - Five Integers
# A, B, C, D, E = map(int, input().split())

# ans = len(set([A, B, C, D, E]))
# len(set((A, B, C, D, E)))
# len({A, B, C, D, E})
# print(ans)

# B - Count Distinct Integers
# N = int(input())
# A = list(map(int, input().split()))
# print(len(set(A)))

# B - Substring
# S = input()
# ans_set = set()
# tmp = ''
# for i in range(len(S)):
#     tmp = S[i]
#     ans_set.add(tmp)
#     for j in range(i+1, len(S)):
#         tmp += S[j]
#         ans_set.add(tmp)

# print(len(ans_set))

# B - Shiritori 
# N = int(input())
# ans = set()
# before = ''
# continue_flag = True
# for i in range(N):
#     if before == '':
#         before = input()
#         ans.add(before)
#         continue
#     else:
#         now = input()
#         if not before[-1] == now[0] or now in ans:
#             continue_flag = False
#         else:
#             ans.add(now)
#             before = now

# print('Yes') if continue_flag == True else print('No')

# B - Postal Card
# N, M = map(int, input().split())
# s_list = []
# cnt = 0
# for _ in range(N):
#     s_list.append(input())
# t_list = []
# for _ in range(M):
#     t_list.append(input())

# for i in range(N):
#     tmp = s_list[i]
#     for j in range(M):
#         if tmp[-1] == t_list[j][-1] and tmp[-2] == t_list[j][-2] and tmp[-3] == t_list[j][-3]:
#             cnt += 1
#             break

# print(cnt)

