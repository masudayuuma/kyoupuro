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
import sys
sys.setrecursionlimit(100000000)
N, X, Y = map(int, input().split())
total = 0
def recrusion_red(level_r):
    if level_r < 2:
        return 0

    level_r -= 1
    blue_n = X*recrusion_blue(level_r+1) + recrusion_red(level_r)

    return blue_n


def recrusion_blue(level_b):
    if level_b < 2:
        return 1

    level_b -= 1
    blue_n = Y*recrusion_blue(level_b) + recrusion_red(level_b)
    return blue_n


print(recrusion_red(N))