# E - Alternating Costs
# T = int(input())

# for i in range(T):
#     a, b, x, y = map(int, input().split())
#     cost = 0
#     x = abs(x)
#     y = abs(y)
#     diff = min(x, y)
#     cost += diff*min(a, b)*2
#     x -= diff
#     y -= diff

#     cnt = 0
#     min_cost_A = min(a, b*3)
#     min_cost_B = min(b, a*3)

#     if x > 0:
#         x_2 = x //2
#         if x % 2 == 1:
#             cost += min_cost_A*(x_2+1)+min_cost_B*x_2
#         else:
#             cost += min_cost_A*x_2+min_cost_B*x_2
#     else:
#         y_2 = y // 2
#         if y % 2 == 1:
#             cost += min_cost_A*y_2+min_cost_B*(y_2+1)
#         else:
#             cost += min_cost_A*y_2+min_cost_B*y_2

#     print(cost)

# E - E-liter
# from atcoder.fenwicktree import FenwickTree
# N, Q = map(int, input().split())

# col_timestamp = [0]*N
# row_timestamp = [-1]*N

# fw_col = FenwickTree(Q+1)
# fw_row = FenwickTree(Q+1)

# ans = 0
# for time in range(Q):
#     q, i = map(int, input().split())
#     i -= 1
#     if q == 1:
#         now_stamp = row_timestamp[i] if row_timestamp[i] > -1 else 0
#         time += 1
#         if row_timestamp[i] == -1:
#             row_timestamp[i] = time
#             ans += N
#         else:
#             fw_row.add(row_timestamp[i], -1)
#             row_timestamp[i] = time
#             ans += fw_col.sum(now_stamp, time)
#         fw_row.add(time, 1)
#         print(ans)
#     else:
#         time += 1
#         if col_timestamp[i] != 0:
#             fw_col.add(col_timestamp[i], -1)
#         now_stamp = col_timestamp[i]
#         ans -= fw_row.sum(now_stamp, time)
#         fw_col.add(time, 1)
#         col_timestamp[i] = time
#         print(ans)

# J - 数列の反転
# from atcoder.fenwicktree import FenwickTree
# N, Q = map(int, input().split())
# fw = FenwickTree(N+2)
# for i in range(Q):
#     t, k = map(int, input().split())

#     if t == 1:
#         pos = k
#         if pos <= N:
#             d = N-pos+1
#         else:
#             d = pos-N
#         flag = fw.sum(0, d+1)%2
#         if flag == 0:
#             print(pos)
#         else:
#             print(2*N+1-pos)
            
#     else:
#         fw.add(1, 1)
#         fw.add(k+1, -1)

