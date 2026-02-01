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
from collections import deque

N, X = map(int, input().split())
A = list(input())

A[X-1] = '@'

que = deque()
que.append(X-1)

while len(que) > 0:
    t = que.popleft()
    if t < N-1 and A[t+1] == '.':
        que.append(t+1)
        A[t+1] = '@'
    if t > 0 and A[t-1] == '.':
        que.append(t-1)
        A[t-1] = '@'

print(''.join(A))