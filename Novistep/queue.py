# A52 - Queue
# from collections import deque

# Q = int(input())
# que = deque()

# for _ in range(Q):
#     query = input().split()
#     if query[0] == '1':
#         que.append(query[1])
#     elif query[0] == '2':
#         print(que[0])
#     else:
#         que.popleft()

# B - Restaurant Queue
# from collections import deque

# Q = int(input())
# que = deque()
# for _ in range(Q):
#     query = input().split()

#     if query[0] == '1':
#         que.append(query[1])
#     else:
#         num = que.popleft()
#         print(num)

# B52 - Ball Simulation
# from collections import deque

# N, X = map(int, input().split())
# A = list(input())

# A[X-1] = '@'

# que = deque()
# que.append(X-1)

# while len(que) > 0:
#     t = que.popleft()
#     if t < N-1 and A[t+1] == '.':
#         que.append(t+1)
#         A[t+1] = '@'
#     if t > 0 and A[t-1] == '.':
#         que.append(t-1)
#         A[t-1] = '@'

# print(''.join(A))

# C - Large Queue
# from collections import deque

# Q = int(input())
# ans = 0
# que = deque()
# for _ in range(Q):
#     query = input().split()

#     if query[0] == '1':
#         que.append((int(query[1]), int(query[2])))
#     if query[0] == '2':
#         k = int(query[1])
#         tmp = 0
#         while k > 0:
#             c, x = que[0]
#             if k-c >= 0:
#                 tmp += c*x
#                 que.popleft()
#                 k -= c
#             else:
#                 c = c-k
#                 tmp += k*x
#                 que[0] = (c, x)
#                 break
#         # ans += tmp
#         print(tmp)
        
# D - Cylinder
# from collections import deque

# Q = int(input())
# que = deque()
# for _ in range(Q):
#     query = list(map(int, input().split()))

#     if query[0] == 1:
#         que.append((query[1], query[2]))
#     else:
#         ans = 0
#         k = query[1]
#         while k > 0:
#             # print(que[0])
#             c = que[0][1]
#             x = que[0][0]
#             if k < c:
#                 ans += k*x
#                 que[0] = (x, c-k)
#                 k -= c
#             else:
#                 que.popleft()
#                 ans += x*c
#                 k -= c
#         print(ans)

# Queue
# from collections import deque
# n, q = map(int, input().split())
# que = deque()
# for _ in range(n):
#     name, time = input().split()

#     que.append((name, int(time)))
# total =0
# while len(que) > 0:
#     t_n, t_q = que.popleft()

#     if t_q > q:
#         que.append((t_n, t_q-q))
#         total += q
#     else:
#         total += t_q
#         print(f"{t_n} {total}")

# D - Home Garden
