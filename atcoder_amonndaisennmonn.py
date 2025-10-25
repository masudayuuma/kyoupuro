# N = int(input())
# A = list(map(int, input().split()))

# count_same_num = 0
# for i in range(1,len(A)):
#     if A[i] == A[i-1]:
#         count_same_num += 1
#         if count_same_num == 2:
#             print('Yes')
#             exit()
#     else:
#         count_same_num = 0
        
# print('No')
        
#A - Strictly Increasing?
# N = int(input())
# A = list(map(int, input().split()))
# for i in range(1, N):
#     if A[i-1] < A[i]:
#         continue
#     else:
#         print("No")
#         exit()
# print('Yes')

#A - 22222
# S = input()

# new_s = ""
# for i in range(len(S)):
#     if S[i] == '2':
#         new_s = new_s + '2'

# print(new_s)

#A - Poisonous Oyster
# S = list(map(str, input().split()))

# if S[0] == 'sick' and S[1] == 'sick':
#     print(1)
# elif S[0] == 'fine' and S[1] == 'sick':
#     print(3)
# elif S[0] == 'sick' and S[1] == 'fine':
#     print(2)
# else:
#     print(4)

#A - Shuffled Equation  / 
# A1, A2, A3 = map(int, input().split())
# if A1*A2 == A3:
#     print("Yes")
# elif A2*A3 == A1:
#     print("Yes")
# elif A1*A3 == A2:
#     print("Yes")
# else:
#     print("No")

#A - Hamming Distance
# N = int(input())
# S = input()
# T = input()
# count_diff = 0

# for i in range(N):
#     if S[i] == T[i]:
#         continue
#     else:
#         count_diff += 1

# print(count_diff)

#A - Lucky Direction
# D = input()

# if D == "N":
#     print("S")
# elif D == "E":
#     print("W")
# elif D == "W":
#     print("E")
# elif D == "S":
#     print("N")
# elif D == "NE":
#     print("SW")
# elif D == "NW":
#     print("SE")
# elif D == "SW":
#     print("NE")
# else:
#     print("NW")

#A - Is it rated?
# R, X = map(int, input().split())

# if X == 1 and 1600 <= R and R <= 2999:
#     print("Yes")
# elif  X == 2 and 1200 <= R and R <= 2399:
#     print("Yes")
# else:
#     print("No")

#A - Not Found
# S = input()

# a_to_z = list("abcdefghijklmnopqrstuvwxyz")

# for i in(a_to_z):
#     if not i in S:
#         print(i)
#         exit()


#A - Not Acceptable 
# A, B, C, D = map(int, input().split())

# if A > C:
#     print("Yes")
# elif A == C and B > D:
#     print("Yes")
# else:
#     print("No")

#A - Odd Position Sum
# N = int(input())
# A = list(map(int, input().split()))

# odd_sum = 0
# for a in range(N):
#     if a % 2 == 0:
#         odd_sum += A[a]

# print(odd_sum)


# A, B = map(int, input().split())

# if float(A/B) > A//B+0.5:
#     print(A//B+1)
# else:
#     print(A//B)

#A 
# N = int(input())
# T = input()
# A = input()

# for i in range(N):
#     if T[i] == A[i] and T[i] == 'o':
#         print("Yes")
#         exit()

# print("No")

#A - Unsupported Type
# N = int(input())
# A = list(map(int, input().split()))
# X = int(input())

# for i in A:
#     if X == i:
#         print("Yes")
#         exit()

# print("No")

# A - Sigma Cubes
# N = int(input())

# ans = 0
# for i in range(1, N+1):
#     # print(i)
#     ans += ((-1)**i)*(i**3)
#     # print(ans)

# print(ans)

# A - Isosceles
# a, b, c = map(int, input().split())

# if a == b or b == c or a == c:
#     print('Yes')
# else:
#     print('No')

# A - Scary Fee
# X, C = map(int, input().split())

# ans = X//(1000+C)

# print(ans*1000)

# A - OS Versions
# X, Y = input().split(' ')

# dict = {'Ocelot': 1, 'Serval': 2, 'Lynx': 3}

# if dict[X] >= dict[Y]:
#     print('Yes')
# else:
#     print('No')

# A - ABC -> AC
# s = input()
# hurf_l = len(s)//2
# print(s[:hurf_l]+s[len(s)-hurf_l:])

# A - Grandma's Footsteps
S, A, B, X = map(int, input().split())

warikiri = X//(A+B)
amari = X%(A+B)

ans = warikiri*S*A+S*min(amari, A)
print(ans)