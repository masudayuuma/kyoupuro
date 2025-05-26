# # 問題文
# # シカのAtCoDeerくんは二つの正整数 
# # a,b を見つけました。 
# # a と 
# # b をこの順につなげて読んだものが平方数かどうか判定してください。

# # 制約
# # 1 
# # ≤ 
# # a,b 
# # ≤ 
# # 100
# # a,b は整数

# a, b = map(int, input().split())
# n = int(str(a) + str(b))

# if n**0.5 == int(n**0.5):
#     print("Yes")
# else:
#     print("No")

# N = int(input())
# K = int(input())
# X = list(map(int, input().split()))

# sum = 0
# for i in range(1, N+1):
#     minNum = min(abs(X[i-1]), abs(K-X[i-1]))*2
#     sum += minNum

# print(sum)

# N = int(input())
# a = list(map(int, input().split()))

# alice_sum =0
# bob_sum = 0
# a.sort(reverse=True)

# while True:
#     alice_sum += max(a)
#     a.remove(max(a))
#     if a:
#         bob_sum += max(a)
#         a.remove(max(a))
#     if not a:
#         break

# print(alice_sum - bob_sum)

# N = int(input())
# max_sum = 0
# max_num = 0

# for i in range(1, N+1):
#     sum = 0
#     num = i
#     if i == 1:
#         sum += 1
#     while True:
#         if num % 2 == 0:
#             num = num // 2
#             sum += 1
#         else:
#             break

#     if sum > max_sum:
#         max_num = i
#         max_sum = sum
# 
# print(max_num)

# N = int(input())

# macnt = -1  # 最大で2で割れる回数
# ans = -1    # そのときの数

# for x in range(1, N + 1):
#     cnt = 0
#     y = x
#     while y % 2 == 0:
#         y //= 2
#         cnt += 1
#     if cnt > macnt:
#         macnt = cnt
#         ans = x

# print(ans)

# 問題文
# 1 周 
# K メートルの円形の湖があり、その周りに 
# N 軒の家があります。

# i 番目の家は、湖の北端から時計回りに 
# A 
# i
# ​
#   メートルの位置にあります。

# 家の間の移動は、湖の周りに沿ってのみ行えます。

# いずれかの家から出発して 
# N 軒すべての家を訪ねるための最短移動距離を求めてください。

# 制約
# 2≤K≤10 
# 6
 
# 2≤N≤2×10 
# 5
 
# 0≤A 
# 1
# ​
#  <...<A 
# N
# ​
#  <K
# 入力中のすべての値は整数である。
# 入力
# 入力は以下の形式で標準入力から与えられる。

# K 
# N
# A 
# 1
# ​
  
# A 
# 2
# ​
  
# ... 
# A 
# N
# ​
 
# 出力
# いずれかの家から出発して 
# N 軒すべての家を訪ねるための最短移動距離を出力せよ。

# 入力例 1
# Copy
# 20 3
# 5 10 15
# 出力例 1
# Copy
# 10
# 1 番目の家から出発し、
# 2 番目、
# 3 番目の家へ順に移動すると移動距離が 
# 10 になります。

# 入力例 2
# Copy
# 20 3
# 0 5 15
# 出力例 2
# Copy
# 10
# 2 番目の家から出発し、
# 1 番目、
# 3 番目の家へ順に移動すると移動距離が 
# 10 になります。

# K, N = map(int, input().split())
# A = list(map(int, input().split()))

# distances = []

# for i in range(N):
#     if i == N - 1:  # 最後の家と最初の家の間の距離を計算
#         distances.append(K - A[i] + A[0])
#     else:  # 隣り合う家の距離を計算
#         distances.append(A[i+1] - A[i])

# total_distance = sum(distances)  # 全ての距離を合計
# max_distance = max(distances)  # 最も長い距離を見つける

# print(total_distance - max_distance)  # 最大の距離を引く

# A, B, C = map(int, input().split())
# count = 0
# while True:
#     if not A%2 and not B%2 and not C%2:
#         if A == B == C:
#             print(-1)
#             exit()
#         a = B//2 + C//2
#         b = A//2 + C//2
#         c = A//2 + B//2
#         A, B, C = a, b, c
#         count += 1
#     else:
#         break

# print(count)

