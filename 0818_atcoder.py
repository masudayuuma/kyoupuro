# 	A - AtCoder Language
# S = input()

# if S == 'red':
#     print('SSS')
# elif S == 'blue':
#     print('FFF')
# elif S == 'green':
#     print('MMM')
# else:
#     print('Unknown')

# B - Get Min
Q = int(input())
list_box = []
for i in range(Q):
    n, *x = map(int, input().split())
    if n == 1:
        list_box.append(x[0])
    if n == 2:
        list_box.sort()
        ans = list_box.pop(0)
        print(ans)

import heapq
Q = int(input())
heap = []

for _ in range(Q):
    n, *x = map(int, input().split())
    if n == 1:
        heapq.heappush(heap, x[0])
    elif n == 2:
        ans = heapq.heappop(heap)
        print(ans)
