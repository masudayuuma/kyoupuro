# A51 - Stack
# Q = int(input())
# stack = []
# for q in range(Q):
#     query = input().split()
#     if query[0] == '1':
#         stack.append(query[1])
#     elif query[0] == '2':
#         name = stack[-1]
#         print(name)
#     else:
#         stack.pop()

# A - 図書館 2 (Library 2)
# Q = int(input())

# read_stack = []
# for q in range(Q):
#     s = input()

#     if s == 'READ':
#         read = read_stack.pop()
#         print(read)
#     else:
#         read_stack.append(s)

# B - Card Pile
# Q = int(input())

# num_stack = [0]*100
# for _ in range(Q):
#     query = input().split()

#     if query[0] == '1':
#         num_stack.append(query[1])
#     else:
#         del_num = num_stack.pop()
#         print(del_num)

# C - Merge the balls
# N = int(input())
# A = list(map(int, input().split()))

# balls_stack = []

# for a in A:
#     balls_stack.append(a)
#     if len(balls_stack) <= 1:
#         continue
    
#     while len(balls_stack) >= 2 and balls_stack[-1] == balls_stack[-2]:
#         pop_1 = balls_stack.pop()
#         pop_2 = balls_stack.pop()

#         balls_stack.append(pop_1+1)

# print(len(balls_stack))

# D - Strange Balls
# N = int(input())

# A = list(map(int, input().split()))

# num_stack = []
# cnt = 0
# target = -1
# total = 0
# for a in A:
#     if target != a:
#         num_stack.append((target, cnt))
#         target = a
#         cnt = 0
        
#     cnt += 1
#     total += 1
#     if target == cnt:
#         total -= cnt
#         target, cnt = num_stack.pop()
        
#     print(total)

# B51 - Bracket
# S = input()

# open_stack = []
# for i in range(len(S)):
#     if S[i] == '(':
#         open_stack.append(i+1)
#     else:
#         t_i = open_stack.pop()
#         print(t_i, i+1)

# 