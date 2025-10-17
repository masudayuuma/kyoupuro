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

#B - Restaurant Queue
# from collections import deque

# queue = deque()
# result = []
# Q = int(input())

# for _ in range(Q):
#     q, *n = map(int, input().split())
#     if q == 1:
#         queue.append(n[0])
#     else:
#         result.append(queue.popleft())

# for res in result:
#     print(res)

# from collections import deque

# q = int(input())
# que = deque()

# for _ in range(q):
#     t, *x = map(int,input().split())
#     if t == 1:
#         que.append(x[0])
#     else:
#         print(que[0])
#         que.popleft()

#B - Make Target
# N = int(input())

# target = [["?"]*N for _ in range(N)]

# for i in range(N):
#     for j in range(N):
#         if min(i, j, N-i-1, N-j-1) % 2 == 0:
#             target[i][j] = "#"
#         else:
#             target[i][j] = "."

# for row in target:
#     print("".join(row))

#B - cat
# N = int(input())
# result = ""
# cnt = []
# for i in range(N):
#     s = input()
#     cnt.append(s)

# cnt.sort(key = len)
# print("".join(cnt))

#B - A..B..C
# S = input()
# cnt = 0
# for i in range(len(S)-2):
#     for j in range(i+1, len(S)-1):
#         for k in range(i+2, len(S)):
#             if S[i] == "A" and S[j] == "B" and S[k] == "C" and j-i == k-j:
#                 cnt += 1

# print(cnt)



# B - Pick Two
# S = input()

# for i in range(len(S)-1):
#     for j in range(i+1, len(S)):
#         if S[i] == "#" and S[j] == "#":
#             print(f"{i+1},{j+1}")
#             S = S.replace("#", ".", 1)
#             S = S.replace("#", ".", 1)

# String Too Long
# N = int(input())
# ans = ""
# for i in range(N):
#     c, l = input().split()
#     l = int(l)
#     if l > 100:
#         print("Too Long")
#         exit()
#     else:
#         ans += c*l
#         if len(ans) > 100:
#             print("Too Long")
#             exit()

# print(ans)

# B - cat 2
# N = int(input())
# ans = set()
# S = list()
# for i in range(N):
#     s = input()
#     S.append(s)

# for i in range(N-1):
#     for j in range(i+1, N):
#         ans.add(S[i]+S[j])
#         ans.add(S[j]+S[i])

# print(len(ans))

# B - Precondition 
# S = input()
# T = input()
# T = set(T)

# for s in range(1, len(S)):
#     if S[s].isupper():
#         if S[s-1] in T:
#             continue
#         else:
#             print('No')
#             exit()

# print('Yes')

# B - Distance Table
# N = int(input())
# D = list(map(int, input().split()))

# ans = []

# for i in range(len(D)):
#     tmp_num = 0
#     tmp_ans = []
#     for j in range(i,len(D)):
#         tmp_num += D[j]
#         tmp_ans.append(tmp_num)
#     ans.append(tmp_ans)

# for a in ans:
#     print(' '.join(map(str, a)))

# B - Reverse Proxy
# N, Q = map(int, input().split())
# X = list(map(int, input().split()))

# X_box = [0]*N
# ans = []
# for i in X:
#     if i == 0:
#         min_num = min(X_box)
#         min_i = X_box.index(min_num)
#         X_box[min_i] += 1
#         ans.append(min_i+1)
#     else:
#         X_box[i-1] += 1
#         ans.append(i)

# # print(" ".join(map(str, ans)))
# print(*ans)

# B - Compression
# N = int(input())
# A = list(map(int, input().split()))

# A = list(set(A))
# A.sort()

# print(len(A))
# print(' '.join(map(str, A)))

# B - Who is Missing?
# N, M = map(int, input().split())
# A = list(map(int, input().split()))

# ans = []
# for i in range(1, N+1):
#     if i in A:
#         continue
#     else:
#         ans.append(i)
# print(len(ans))
# print(*ans)

# B - Seek Grid 
# N, M = map(int, input().split())
# S = [list(input()) for _ in range(N)]
# T = [list(input()) for _ in range(M)]

# for s_i in range(len(S)-len(T)+1):
#     for s_j in range(len(S[0])-len(T[0])+1):
#         flag = False
#         ans = (s_i+1, s_j+1)
#         for t_i in range(len(T)):
#             for t_j in range(len(T[0])):
#                 if S[s_i+t_i][s_j+t_j] != T[t_i][t_j]:
#                     flag =True
#                     break
#             if flag == True:
#                 break
#         if flag == False:
#             print(*ans)
#             exit()

# ans = (-1, -1)
# print(*ans)

