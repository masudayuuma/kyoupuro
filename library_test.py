from collections import Counter

nums = [1, 2, 2, 3, 3, 3]
c = Counter(nums)

s = "banana"
print(Counter(s))

c = 'banana'
print(c['a'])  # 3 （'a'の出現回数）
print(c['x'])  # 0 （存在しないキーでも0を返す）

print(c.most_common())      # [('a', 3), ('n', 2), ('b', 1)]
print(c.most_common(1))     # [('a', 3)] 上位1件
print(c.most_common(2))     # [('a', 3), ('n', 2)]

print(list(c.elements()))  # ['b', 'a', 'a', 'a', 'n', 'n']


from bisect import bisect_left, bisect_right

arr = [1,3,5,5,5,6,7] # 昇順にソートされている必要がある
l = bisect_left(arr, 5)  # 5が入るべき境目のうち最も左側の境目を返す
r = bisect_right(arr, 5)  # 5が入るべき境目のうち最も左側の境目を返す
print(l, r) # "2 5" が出力される


