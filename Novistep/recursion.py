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
