# A - A Recursive Function
# N = int(input())

# def recrusion(x):
#     if x == 0:
#         return 1
    
#     return x*recrusion(x-1)

# print(recrusion(N))

# D - Caracal vs Monster
# import sys
# sys.setrecursionlimit(1000000000)

# H = int(input())
# cnt = 0
# def fight(h):
#     if h == 1:
#         # cnt += 1
#         return 1
    
#     return fight(h//2)*2+1


# print(fight(H))

# C - Brute-force Attack
# import sys
# sys.setrecursionlimit(100000000)

# N = int(input())

# def recrusion(string):
#     # print(string)
#     if len(string) == N:
#         print(string)
#         return
    
#     recrusion(string +'a')
#     recrusion(string + 'b')
#     recrusion(string + 'c')


# recrusion('')


# C - 1 2 1 3 1 2 1
# import sys
# sys.setrecursionlimit(100000000)
# N = int(input())

# def recurusion(num):
#     if num == 1:
#         return [1]
    
#     return recurusion(num-1)+[num]+recurusion(num-1)

# print(' '.join(map(str, recurusion(N))))

# # C - Enumerate Sequences
# import sys
# sys.setrecursionlimit(100000000)
# N, K = map(int, input().split())
# R = list(map(int, input().split()))


# def recrusion(cnt, total, tmp):
#     if cnt == N:
#         if total % K == 0:
#             print(*tmp)
#         return


#     for i in range(1, R[cnt]+1):
#         tmp.append(i)
#         total += i
#         recrusion(cnt+1, total, tmp)
#         total -= i
#         tmp.pop()    


# recrusion(0, 0, [])


# C - Sierpinski carpet
# import sys
# sys.setrecursionlimit(100000000)

# N = int(input())

# def make_carpet(k):
#     if k == 0:
#         return['#']
    
#     prev = make_carpet(k-1)
#     size = len(prev)

#     result = []

#     for row in prev:
#         result.append(row*3)

#     for row in prev:
#         result.append(row + '.' * size + row)

#     for row in prev:
#         result.append(row*3)

#     return result

# carpet = make_carpet(N)
# for row in carpet:
#     print(row)

# C - Changing Jewels
# import sys
# sys.setrecursionlimit(100000000)
# N, X, Y = map(int, input().split())
# total = 0
# def recrusion_red(level_r):
#     if level_r < 2:
#         return 0

#     level_r -= 1
#     blue_n = X*recrusion_blue(level_r+1) + recrusion_red(level_r)

#     return blue_n


# def recrusion_blue(level_b):
#     if level_b < 2:
#         return 1

#     level_b -= 1
#     blue_n = Y*recrusion_blue(level_b) + recrusion_red(level_b)
#     return blue_n


# print(recrusion_red(N))

# C - Divide and Divide
# import sys
# sys.setrecursionlimit(100000000)

# N = int(input())
# memo = {}

# def recrusion(num):
#     if num == 1 or num == 0:
#         return 0
    
#     if num in memo:
#         return memo[num]

#     a = (num+2-1)//2
#     b = num//2
#     result = recrusion(a)+recrusion(b)+a+b
#     memo[num] = result
#     return result

# print(recrusion(N))

# use cache
# import sys
# from functools import cache
# sys.setrecursionlimit(100000000)

# N = int(input())
# @cache

# def recrusion(num):
#     if num == 1 or num == 0:
#         return 0
    
#     a = (num+2-1)//2
#     b = num//2
#     return recrusion(a)+recrusion(b)+a+b

# print(recrusion(N))

# C - Concat (X-th)
N, K, X = map(int, input().split())

S_list = [input() for _ in range(N)]

ans = []

def recrusion(str, num):
    if num == K:
        ans.append(str)
        return
    
    for s in S_list:
        recrusion(str+s, num+1)

recrusion('', 0)
ans.sort()
print(ans[X-1])
