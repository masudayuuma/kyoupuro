#1
# N, L = map(int, input().split())
# K = int(input())
# A = list(map(int, input().split()))

# A.append(L) #34の追加
# dif = [A[0]]
# for i in range(N):
#     dif.append(A[i+1] - A[i])

# def is_ok(x):
#     length = 0
#     cnt = 0
#     for i in dif:
#         if length+i >= x:
#             cnt += 1
#             length = 0
#         else:
#             length += i
#     return cnt #分割する領域

# def meguru_bisect(ng, ok):
#     while ng - ok > 1:
#         mid = (ng + ok) // 2
#         print(mid)
#         if is_ok(mid) >= K+1:
#             ok = mid
#         else:
#             ng = mid
#     return ok
    
# print(meguru_bisect(L+1, -1))


#4 004 - Cross Sum（★2）
# h, w = map(int, input().split())
# A = [list(map(int, input().split())) for _ in range(h)]

# row_sum = []
# col_sum = []

# for i in A:
#     row_sum.append(sum(i))

# for i in range(w):
#     sumsum = 0
#     for j in range(h):
#         sumsum += A[j][i]
#     col_sum.append(sumsum)        

# for i in range(h):
#     line = [str(row_sum[i] + col_sum[j] - A[i][j]) for j in range(w)]
#     print(' '.join(line))


#007 - CP Classes（★3）
N = int(input())
A = list(map(int, input().split()))
Q = int(input())
B = [int(input()) for _ in range(Q)]

A = sorted(A)
abs_a_b = []

for b in range(Q):
    first = 0
    final = N-1
    while final - first > 1 :
        mid = (first + final) // 2
        if A[mid] >= B[b]:
            final = mid
        else:
            first = mid
    # print(A[final] - B[b])
    abs_a_b.append(min(abs(A[final] - B[b]), abs(A[first] - B[b]) ))

for i in range(Q):
    print(abs_a_b[i])
        


#010 - Score Sum Queries（★2）
# N = int(input())
# c = [0 for _ in range(N)] 
# p = [0 for _ in range(N)]
# ruisekiwa = [[0,0] for _ in range(N)]
# for n in range(N):
#     c.append(int(input()))
#     p.append(int(input()))
#     if c[n] == 1:
#         ruisekiwa[n][0] += ruisekiwa[n-1][0] + p[n]
#         ruisekiwa[n][1] += ruisekiwa[n-1][1]
#     elif c[n] == 2:
#         ruisekiwa[n][1] += ruisekiwa[n-1][1] + p[n]
#         ruisekiwa[n][0] += ruisekiwa[n-1][0]


# Q = int(input())

# l = []
# r = []

# for q in range(Q):
#     l.append(int(input()))
#     r.append(int(input()))

# for q in range(Q):
#     sum_1 = ruisekiwa[r][0] - ruisekiwa[l-1][0]
#     sum_2 = ruisekiwa[r][1] - ruisekiwa[l-1][1]
#     print(sum_1 + ' ' + sum_2)
    
#↑の正解版、↑はエラー多い。考え方はあっていた
# import sys
# input = sys.stdin.readline

# N = int(input())
# class1 = [0]*(N+1)
# class2 = [0]*(N+1)

# for i in range(1, N+1):
#     c,p = map(int, input().split())
#     class1[i] = class1[i-1] + ( p if c == 1 else 0 )
#     class2[i] = class2[i-1] + ( p if c == 2 else 0 )

# Q = int(input())

# for i in range(Q):
#     l, r = map(int, input().split())
#     ans1 = class1[r] - class1[l-1]
#     ans2 = class2[r] - class2[l-1]
#     print(f"{ans1} {ans2}")

#022 - Cubic Cake（★2）
# import math

# A, B, C = map(int, input().split())

# gcd_A_B = math.gcd(A, B)
# gcd_A_B_C = math.gcd(gcd_A_B, C)

# cut_num = (A//gcd_A_B_C -1) + (B //gcd_A_B_C - 1) + (C // gcd_A_B_C -1)
# print(cut_num)