# B - Geometric Sequence
# N = int(input())
# A = list(map(int, input().split()))
# if N == 1:
#     print('Yes')
#     exit()

# for i in range(2, N):
#     if A[i] * A[0] != A[i-1]*A[1]:
#         print('No')
#         exit()

# print('Yes')
            
# 	B - tcaF
# X = int(input())
# index = 1
# while X > 1:
#     X /= index
#     index += 1

# print(index-1)


# B - Heavy Snake
# N, D = map(int, input().split())
# ans = 0
# T = []
# L = []
# for i in range(N):
#     t, l = map(int, input().split())
#     T.append(t)
#     L.append(l)

# for i in range(1,D+1):
#     ans = 0
#     for j in range(N):
#         t, l = T[j], L[j]
#         if ans < t*(l+i):
#             ans = t*(l+i)
#     print(ans)

# B - 9x9 Sum
# X = int(input())
# ans = 0
# for i in range(1, 10):
#     for j in range(1, 10):
#         if i*j == X:
#             continue
#         ans += i*j

# print(ans)


# S = input()
# cnt = 0
# i = 0
# while i < len(S):
#     if S[i] == '0' and S[i+1] == '0':
#         cnt += 1
#         i += 2
#     else:
#         cnt += 1
#         i += 1
#     # print(cnt)
#     if i == len(S)-1:
#         cnt += 1
#         break

# print(cnt)

# B - Santa Claus 1
# h, w, x, y = map(int, input().split())

# path_grid = [input() for _ in range(h)]

# path = input()
# times = len(path)
# cnt = set()
# x, y = x-1, y-1
# for i in range(times):
#     if path[i] == 'U' and (path_grid[x-1][y] == '@' or path_grid[x-1][y] == '.'):
#         if path_grid[x-1][y] == '@':
#             cnt.add((x-1, y))
#         x, y = x-1, y
#     elif path[i] == 'D' and (path_grid[x+1][y] == '@' or path_grid[x+1][y] == '.'):
#         if path_grid[x+1][y] == '@':
#             cnt.add((x+1, y))
#         x, y = x+1, y
#     elif path[i] == 'L' and (path_grid[x][y-1] == '@' or path_grid[x][y-1] == '.'):
#         if path_grid[x][y-1] == '@':
#             cnt.add((x, y-1))
#         x, y = x, y-1
#     elif path[i] == 'R' and (path_grid[x][y+1] == '@' or path_grid[x][y+1] == '.'):
#         if path_grid[x][y+1] == '@':
#             cnt.add((x, y+1))
#         x, y = x, y+1
#     else:
#         continue

# print(x+1, y+1, len(cnt))


# B - Find Permutation 2 
# N = int(input())
# A = list(map(int, input().split()))

# ans = set()
# cnt = 0
# for i in range(N):
#     if A[i] == -1:
#         cnt += 1
#     elif not A[i] in ans:
#         ans.add(A[i])
#     else:
#         print('No')
#         exit()

# if len(ans)+cnt == N:
#     print('Yes')
# else:
#     print('No')

# kari = []
# for i in range(N):
#     if not i+1 in ans:
#         kari.append(i+1)

# for i in range(N):
#     if A[i] == -1:
#         A[i] = kari.pop()

# print(' '.join(map(str, A)))
    
# B - Perfect
# from collections import defaultdict
# N, M, K = map(int, input().split())
# ans = []
# dict = defaultdict(int)
# for i in range(K):
#     a, b = map(int, input().split())
#     dict[a] += 1
#     if dict[a] == M:
#         ans.append(a)

# print(*ans)

# B - Locked Rooms
# N = int(input())
# L = list(map(int, input().split()))
# cnt_left = 1
# cnt_right = 1
# for i in range(N):
#     if L[i] == 0:
#         cnt_left += 1
#         # print('left')
#     else:
#         break

# for i in range(N-1, -1, -1):
#     if L[i] == 0:
#         cnt_right += 1
#         # print('right')
#     else:
#         break

# if cnt_left+cnt_right >= N+1:
#     print(0)
# else:
#     print(N+1-(cnt_left+cnt_right))

# B - The Odd One Out
# from collections import defaultdict
# S = input()
# dict = defaultdict(int)

# for s in S:
#     if s in dict:
#         dict[s] += 1
#     else:
#         dict[s] = 1

# for key, cnt in dict.items():
#     if cnt == 1:
#         print(key)
    
# # B - Sum of Digits Sequence
# n = int(input())

# # a0 = 1
# a_list = [0]*(n+1)
# a_list[0] = 1
# total = 0
# for i in range(1, n+1):
#     total = 0
#     for j in range(0, i):
#         for k in str(a_list[j]):
#             total += int(k)
#     a_list[i] = total
#     # print(total, a_list[i])


# print(total)