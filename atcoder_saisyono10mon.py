# a,b = map(int, input().split())
# seki = a*b
# if seki%2 == 0:
#     print("Even")
# else:
#     print("Odd")

#精選過去問10問

#3
# N = int(input())
# A = list(map(int, input().split()))
# count = 0
# while all(a % 2 == 0 for a in A):
#     A = [a//2 for a in A]
#     count += 1
# print(count)

    
#4    
# A = int(input())
# B = int(input())
# C = int(input())
# X = int(input())

# count = 0
# for i in range(0, A+1):
#     for j in range(0, B+1):
#         if (X - 500*i - 100*j) % 50 == 0 and (X - 500*i - 100*j) <= C*50 and (X - 500*i - 100*j) >= 0:
#             count += 1

# print(count) 


#5
# N, A, B = map(int, input().split())
# total = 0
# for i in range(0, N+1):
#     if A <= sum(map(int, str(i))) <= B:
#         total += i

# print(total)

#6
# N = int(input())
# a = list(map(int, input().split()))

# a = list(sorted(a, reverse= True))
# alice = 0
# bob = 0
# for i in range(len(a)):
#     if i%2 == 0:
#         alice += a[i]
#     else:
#         bob += a[i]

# print(alice - bob)

#7
# N = int(input())
# d = [input() for i in range(N)]
# print(len(set(d)))

#9
# S = input()
# S = S[::-1]
# divide = ["dream", "dreamer", "erase", "eraser"]
# divide = [d[::-1] for d in divide]

# can = True
# i = 0

# while i < len(S):
#     can2 = False
#     for d in divide:
#         if S[i:i+len(d)] == d: #iからi+len(d)をスライスする
#             can2 = True
#             i += len(d)
#             break
#     if not can2:
#         can = False
#         break

# if can:
#     print("YES")
# else:
#     print("NO")


