# # A - Fizz
# N = int(input())

# for i in range(1, N+1):
#     if i % 3 == 0:
#         print('Fizz')
#     else:
#         print(i)

# B - Monocolor
# from collections import Counter
# N = int(input())

# C = list(map(int, input().split()))

# cnt = Counter(C)

# max_cnt = 0
# for key, c in cnt.items():
#     max_cnt = max(max_cnt, c)

# print(N-max_cnt)

# C - Inc, Dec, Xor
# N, Q = map(int, input().split())

# A = [0] * N
# active = set()
# xor_all = 0

# for _ in range(Q):
#     query = list(map(int, input().split()))

#     if query[0] == 1:
#         x = query[1] - 1

#         old = A[x]
#         A[x] += 1

#         xor_all ^= old
#         xor_all ^= A[x]

#         active.add(x)

#     else:
#         new_active = set()

#         for x in active:
#             old = A[x]
#             A[x] -= 1

#             xor_all ^= old
#             xor_all ^= A[x]

#             if A[x] > 0:
#                 new_active.add(x)

#         active = new_active
#     print(xor_all)     
    

# D - Inverse and Swap
# N, Q = map(int, input().split())

# P = list(map(int, input().split()))
# t_list = [0]*N
# f_list = [0]*N

# for i, p in enumerate(P):
#     t_list[i] = p-1
#     f_list[p-1] = i

# ok = True
# for q in range(Q):
#     inp = list(map(int, input().split()))

#     if inp[0] == 1:
#         i_1 = inp[1]-1
#         i_2 = inp[2]-1

#         if ok == True:
#             v_1 = t_list[i_1]
#             v_2 = t_list[i_2]
#             t_list[i_1], t_list[i_2] = t_list[i_2], t_list[i_1]
#             f_list[v_1], f_list[v_2] = f_list[v_2], f_list[v_1]
#         else:
#             v_1 = f_list[i_1]
#             v_2 = f_list[i_2]
#             f_list[i_1], f_list[i_2] = f_list[i_2], f_list[i_1]
#             t_list[v_1], t_list[v_2] = t_list[v_2], t_list[v_1]
#     else:
#         ok = not ok
#     # print(t_list, f_list, ok)

# ans = t_list if ok else f_list
# result = [a+1 for a in ans]
# print(*result)


# C - Inc, Dec, Xor
# N, Q = map(int, input().split())
# cnt = [0]*N
# actives = set()
# total = 0
# for q in range(Q):
#     query = list(map(int, input().split()))

#     if query[0] == 1:
#         x = query[1] -1
#         actives.add(x)
#         total ^= cnt[x]
#         cnt[x] += 1
#         total ^= cnt[x]
#     else:
#         new = actives.copy()
#         for act in actives:
#             x = act
#             total ^= cnt[x]
#             cnt[x] -= 1
#             total ^= cnt[x]
#             if cnt[x] == 0: new.remove(act)
#         actives = new
#     print(total)
            

