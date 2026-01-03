# A - Triangular Number
# N = int(input())
# ans = 0
# for i in range(1, N+1):
#     ans += i

# print(ans)

#saisoku
# N = int(input())
# print(N*(N+1)//2)

# B - No-Divisible Range
# N = int(input())
# A = list(map(int, input().split()))
# ans = 0
# for i in range(N-1):
#     tmp_sum = A[i]
#     tmp_list = [A[i]]
#     for j in range(i+1, N):
#         tmp_sum += A[j]
#         tmp_list.append(A[j])
#         flag = True
#         for k in tmp_list:
#             if tmp_sum % k == 0:
#                 flag = False
#                 break
#         if flag == True:
#             ans += 1
# print(ans)


# C - Domino
# N = int(input())
# A = list(map(int, input().split()))
# ans = 1
# can_do = A[0]-1
# for i in range(1, N):
#     if can_do > 0:
#         ans += 1
#         can_do = max(can_do-1, A[i]-1)
#         continue
#     else:
#         break

# print(ans)

# D - Reachability Query 2
# N, M = map(int, input().split())
# move_ret = [set() for _ in range(N + 1)]
# for _ in range(M):
#     x, y = map(int, input().split())
#     move_ret[y].append(x)

# Q = int(input())
# can_path = [False] * (N + 1)

# ans = []

# for _ in range(Q):
#     n, v = map(int, input().split())
#     if n == 1:
#         if not can_path[v]:
#             stack = [v]
#             while stack:
#                 u = stack.pop()
#                 if can_path[u]:
#                     continue
#                 can_path[u] = True
#                 for prev in move_ret[u]:
#                     if not can_path[prev]:
#                         stack.append(prev)
#     else:
#         ans.append("Yes" if can_path[v] else "No")

# for i in ans:
#     print(i)

# mou1kai
# import sys
# sys.setrecursionlimit(10**6)
# from collections import defaultdict
# N, M = map(int, input().split())
# s2s = defaultdict(list)
# black_symbol = set()
# que = []
# for i in range(M):
#     x, y = map(int, input().split())
#     s2s[y].append(x)

# def check(symbol):
#     for s in s2s[symbol]:
#         if not s in black_symbol:
#             black_symbol.add(s)
#             check(s)


# Q = int(input())
# for i in range(Q):
#     q, v = map(int, input().split())
#     if q == 1:
#         if not v in black_symbol:
#             black_symbol.add(v)
#             check(v)
#     else:
#         print('Yes' if v in black_symbol else 'No')
            

# E - Cover query　コンテスト後改めて実行するとTLEなるのはなぜ
# from sortedcontainers import SortedList

# N, Q = map(int, input().split())

# ans_list = SortedList()
# total_b = 0

# for _ in range(Q):
#     L, R = map(int, input().split())
    
#     t_l, t_r = L, R
    
#     idx = ans_list.bisect_left((L, 0))
    
#     if idx > 0 and ans_list[idx-1][1] >= L-1:
#         idx -= 1
    
#     while idx < len(ans_list) and ans_list[idx][0] <= t_r + 1:
#         l, r = ans_list[idx]
#         total_b -= (r-l+1)
#         t_l = min(t_l, l)
#         t_r = max(t_r, r)
#         ans_list.pop(idx)
    
#     ans_list.add((t_l, t_r))
#     total_b += (t_r-t_l+1)
    
#     print(N-total_b)

# もう１回　TLEなるのはなぜ
# from sortedcontainers import SortedList
# N, Q = map(int, input().split())

# tree_list = SortedList()
# ans = 0
# for q in range(Q):
#     t_l, t_r = map(int, input().split())
    
#     idx = tree_list.bisect_left((t_l, 0))

#     if idx > 0 and tree_list[idx-1][1]+1 >= t_l:
#         idx -= 1

#     while idx < len(tree_list) and t_r+1 >= tree_list[idx][0]:

#         l, r = tree_list[idx]

#         t_l = min(t_l, l)
#         t_r = max(t_r, r)
#         tree_list.pop(idx)
#         ans -= r-l+1

#     tree_list.add((t_l, t_r))
#     ans += t_r-t_l+1
#     print(N-ans)

# F - Cat exercise
# Cartesian Treeという構造を用いてDPを解くらしいが、ライブラリが欲しいところ
# import sys
# sys.setrecursionlimit(1_000_000)
# input = sys.stdin.readline


# class CartesianTree:
#     """
#     最大ヒープ Cartesian Tree を O(N) で構築するクラス
#     a: 配列 (list of int)
#     is_max=True: 値が最大ヒープになるように構築
#     """
#     def __init__(self, a, is_max=True):
#         n = len(a)
#         self.n = n
#         self.l = [-1] * n   # 左の子
#         self.r = [-1] * n   # 右の子
#         self.root = -1
#         self.build(a, is_max)

#     def build(self, a, is_max=True):
#         n = self.n
#         l = self.l
#         r = self.r
#         st = []

#         # ここは AtCoder editorial の実装と同じ最大ヒープ用アルゴリズム
#         for i in range(n):
#             last = -1
#             # 最大ヒープなので「小さい方」を落としていく単調スタック
#             while st and a[st[-1]] < a[i]:
#                 last = st.pop()

#             if st:
#                 # 現在の i は，スタック頂点の「右の子」になる
#                 r[st[-1]] = i
#             if last != -1:
#                 # さっきポップされた last は，i の「左の子」になる
#                 l[i] = last

#             st.append(i)

#         # ルート：スタック底が根（=最初に入って最後まで残る）
#         self.root = st[0]


# def main():
#     n = int(input())
#     p = list(map(int, input().split()))

#     # 最大ヒープ Cartesian Tree を構築
#     t = CartesianTree(p, is_max=True)

#     l = t.l
#     r = t.r

#     # f(v): v を根とする部分木だけ残したときの，取りうる最大移動距離
#     def dfs(v: int) -> int:
#         res = 0
#         lv = l[v]
#         rv = r[v]
#         if lv != -1:
#             res = max(res, dfs(lv) + (v - lv))
#         if rv != -1:
#             res = max(res, dfs(rv) + (rv - v))
#         return res

#     ans = dfs(t.root)
#     print(ans)


# if __name__ == "__main__":
#     main()
