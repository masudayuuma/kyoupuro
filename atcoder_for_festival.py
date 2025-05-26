#https://qiita.com/e869120/items/f1c6f98364d1443148b3#%E5%85%A8%E6%8E%A2%E7%B4%A2%E3%81%AE%E5%95%8F%E9%A1%8C

#2
# N = int(input())
# S = input()

# count = 0
# for i in range(N-2):
#     if S[i] == "A" and S[i+1] == "B" and S[i+2] == "C":
#         count += 1

# print(count)

#3
# S = input()
# max_count = 0
# serial_count = 0
# S = S + "X"
# for i in range(len(S)):
#     if S[i] == "A" or S[i] == "C" or S[i] == "G" or S[i] == "T":
#         serial_count += 1
#     else:
#         serial_toggle = False
#         if serial_count > max_count:
#             max_count = serial_count
#             serial_count = 0
# print(max_count)

#4
# N = int(input())
# count = 0
# for i in range(1, N+1):
#     if i%2 == 1:
#         divided_count = 0
#         for j in range(1, N+1):
#             if i >= j and i % j == 0:
#                 divided_count += 1
#         if divided_count >= 8:
#             count += 1
            
# print(count)

#4
# A, B, K = map(int, input().split())
# count_num= []
# for i in range(1, max(A,B)+1):
#     if A % i == 0 and B % i == 0:
#         count_num.append(i)
# count_num.sort(reverse=True)
# print(count_num[K-1])

#5 N**0.5まで計算すれば約数がある。（例えば整数 nが素数かどうかを判定するのは、実は 2 から n−−√ まで順に試し割りすればよいという話など。）
# N = int(input())
# min_digit = 10000000000000000000000000000000000000000000
# for i in range(1, int(N**0.5)+1):
#     if N%i == 0:
#         digit = max(int(len(str(N//i))) , int(len(str(i))))
#         if min_digit > digit:
#             min_digit = digit

# print(min_digit)

#6
# A, B, C, X, Y = map(int, input().split())
# ans = 10**18
# for c in range(0, max(X, Y)*2+1):
#     need_a = max(0, X-c//2)
#     need_b = max(0, Y-c//2)
#     total_cost = need_a*A + need_b*B + c*C
#     ans = min(ans, total_cost)

# print(ans)

#7 さすがにムズイ
# N = int(input())
# S = input()

# NEXT = [[N]* 10 for _ in range(N+1)]
# for i in range(N-1, -1, -1):
#     NEXT[i] = NEXT[i+1][:]
#     d = int(S[i])
#     NEXT[i][d] = i

# ans = 0
# for pin in range(1000):
#     a = pin // 100
#     b = (pin//10) % 10
#     c = pin % 10

#     pos = NEXT[0][a]
#     if pos == N:
#         continue
#     pos = NEXT[pos+1][b]
#     if pos == N:
#         continue
#     pos = NEXT[pos+1][c]
#     if pos == N:
#         continue
#     ans += 1

# print(ans)

