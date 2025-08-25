# https://www.sejuku.net/blog/49951
# python基本文法まとめて解説

'''
print("コメントテスト1")
print("コメントテスト2")
print("コメントテスト3”)
'''

#辞書
fruits = {"apple":2, "orange":3, "melon":5}
print(fruits["apple"])


#https://qiita.com/yamadagenki/items/4ef889964b18dfe90329
#プログラミング初心者に確実に押さえておいて欲しい文法一覧（技術面接対策用）
str1 = "Hello, "
str2 = "World!"
resutl = str1 + str2

S = "example"
print(S[0])
print(S[1])

number = 15
if number >= 10:
    print("10以上です")
else:
    print("10未満です")

age = 20
country = "Japan"
if age >= 18 and country == "Japan":
    print("条件を満たしています")
else:
    print("条件を満たしていません")

if age >= 18 or country == "Japan":
    print("条件を満たしています")
else:
    print("条件を満たしていません")

for i in range(5):
    print(i)

def double(number):
    result = number * 2
    return result

print(double(5))



############################################################################################################################
# a = int(input())
# b = int(input())
# print(a + b)

# n = int(input())
# if n % 2 == 0:
#     print("even")
# else:
#     print("odd")

# n = int(input())
# total = 0
# for i in range(n):
#     total += i
# print(total)

# nums = list(map(int, input().split()))
# print(max(nums))

# s = input()
# print(s[::-1])

# def is_even(n):
#     return n%2 == 0

# x = int(input())
# if is_even(x):
#     print("even")
# else:
#     print("odd")

# s = input()
# counter = {}
# for c in s:
#     if c in counter:
#         counter[c] += 1
#     else:
#         counter[c] = 1
# print(counter)

# d = {"apple" : 100, "banana" : 200}
# print(d["apple"])

# s = set([1, 2, 3, 3])
# s.add(4)
# print(s)

# nums = list(map(int, input().split()))
# even_nums = [x for x in nums if x % 2 == 0]
# print(even_nums)


