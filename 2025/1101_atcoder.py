# A - Candy Cookie Law
# A, B, C, D = map(int, input().split())

# if A <= C:
#     if B <= D:
#         print('No')
#     else:
#         print('Yes')
# else:
#     print('No')

# B - Count Subgrid
# N, M = map(int, input().split())
# S = [input() for _ in range(N)]

# set_grid = set()

# for i in range(N-M+1):
#     for j in range(N-M+1):
#         targetgrid = tuple(S[i+k][j:j+M] for k in range(M))
#         set_grid.add(targetgrid)

# print(len(set_grid))

# C - Truck Driver
N, A, B = map(int, input().split())

S = input()

l, r = 0, 1
a_cnt = 0
b_cnt = 0
ans = 0
if S[0] == 'a':
    a_cnt += 1
else:
    b_cnt += 1

while True:
    if a_cnt >= A and b_cnt < B:
        ans += 1
        if r != N-1:
            r += 1
            if S[r] == 'a':
                a_cnt += 1
            else:
                b_cnt += 1
    elif b_cnt < B:
        r += 1
        if r == N:
            break
        if S[r] == 'a':
            a_cnt += 1
        else:
            b_cnt += 1      
    elif r == l:
        r += 1
        if r == N:
            break
        if S[r] == 'a':
            a_cnt += 1
        else:
            b_cnt += 1     

    elif b_cnt >= B:
        if S[l] == 'a':
            a_cnt -= 1
        else:
            b_cnt -= 1
        l += 1

# N, A, B = map(int, input().split())
# S = input().strip()

# ans = 0
# l = 0

# ra = 0
# acnt_a = 0
# bcnt_a = 0

# rb = 0
# acnt_b = 0
# bcnt_b = 0

# while l < N:
#     while ra < N and acnt_a < A:
#         if S[ra] == 'a':
#             acnt_a += 1
#         else:
#             bcnt_a += 1
#         ra += 1

#     while rb < N and bcnt_b < B:
#         if S[rb] == 'a':
#             acnt_b += 1
#         else:
#             bcnt_b += 1
#         rb += 1

#     if acnt_a >= A:
#         left = max(ra, l+1)
#         right = min(rb, N)
#         if right > left:
#             ans += right-left
#     if S[l] == 'a':
#         if l < ra:
#             acnt_a -= 1
#         if l < rb:
#             acnt_b -= 1
#     else:
#         if l < ra:
#             bcnt_a -= 1
#         if l < rb:
#             bcnt_b -= 1

#     l += 1

#     if ra < l:
#         ra = l 
#     if rb < l:
#         rb = l

# print(ans)

# D - Neighbor Distance
# from collections import defaultdict
# from bisect import bisect_right
# N = input()
# X = list(map(int, input().split()))

# diff_dict = defaultdict(int)

# diff_dict[0] = X[0]
# diff_dict[X[0]] = X[0]
# ans = X[0]*2
# bisect_list = [0, X[0]]


# for i in range(1, len(X)):
#     target_i = bisect_right(bisect_list, X[i])
#     bisect_list = bisect_list[:target_i] + X[i] + bisect_list[target_i:]
#     if target_i > 0 and diff_dict[bisect_list[target_i-1]]:
#         ans -= diff_dict[bisect_list[target_i-1]]
#         ans += 
#         diff_dict[bisect_list[target_i-1]] = min(diff_dict[target_i-1], X[i] - bisect_list[target_i-1])
#     if target_i != len(bisect_list)-1 and diff_dict[bisect_list[target_i+1]]:
#         diff_dict[bisect_list[target_i+1]] = min(diff_dict[target_i+1], bisect_list[target_i+1]-X[i])

# filepath: [1101_atcoder.py](http://_vscodecontentref_/1)
# D - Neighbor Distance
# from bisect import bisect_right, insort

# N = int(input())
# X = list(map(int, input().split()))

# positions = [0]
# min_dist = {}
# ans = 0

# for x in X:
#     idx = bisect_right(positions, x)
#     insort(positions, x)

#     left_dist = x - positions[idx - 1] if idx > 0 else float('inf')
#     right_dist = positions[idx + 1] - x if idx < len(positions) - 1 else float('inf')
#     new_min_dist = min(left_dist, right_dist)
#     min_dist[x] = new_min_dist
#     ans += new_min_dist

#     if idx > 0:
#         left_pos = positions[idx - 1]
#         old_left_dist = min_dist.get(left_pos, float('inf'))
#         new_left_dist = x - left_pos
#         if idx > 1:
#             new_left_dist = min(new_left_dist, left_pos - positions[idx - 2])
        
#         if old_left_dist == float('inf'):
#             min_dist[left_pos] = new_left_dist
#             ans += new_left_dist
#         elif new_left_dist < old_left_dist:
#             ans -= old_left_dist
#             ans += new_left_dist
#             min_dist[left_pos] = new_left_dist
    
#     if idx < len(positions) - 1:
#         right_pos = positions[idx + 1]
#         old_right_dist = min_dist.get(right_pos, float('inf'))
#         new_right_dist = right_pos - x
#         if idx + 2 < len(positions):
#             new_right_dist = min(new_right_dist, positions[idx + 2] - right_pos)
#         if new_right_dist < old_right_dist:
#             if old_right_dist != float('inf'):
#                 ans -= old_right_dist
#             ans += new_right_dist
#             min_dist[right_pos] = new_right_dist
    
#     print(ans)