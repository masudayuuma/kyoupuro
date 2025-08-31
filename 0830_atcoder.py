# 	A - Misdelivery
# N = int(input())
# S = [input() for _ in range(N)]

# X, Y = map(str, input().split())
# i = int(X)-1

# if S[i] == Y:
#     print('Yes')
# else:
#     print('No')

# B - Fibonacci Reversed
# X, Y = map(str, input().split())
# ans = [0]*10
# ans[0] = X
# ans[1] = Y

# for i in range(2, 10):
#     tmp_ans = str(int(ans[i-1])+int(ans[i-2]))
#     rev_tmp_ans = tmp_ans[::-1]
#     while rev_tmp_ans[0] == '0':
#         rev_tmp_ans = rev_tmp_ans[1:]
#     ans[i] = rev_tmp_ans

# print(int(ans[9]))

# C - Alternated
# N = int(input())
# S = input()

# A_i = []
# B_i = []
# for i in range(len(S)):
#     if S[i] == 'A':
#         A_i.append(i)
#     else:
#         B_i.append(i)

# mov_for_A = 0
# mov_for_B = 0
# for idx, i in enumerate(A_i):
#     mov_for_A += abs(i-2*idx)
# for idx, i in enumerate(B_i):
#     mov_for_A += abs(i-(2*idx+1))

# for idx, i in enumerate(A_i):
#     mov_for_B += abs(i-(2*idx+1))
# for idx, i in enumerate(B_i):
#     mov_for_B += abs(i-(2*idx))

# ans = min(mov_for_A, mov_for_B)//2
# print(ans)

# N = int(input())
# S = input()
# A_i = []
# for i in range(len(S)):
#     if S[i] == 'A':
#         A_i.append(i)

# mov_for_A = 0
# mov_for_B = 0
# for idx, a_i in enumerate(A_i):
#     mov_for_A += abs(a_i-(2*idx+1))
#     mov_for_B += abs(a_i-(2*idx))

# ans = min(mov_for_A, mov_for_B)
# print(ans)

# D - RLE Moving
