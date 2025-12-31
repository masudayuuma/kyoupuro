# A31 - Divisors
# N = int(input())

# ans_5 = N // 5
# ans_3 = N // 3

# ans_15 = N // 15

# print(ans_5+ans_3-ans_15)

# 004 - Cross Sum（★2）
# H, W = map(int, input().split())

# A = [list(map(int, input().split())) for _ in range(H)]

# prefix_W = [0]*W
# prefix_H = [0]*H
# ans_grid = [[0]*W for _ in range(H)]

# for i in range(H):
#     tmp_ans = 0
#     for j in range(W):
#         tmp_ans += A[i][j]
#     prefix_H[i] = tmp_ans

# for j in range(W):
#     tmp_ans = 0
#     for i in range(H):
#         tmp_ans += A[i][j]
#     prefix_W[j] = tmp_ans

# for i in range(H):
#     for j in range(W):
#         ans = prefix_H[i] + prefix_W[j] - A[i][j]
#         ans_grid[i][j] = ans

# for i in range(H):
#     print(*ans_grid[i])

# C - Anti-Division
# C*D = gcd(C, D)*lcm(C, D)
# from math import lcm
# A, B, C, D = map(int, input().split())

# ans_a_c = (A-1) // C
# ans_a_d = (A-1) // D
# ans_a_c_d = (A-1) // lcm(C, D)
# ans_b_c = B // C
# ans_b_d = B // D
# ans_b_c_d = B // lcm(C, D)
# total_wari = ans_b_c + ans_b_d + ans_a_c_d - ans_a_c - ans_a_d - ans_b_c_d
# print(B-A+1-total_wari)


# B31 - Divisors Hard
# from math import lcm

# N = int(input())

# ans_3 = N // 3
# ans_5 = N // 5
# ans_7 = N // 7

# ans_3_5 = N // lcm(3, 5)
# ans_3_7 = N // lcm(3, 7)
# ans_5_7 = N // lcm(5, 7)

# ans_3_5_7 = N // lcm(3, 5, 7)

# print(ans_3+ans_5+ans_7-(ans_3_5+ans_3_7+ans_5_7)+ans_3_5_7)

# D - FizzBuzz Sum Hard
# from math import lcm
# N, A, B = map(int, input().split())

# ans_A = N // A
# ans_B = N // B
# ans_A_B = N // lcm(A, B)
# hiku = (ans_A+1)*(ans_A)*A//2 + (ans_B+1)*(ans_B)*B//2 - (ans_A_B+1)*(ans_A_B)*lcm(A, B)//2

# print((N+1)*N//2 - hiku)

# C - Ubiquity
# MOD = 10**9+7
# N = int(input())
# ans = (pow(10, N, MOD)-2*pow(9, N, MOD)+pow(8, N, MOD))%MOD
# print(ans)