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

# D - Colorful Bracket Sequence
# S = input()

# stack = []

# bracket_dict = {')': '(', ']':'[', '>':'<'}

# for s in S:
#     if s in bracket_dict and len(stack) > 0 and bracket_dict[s] == stack[-1]:
#         stack.pop()
#     else:
#         stack.append(s)

# print('Yes' if len(stack) == 0 else 'No')

# Stack
# S = input().split()

# operater = {'+': lambda a,b: a+b,
#             '-': lambda a,b: a-b,
#             '*': lambda a,b: a*b
# }
# caculate_stack = []

# for s in S:
#     if s in operater:
#         num1 = caculate_stack.pop()
#         num2 = caculate_stack.pop()
#         # print(operater[s](num2, num1))
#         caculate_stack.append(operater[s](num2, num1))
#     else:
#         caculate_stack.append(int(s))

# print(caculate_stack[0])

# D - Take ABC
# S = list(input())

# char_stack = []
# char_comb = {'A':'X', 'B': 'A', 'C':'B'}

# for s in S:
#     char_stack.append(s)
#     if len(char_stack) > 2 and char_stack[-1] == 'C' and char_comb[char_stack[-1]] == char_stack[-2] and char_comb[char_stack[-2]] == char_stack[-3]:
#         char_stack.pop()
#         char_stack.pop()
#         char_stack.pop()

# print(''.join(char_stack))


# B - Abbreviate Fox
# N = int(input())
# S = list(input())

# char_stack = []

# for s in S:
#     char_stack.append(s)
#     if len(char_stack) > 2 and char_stack[-1] == 'x' and char_stack[-2] == 'o' and char_stack[-3] == 'f':
#         char_stack.pop()
#         char_stack.pop()
#         char_stack.pop()

# print(len(char_stack))

# D - Mismatched Parentheses
# N = int(input())
# S = input()

# char_stack = []
# open_cnt = -1
# open_stack = 0
# del_target = ''
# for i in range(N):
#     if S[i] == '(':
#         open_stack += 1
#         char_stack.append(S[i])
#     elif S[i] == ')' and open_stack > 0:
#         while del_target != '(':
#             del_target = char_stack.pop()
#         del_target = ''
#         open_stack -= 1
#     else:
#         char_stack.append(S[i])

# print(''.join(char_stack))

# D - Scope
# S = input()

# char_stack = []
# char_set = set()
# for s in S:
#     if s in char_set:
#         print('No')
#         exit()

#     char_stack.append(s)
#     if s != '(' and s != ')':
#         char_set.add(s)
#     if s == ')':
#         target = ''
#         while target != '(':
#             target = char_stack.pop()
#             if target in char_set:
#                 char_set.remove(target)

# print('Yes')

# D - Moves on Binary Tree
# 掛け算の値が増えると計算量が重くなりすぎてTLEする
# N, X = map(int, input().split())

# S = input()

# diff_stack = []
# for s in S:
#     if s == 'U':
#         if len(diff_stack) > 0:
#             diff_stack.pop()
#         else:
#             X = X // 2
#     else:
#         diff_stack.append(s)

# for s in diff_stack:
#     if s == 'U':
#         X = X // 2
#     elif s == 'R':
#         X = 2*X+1
#     elif s == 'L':
#         X = 2*X

# print(X)

# C - Brackets Stack Query
Q = int(input())
stack = []
open_cnt = 0
close_cnt = 0
target = -1
flag = True

for q in range(Q):
    query = input().split()

    if query[0] == '1':
        s = query[1]
        stack.append(s)

        if s == ')':
            close_cnt += 1
        else:
            open_cnt += 1
        
        if flag == True and open_cnt < close_cnt:
            flag = False
            target = len(stack)

    else:
        s = stack.pop()

        if s == '(':
            open_cnt -= 1
        else:
            close_cnt -= 1

        if len(stack) == target-1:
            target = -1
            flag = True

    if flag == True and open_cnt == close_cnt:
        print('Yes')
    else:
        print('No')