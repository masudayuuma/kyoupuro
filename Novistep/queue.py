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
from collections import deque

Q = int(input())
que = deque()
for _ in range(Q):
    query = input().split()

    if query[0] == '1':
        que.append(query[1])
    else:
        num = que.popleft()
        print(num)