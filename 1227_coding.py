# A - First Contest of the Year
# D, F = map(int, input().split())

# print(7-((D-F)%7))

# B - Substring 2
# N, M = map(int, input().split())

# S = list(input())
# T = list(input())
# ans = float('inf')
# for i in range(N-M+1):
#     cnt = 0
#     for j in range(M):
#         for k in range(10):
#             if int(S[i+j]) == (int(T[j])+k)%10:
#                 break
#             cnt += 1
            
#     ans = min(ans, cnt)

# print(ans)

# C - 1D puyopuyo
# N = int(input())

# A = list(map(int, input().split()))

# num_stack = []
# same_cnt = 0
# target_num = -1
# for i in range(N):
#     num_stack.append(A[i])

#     if len(num_stack) > 3 and num_stack[-1] == num_stack[-2] == num_stack[-3] == num_stack[-4]:
#         num_stack.pop()
#         num_stack.pop()
#         num_stack.pop()
#         num_stack.pop()

# print(len(num_stack))

# D - Tail of Snake
# N = int(input())

# A = list(map(int, input().split()))
# B = list(map(int, input().split()))
# C = list(map(int, input().split()))

# dp = [[0]*N for _ in range(3)]

# dp[0][0] = A[0]
# for i in range(1, N):
#     dp[0][i] = dp[0][i-1]+A[i]

# dp[1][1] = dp[0][0] + B[1]
# for i in range(2, N):
#     dp[1][i] = max(dp[1][i-1]+B[i], dp[0][i-1]+B[i])

# dp[2][2] = dp[1][1] + C[2]
# for i in range(3, N):
#     dp[2][i] = max(dp[2][i-1]+C[i], dp[1][i-1]+C[i])

# print(dp[2][N-1])

# E - Heavy Buckets
