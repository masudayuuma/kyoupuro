#B - Unauthorized 
# N = int(input())
# S = [input() for _ in range(N)]

# flg_login = False
# err_count = 0

# for n in range(N):
#     if S[n] == "login":
#         flg_login = True
#     elif S[n] == "private" and flg_login == False:
#         err_count += 1
#     elif S[n] == "logout":
#         flg_login = False
#     else:
#         continue
        
# print(err_count)

#B - Not All
# N, M = map(int, input().split())
# A = list(map(int, input().split()))

# count_del = 0
# while True:
#     if all(i in A for i in range(1, M+1)):
#         A = A[:-1]
#         count_del += 1
#     else:
#         break

# print(count_del)

#B - Grid Rotation
# N = int(input())
# S = [list(input()) for _ in range(N)]
# T = [list(input()) for _ in range(N)]

# min_dif = 1000000000
# def rotete_clockwise(matrix):
#     global min_dif
#     n = len(matrix)
#     result = [[0] * n for _ in range(n)]
    
#     # まず回転させる
#     for i in range(N):
#         for j in range(N):
#             result[j][n-1-i] = matrix[i][j]
    
#     # 回転後に差分をカウント
#     dif_count = 0
#     for i in range(N):
#         for j in range(N):
#             if T[i][j] != result[i][j]:
#                 dif_count += 1
                
#     min_dif = min(min_dif, dif_count)
#     return result

# # 90度回転
# S_90 = rotete_clockwise(S)


# # 180度回転
# S_180 = rotete_clockwise(S_90)


# # 270度回転
# S_270 = rotete_clockwise(S_180)


# S_360 = rotete_clockwise(S_270)

# print(min_dif+1)

#B - Product Calculator
# N, K = map(int, input().split())
# A = list(map(int, input().split()))

# num = 1
# for n in range(N):
#     num *= A[n]
#     if len(str(num)) > K:
#         num = 1

# print(num)

#B - Sum of Geometric Series
# N, M = map(int, input().split())
# sum_gs = 1
# for i in range(1, M+1):
#     sum_gs += N**i
#     if sum_gs > 10**9:
#         print("inf")
#         exit()
# print(sum_gs)

#B - Ranking with Ties
# N = int(input())
# P = list(map(int, input().split()))

# S = sorted(P, reverse=True)

# ranking_numbering = {}
# for p in P:
#     for s in range(N):
#         if p == S[s]:
#             print(s+1)
#             break

#B - Full House 3
# A = list(map(int, input().split()))

# counter = {}
# for a in A:
#     if a in counter:
#         counter[a] += 1
#     else:
#         counter[a] = 1

# found = False
# for x in counter:
#     if counter[x] >= 3:
#         for y in counter:
#             if x != y and counter[y] >= 2:
#                 found = True
#                 break
# if found:
#     print("Yes")
# else:
#     print("No")

#B - P(X or Y)
# X, Y = map(int, input().split())
# bunnbo = 36
# x_count = 0
# y_count = 0

# for i in range(1, 7):
#     for j in range(1, 7):
#         if i+j >= X and abs(i-j) >= Y:
#             x_count += 1
#         elif i+j >= X:
#             x_count += 1
#         elif abs(i-j) >= Y:
#             y_count += 1
        
# print((x_count+y_count)/bunnbo)

#B - Ticket Gate Log
# S = input()
# S += "p"
# new_S = ""
# cnt = 0
# if S[0] == "o":
#     S = "i" + S
#     cnt += 1
# for i in range(len(S)-1):
#     new_S += S[i]
#     if S[i] == S[i+1] == "i":
#         new_S += "o"
#         cnt += 1
#     if S[i] == "o" and S[i+1] == "o":
#         new_S += "i"
#         cnt += 1
# # print(new_S)

# if len(new_S) % 2 == 0:
#     print(cnt)
# else:
#     print(cnt + 1)

#B - Four Hidden
# T = input()
# U = input()


# for i in range(len(T) - len(U)+1):
#     flg = True
#     for j in range(len(U)):
#         if not T[i+j] == '?' and not T[i+j] ==U[j]:
#             flg = False
#             break
#     if flg == True:
#         print('Yes')
#         exit()

# print('No') 

#B - Card
# from collections import deque

# stack = deque()
# for i in range(100):
#     stack.append(0)

# types = []
# results = []
# Q = int(input())
# for i in range(Q):
#     type, *x = map(int, input().split())
#     if type == 1:
#         stack.append(x[0])
#     else:
#         results.append(stack.pop())

# for result in results:
#     print(result)


#B - Citation
# N = int(input())
# A = list(map(int, input().split()))

# max_x = 0

# for x in range(N + 1):
#     count = 0
#     for a in A:
#         if a >= x:
#             count += 1
    
#     if count >= x:
#         max_x = x

# print(max_x)












