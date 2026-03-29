#1
# class Solution:
#     def hasDuplicate(self, nums: List[int]) -> bool:
#         ans = set()
#         flag = False
#         for i in nums:
#             if i in ans:
#                 flag = True
#                 break
#             else:
#                 ans.add(i)
#         return flag

#2
# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         from collections import Counter
#         s_dict = Counter(s)
#         t_dict = Counter(t)
#         if s_dict == t_dict:
#             return True
#         else:
#             return False
