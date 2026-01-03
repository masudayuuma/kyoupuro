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


#貪欲法で尺取り法を用いる
# for _ in range(int(input())):
#     n, m = map(int, input().split())
#     a = sorted(list(map(int, input().split())), reverse=True)
#     b = sorted(list(map(int, input().split())))
#     c, idx = 0, 0
#     for v in a:
#         while idx < n and b[idx] +v <m:
#             idx += 1
#         if idx >= n:
#             break
#         c += 1
#         idx += 1
#     print(sum(a) + sum(b) - m * c)

