# A11 - Binary Search 1
#めぐる式
# N, X = map(int, input().split())
# A = list(map(int, input().split()))

# ng = -1
# ok = N
# while ok - ng > 1:
#     mid = (ok + ng) // 2
#     if X <= A[mid]:
#         ok = mid
#     else:
#         ng = mid

# print(ok+1)

#普通
# N, X = map(int, input().split())
# A = list(map(int, input().split()))

# left = 0
# right = N-1
# flag = False
# while left <= right:
#     mid = (left+right)//2
#     if A[mid] > X:
#         right = mid-1
#         continue
#     if A[mid] < X:
#         left = mid+1
#         continue

#     flag = True
#     break

# if flag == True:
#     print(mid+1)
# else:
#     print(-1)    

# ライブラリ使用
# from bisect import bisect_right, bisect_left
# N, X = map(int, input().split())
# A = list(map(int, input().split()))

# print(bisect_left(A, X)+1)

# A12 - Printer
# N, K = map(int, input().split())
# A = list(map(int, input().split()))

# right = 10**9
# left = 1

# while left < right:
#     mid = (left+right)//2
#     num = 0
    
#     for i in A:
#         num += mid//i
#     # print(mid, num)
#     if num >= K:
#         right = mid
#     if num < K:
#         left = mid+1
    
# print(right)


# A13 - Close Pair
# 配列のスライスはTLEなる
# from bisect import bisect_left
# N, K =map(int, input().split())
# A = list(map(int, input().split()))

# ans = 0
# for i in range(N-1):
#     target = A[i]+K
    
#     num = bisect_left(A, target+1)
#     # print(num)
#     ans += max(0, num-(i+1))
    
# print(ans)

# A14 - Four Boxes
# set版
# N, K = map(int, input().split())
# A_list = list(map(int, input().split()))
# B_list = list(map(int, input().split()))
# C_list = list(map(int, input().split()))
# D_list = list(map(int, input().split()))

# A_B_list = []
# C_D_list = []
# for i in range(N):
#     for j in range(N):
#         A_B_list.append(A_list[i]+B_list[j])
#         C_D_list.append(C_list[i]+D_list[j])
# C_D_list = set(C_D_list)

# for i in range(N**2):
#     if K-A_B_list[i] in C_D_list:
#         print('Yes')
#         exit()

# print('No')

# 2分探索
# from bisect import bisect_left
# N, K = map(int, input().split())
# A_list = list(map(int, input().split()))
# B_list = list(map(int, input().split()))
# C_list = list(map(int, input().split()))
# D_list = list(map(int, input().split()))

# A_B_list = []
# C_D_list = []
# for i in range(N):
#     for j in range(N):
#         A_B_list.append(A_list[i]+B_list[j])
#         C_D_list.append(C_list[i]+D_list[j])
# C_D_list.sort()

# for A_B_num in A_B_list:
#     n = bisect_left(C_D_list, K-A_B_num)
#     if n < len(C_D_list) and C_D_list[n] == K -A_B_num:
#         print('Yes')
#         exit()

# print('No')


# A15 - Compression
# from bisect import bisect_left
# N = int(input())
# A = list(map(int, input().split()))

# set_sort_A = sorted(list(set(A)))
# after_A = []
# for a in range(N):
#     ans = bisect_left(set_sort_A, A[a])
#     after_A.append(ans+1)

# print(*after_A)

