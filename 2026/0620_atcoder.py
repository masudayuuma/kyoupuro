# A - 16:9
# x, y = map(int, input().split())
# if x*9 == y*16:
#     print('Yes')
# else:
#     print('No')

# B - Train Reservation
# N, X = input().split()
# N = int(N)

# c_dict = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4}

# target = c_dict[X]
# for _ in range(N):
#     s = input()

#     if s[target] == 'o':
#         print('Yes')
#         exit()

# print('No')

# C - Tallest at the Moment
# import bisect

# N = int(input())

# h_list = []
# l_list = []
# max_h = 0
# for i in range(N):
#     h, l = map(int, input().split())
#     h_list.append(h)
#     l_list.append(l)

# target_l = []
# target_h = []
# max_h = 0
# for i in range(N-1, -1, -1):
#     t_h = h_list.pop()
#     t_l = l_list.pop()

#     if max_h < t_h:
#         max_h = t_h
#         target_h.append(t_h)
#         target_l.append(t_l)

# target_h.reverse()
# target_l.reverse()

# Q_n = int(input())
# Q = list(map(int, input().split()))

# for q in Q:
#     a = bisect.bisect_left(target_l, q+1)
#     print(target_h[a])


# D - Maximize the Gap
# N, K = map(int, input().split())

# heap = []

# for i in range(N):
#     l, r = map(int, input().split())
#     heap.append([l, r])
# heap.sort(key=lambda x: x[1])

# l = 0
# r = 10**9+1

# def possible(x):
#     cnt = 1
#     last_r = heap[0][1]
#     for i in range(1, len(heap)):
#         l, r = heap[i]
#         if l - last_r >= x:
#             cnt += 1
#             last_r = r
#     return cnt >= K

# while r - l > 1:
#     mid = (r+l)//2

#     if possible(mid):
#         l = mid
#     else:
#         r = mid

# ans = l if possible(1) and l >= 0 and possible(l) else -1
# print(ans)

# D - Maximize the Gap
# N, K = map(int, input().split())
# lenght_list = []

# for i in range(N):
#     l, r = map(int, input().split())
#     lenght_list.append([l, r])

# lenght_list.sort(key= lambda x : x[1])

# ok = 0
# ng = 10**9+1

# while ng - ok > 1:
#     mid = (ok+ng)//2
#     prev_r = lenght_list[0][1]
#     cnt = 1
#     for l, r in lenght_list[1:]:
#         if prev_r+mid > l:
#             continue

#         cnt += 1
#         prev_r = r

#     if cnt >= K:
#         ok = mid
#     else:
#         ng = mid

# if ok > 0:
#     print(ok)
# else:
#     print(-1)

