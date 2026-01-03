# N = int(input())

# print(2**N-2*N)

# B - Happy Number
# N = input()
# cnt = 0
# while cnt < 1000:
#     cnt += 1
#     if N == '1':
#         print('Yes')
#         exit()
#     tmp = 0
#     for n in list(N):
#         n = int(n)
#         tmp += n**2
#     N = str(tmp)

# print('No')

# C - 2026
# from collections import defaultdict
# N = int(input())

# num_dict = defaultdict(int)
# x = 1
# while x*x*2 < N:
#     y = x+1
#     while x*x+y*y <= N:
#         ans = x*x+y*y
#         num_dict[ans] += 1
#         y += 1
#     x += 1

# answer = [n for n in num_dict if num_dict[n] == 1]
# answer.sort()

# print(len(answer))
# if answer:
#     print(' '.join(map(str, answer)))
# else:
#     print()


# D - Kadomatsu Subsequence
# from collections import Counter
# N = int(input())
# A = list(map(int, input().split()))

# right = Counter(A)
# left = Counter()

# ans = 0

# for x in A:
#     right[x] -= 1
#     if right[x] == 0:
#         del right[x]

#     if x % 5 == 0:
#         t = x // 5
#         ver7 = 7*t
#         ver3 = 3*t

#         ans += left.get(ver7, 0)*left.get(ver3, 0)
#         ans += right.get(ver3, 0)*right.get(ver7, 0)

#     left[x] += 1

# print(ans)

# E - Kite
from bisect import bisect_left

N = int(input())

pair = []

for _ in range(N):
    a, b = map(int, input().split())

    pair.append((a, b))

pair.sort(key=lambda x: (x[0], -x[1]))

dp = []
for a, b in pair:
    position = bisect_left(dp, b)
    if position == len(dp):
        dp.append(b)
    else:
        dp[position] = b

print(len(dp))