# N, L, R = map(int, input().split())
# S = input()

# L = L-1


# for i in range(L, R):
#     if S[i] == "x":
#         print("No")
#         exit()

# print("Yes")

# S = input()
# L = ""
# flag = True
# for i in range(len(S)):
#     if S[i] == "#":
#         L += "#"
#         flag = True
#     elif S[i] == "." and flag:
#         L += "o"
#         flag = False

#     else:
#         L += "."

# print(L)

# from itertools import product
# N, K, X = map(int, input().split())
# S = list()
# for i in range(N):
#     s = input()
#     S.append(s)

# all_str = [''.join(p) for p in product(S, repeat=K)]

# all_str.sort()

# print(all_str[X-1])

import bisect
from collections import defaultdict

T = int(input())
for _ in range(T):
    n, m = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    
    # 全ての可能なペアを効率的に生成
    pairs = []
    
    # Aをソート（二分探索のため）
    A_sorted = sorted((A[i], i) for i in range(n))
    values = [x[0] for x in A_sorted]
    
    for j, b in enumerate(B):
        # より広範囲の余りを探索
        # 余り0から数個の小さい余りまでをターゲットにする
        for target_remainder in range(min(10, m)):  # 小さい余りを優先
            target = (m * 1000 + target_remainder - b) % m  # 大きな倍数を使って正確に計算
            
            # targetに最も近い値を二分探索で見つける
            pos = bisect.bisect_left(values, target)
            
            # 前後の値をチェック
            for p in [pos-2, pos-1, pos, pos+1, pos+2]:
                if 0 <= p < n:
                    a_val, a_idx = A_sorted[p]
                    remainder = (a_val + b) % m
                    pairs.append((remainder, a_idx, j))
    
    # 重複除去とソート
    pairs = list(set(pairs))
    pairs.sort()
    
    # 貪欲選択
    used_a = [False] * n
    used_b = [False] * n
    total = 0
    
    for remainder, a_idx, b_idx in pairs:
        if not used_a[a_idx] and not used_b[b_idx]:
            used_a[a_idx] = True
            used_b[b_idx] = True
            total += remainder
            if sum(used_a) == n:  # 全て選択完了
                break
    
    print(total)