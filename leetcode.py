"""
✅ https://leetcode.com/problems/count-binary-substrings/description/
"""

# def count_binary(s:str) -> int:
#
#     group = s.replace("01", "0,1").replace("10", "1,0").split(",")
#
#     result = 0
#     for i in range(1,len(group)):
#          result += min(group[i-1:i+1])
#
#     return result


"""
✅ https://leetcode.com/problems/find-resultant-array-after-removing-anagrams/description/?envType=problem-list-v2&envId=string&difficulty=EASY
"""

# def removeAnagrams(words: list[str]) -> list[str]:
#     result = [words[0]]
#     for i in range(1,len(words)):
#         if sorted(words[i]) != sorted(result[-1]):
#             result.append(words[i])
#     return result
# words = ["abba","baba","bbaa","cd","cd"]
# print(removeAnagrams(words))


"""
✅ https://leetcode.com/problems/remove-trailing-zeros-from-a-string/description/?envType=problem-list-v2&envId=string&difficulty=EASY
"""

# def removeTrailingZeros(self, num: str) -> str:
#     return num.rstrip("0")


"""
✅ https://leetcode.com/problems/valid-palindrome-ii/description/?envType=problem-list-v2&envId=string&difficulty=EASY
"""

# def validPalindrome(self, s: str) -> bool:
#     if s == s[::-1]:
#         return True
#
#     smth = 1
#     i = 0
#     j = len(s)-1
#     while i < j:
#         if s[i] != s[j]:
#             smth1 = s[:i] + s[i+1:]
#             smth2 = s[:j] + s[j+1:]
#             return smth1 == smth1[::-1] or smth2 == smth2[::-1]
#         i += 1
#         j -= 1
#     return True


"""
✅ https://leetcode.com/problems/determine-color-of-a-chessboard-square/?envType=problem-list-v2&envId=string&difficulty=EASY
"""

# def squareIsWhite(self, coordinates: str) -> bool:
#     column = ord(coordinates[0]) - ord('a') + 1
#     row = int(coordinates[1])
#
#     if (column + row) % 2 == 0:
#         return False
#     else:
#         return True


"""
✅ https://leetcode.com/problems/check-balanced-string/?envType=problem-list-v2&envId=string&difficulty=EASY
"""

# num = "1234"
# even = 0
# odd = 0
# for i in range(len(num)):
#     if i % 2 == 0:
#         even += int(num[i])
#     else:
#         odd += int(num[i])
#
# print(even == odd)


"""
✅ https://leetcode.com/problems/minimum-time-to-type-word-using-special-typewriter/description/
"""

# word = "zjpc"
# pointer = "a"
# result = 0
# for char in word:
#     distance1 = abs(ord(pointer) - ord(char))
#     distance2 = 26-distance1
#     result += min(distance1 , distance2) + 1
#     pointer = char
# print(result)


"""
✅ https://leetcode.com/problems/divide-a-string-into-groups-of-size-k/description/
"""

# s = "abcdefghij"
# k = 3
# fill = "x"
# l=len(s)
# s = s + fill * ((k-l%k)%k)
# result = []
# for i in range(0 , l , k):
#     result.append(s[i:i+k])
# print(result)


"""
✅ https://leetcode.com/problems/shortest-completing-word/description/
"""

# licensePlate = "1s3 PSt"
# words = ["step","steps","stripe","stepple"]
# license = [char.lower() for char in licensePlate if char.isalpha()]
# count_lp = Counter(license)
# for word in words:
#     count_word = Counter(word.lower())
#     for tmp in license:
#         if all(count_word[tmp] >= count_lp[tmp]):
#             print()
#
# print(license)


# ============================================================

# s = "acb347g"
# stack = []
# for i in s:
#     if stack and i.isdigit():
#         stack.pop()
#     else:
#         stack.append(i)
# print("".join(stack))


# =========================================================

# nums = [3,2,1]
# result = set(nums)
# if len(result) < 3:
#     print(max(result))
# result.remove(max(result))
# result.remove(max(result))
# print(max(result))

# ===================================================

# nums = [1,2,3,2]
# result = 0
# for i in nums:
#     if i != i - 1:
#         result += i
# print(result)


# ========================================================

# 819

# paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
# banned = ["hit"]
# result = ""
# txt = paragraph.split()
# for i in range(len(txt)):
#     if txt[i] == txt[i - 1]:
#         result += txt[i]
#
# print(result)


# ==============================================================================

# nums1 = [1,2,3]
# nums2 = [2,4]
# i,j = 0,0
# while i < len(nums1) and j < len(nums2):
#     if nums1[i] == nums2[j]:
#         print(nums1[i])
#     elif nums1[i] < nums2[j]:
#         i += 1
#     else:
#         j += 1
#
# print(-1)


# ==================================================================


# salary = [4000,3000,1000,2000]
# min_salary = min(salary)
# max_salary = max(salary)
# salary.remove(min_salary)
# salary.remove(max_salary)
# smth = sum(salary) / len(salary)
# print(smth)

# ============================================

# nums = [5,1,5,2,5,3,5,4]
# smth = set()
# for i in nums:
#     if i in smth:
#         print(i)
#     smth.add(i)


# ==================================================


# num = input("Enter the number:")
#
# tmp = {
#     1000 : "M",
#     900  : "CM",
#     500  : "D",
#     400  : "CD",
#     100  : "C",
#     90   : "XC",
#     50   : "L",
#     40   : "XL",
#     10   : "X",
#     9    : "IX",
#     5    : "V",
#     4    : "IV",
#     1    : "I"
# }
# result = 0
# for i,j in tmp.items():
#     if tmp[i] > tmp[i+1]:
#         result += i
#     elif tmp[i] < tmp[i+1]:
#         result -= i
#     else:
#         result += i
# print(result)


# s = "abca"
#
# dictionary = {
#     'a' : 0,
#     'b' : 0,
#     'c' : 0
# }
#
# lst = []


# s = "5F3Z-2e-9-w"
# k = 4
# s = s.replace("-", "").upper()
# for i in range(1,len(s), k):


# =============================================================

# 459

# s = "abab"

# =============================================

# 1668

# sequence = "ababc"
# word = "ba"
# count = 0
# max_count = 0
#
# for i in range(len(sequence)):
#     while sequence[i:i + len(word)] == word:
#         count += 1
#         i += len(word)
#     max_count = max(max_count, count)
#     count = 0
# print(max_count)


# =================================

# 389

# s = "abcd"
# t = "abcde"

# result = 0
# for char in s + t:
#     result ^= ord(char)
# print(chr(result))


# ==============================================

# 1556

# n = 234
# result = str(n)[::-1]
# result1 = []
# for i in range(0,len(result),3):
#     result1.append(result[i:i+3])
# result2 = '.'.join(result1)[::-1]
# print(result2)

# ===========================================

# 551


# 2264


# 58

# s = "   fly me   to   the moon  "
#
# txt = s.strip().split(" ")
# print(len(txt[-1]))


# 1455

# sentence = "i love eating burger"
# searchWord = "burg"
# smth = sentence.split()
#
# for i,word in enumerate(smth):
#     if word.startswith(searchWord):
#         print(i+1)
# else:
#     print(-1)


# 482


# ==========================================================

# 242

# s = "rat"
# t = "car"
#
# if len(s) != len(t):
#     print(False)
# else:
#     result1 = sorted(s)
#     result2 = sorted(t)
#
#     if result1 == result2:
#         print(True)
#     else:
#         print(False)

# 344

# s = ["h","e","l","l","o"]
#
# s.reverse()
# print(s)

# ==============================================

# 434

# s = "Hello, my name is John"
# txt = s.strip().split(" ")
# print(len(txt))

# ================================================

# 520

# word = "FLaG"
# if word.isupper() or word.islower() or word.istitle():
#     print(True)
# else:
#     print(False)


# ====================================================

# 709

# s = "Hello"
# smth = ""
# for i in s:
#     if i.isupper():
#         smth += i.lower()
#     else:
#         smth += i
# print(smth)

# ============================================

# 929


# 1796

# def secondHighest(s: str) -> int:
#     digits = set()
#     for i in s:
#         if i.isdigit():
#             digits.add(int(i))
#
#     if len(digits) < 2:
#         return -1
#
#     result = sorted(digits, reverse=True)
#     return result[1]
# print(secondHighest("dg32fbqo"))

# 2129

# title = "capiTalIze tHe titLe"
# result = title.strip().split()
# for i in range(len(result)):
#     if i == 0 or i == len(result) - 1:
#         result[i] = result[i].capitalize()
#     elif len(result[i]) >= 4:
#         result[i] = result[i].capitalize()
#     else:
#         result[i] = result[i].lower()
# print(' '.join(result))


# ========================================

# 1903

# num = "52"
# for i in range(len(num)-1,-1,-1):
#     if int(num[i]) % 2 != 0:
#         print(num[:i+1])
# print("")

# =============================================

# d = {
#     "I": 1,
#     "V": 5,
#     "X": 10,
#     "L": 50,
#     "C": 100,
#     "D": 500,
#     "M": 1000
# }
# s = input(">>>")
# result = 0
# for i in range(len(s)-1):
#     j = d[s[i]]
#     result += -j if j < d[s[i+1]] else j
# result += d[s[-1]]
# print(result)

# ==================================================

# s = "5F3Z-2e-9-w"
# k = 3
# s = s.replace("-", "").upper()[::-1]
# slice_str = []
# for i in range(0 , len(s), k):
#     slice_str.append(s[i:i+k])
# print("-".join(slice_str)[::-1])

# =====================================================

# s = "cbzxy"
# d = {}
# maxi = -1
# for i , char in enumerate(s):
#     if char in d:
#         v = i - d[char] -1
#         maxi = max(v , maxi)
#     else:
#         d[char] = i
# print(maxi)


# word = "zjpc"
# d = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9, 'k': 10, 'l': 11, 'm': 12, 'n': 13, 'o': 14, 'p': 15, 'q': 16, 'r': 17, 's': 18, 't': 19, 'u': 20, 'v': 21, 'w': 22, 'x': 23, 'y': 24, 'z': 25}
# pointer = "a"
# result = 0
# for char in word:
#     distance1 = abs(d[pointer] - d[char])
#     distance2 = 26-distance1
#     result += min(distance1 , distance2) + 1
#     pointer = char
# print(result)


# word = "zjpc"
# pointer = "a"
# result = 0
# for char in word:
#     distance1 = abs(ord(pointer) - ord(char))
#     distance2 = 26-distance1
#     result += min(distance1 , distance2) + 1
#     pointer = char
# print(result)


# ========================================================

# s = "abcdefghij"
# k = 3
# fill = "x"
# l=len(s)
# s = s + fill * ((k-l%k)%k)
# result = []
# for i in range(0 , l , k):
#     result.append(s[i:i+k])
# print(result)


# ==================================================

# s = "acb347g"
# stack = []
# for i in s:
#     if stack and i.isdigit():
#         stack.pop()
#     else:
#         stack.append(i)
# print("".join(stack))


# ============================================================


# licensePlate = "1s3 PSt"
# words = ["step","steps","stripe","stepple"]
# license = ""
# for i in licensePlate:
#     if i.isalpha():
#         license += i
# license = licensePlate.lower()
#
# def counter(txt:str):
#     d = {}.fromkeys(txt, 0)
#     for i in txt:
#         d[i] += 1
#
#     return d
# license = counter(license)
# print(license)


# =========================================================

# nums = [3,2,1]
# result = set(nums)
# if len(result) < 3:
#     print(max(result))
# result.remove(max(result))
# result.remove(max(result))
# print(max(result))

# ===================================================

# nums = [1,2,3,2]
# result = 0
# for i in nums:
#     if i != i - 1:
#         result += i
# print(result)


# ========================================================

# 819

# paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
# banned = ["hit"]
# result = ""
# txt = paragraph.split()
# for i in range(len(txt)):
#     if txt[i] == txt[i - 1]:
#         result += txt[i]
#
# print(result)


# ==============================================================================

# nums1 = [1,2,3]
# nums2 = [2,4]
# i,j = 0,0
# while i < len(nums1) and j < len(nums2):
#     if nums1[i] == nums2[j]:
#         print(nums1[i])
#     elif nums1[i] < nums2[j]:
#         i += 1
#     else:
#         j += 1
#
# print(-1)


# ==================================================================


# salary = [4000,3000,1000,2000]
# min_salary = min(salary)
# max_salary = max(salary)
# salary.remove(min_salary)
# salary.remove(max_salary)
# smth = sum(salary) / len(salary)
# print(smth)

# ============================================

# nums = [5,1,5,2,5,3,5,4]
# smth = set()
# for i in nums:
#     if i in smth:
#         print(i)
#     smth.add(i)


# ==================================================


# 2605
# nums1 = [4,1,3]
# nums2 = [5,7]
# def minNumber(nums1: list[int], nums2: list[int]) -> int:
# smth = set(nums1) & set(nums2)
#
# if smth:
#     return min(smth)
# zxc = min(nums1), min(nums2)
# mini = min(zxc)
# maxi = max(zxc)
# return int(f"{mini}{maxi}")

# ======================================

# 896

# nums = [1,2,2,3]
# num2 = nums.copy()
# num2.sort()
# print(num2 == nums or num2[::-1] == nums)


# ==============================================================

# 1720

# encoded = [1,2,3]
# first = 1
# result = [first]
# for i in encoded:
#     result.append(result[-1]^i)
# print(result)

# ==========================================================

# 2496

# versioon 1

# def maximumValue(strs: list[str]) -> int:
#     return int(zxc) if (zxc:=max(strs, key=lambda x: int(x) if x.isdigit() else len(x))).isdigit() else len(zxc)
# print(maximumValue(["alic3","bob","3","4","00000"]))

# version 2

# strs = ["alic3","bob","3","4","00000"]
# maxi = max(strs, key=lambda x: int(x) if x.isdigit() else len(x))
# if maxi.isdigit():
#     print(int(maxi))
# else:
#     print(len(maxi))

# ================================================


# 812

# def largestTriangleArea(points: list[list[int]]) -> float:
# def area_triangle(point1, point2, point3):
#     x1, y1 = point1
#     x2, y2 = point2
#     x3, y3 = point3
#     result = 1 / 2 * abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2))
#     return result
#
# maxi = 0
# for points in combinations(points, 3):
#     maxi = max(area_triangle(*points), maxi)
# return maxi

# print(largestTriangleArea(points = [[0,0],[0,1],[1,0],[0,2],[2,0]]))
# ===============================================================

# 3300

# nums = [10,12,13,14]
# mini = float('inf')
# for n in nums:
#     n = str(n)
#     s = 0
#     for char in n:
#         s += int(char)
#     mini = min(mini,s)
# print(mini)

# ====================================================================

# from collections import Counter
#
# s1 = "this apple is sweet"
# s2 = "this apple is sour"
# result = []
#
# str1 = s1.split()
# str2 = s2.split()
#
# count1 = Counter(str1)
# count2 = Counter(str2)
#
# for i in str1:
#     if count1[i] == 1 and i not in count2:
#         result.append(i)
#
# for i in str2:
#     if count2[i] == 1 and i not in count1:
#         result.append(i)
# print(result)

# ============================================================

# emails = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
# sett = set()
# for i in emails:
#     local, domain = i.split('@')
#     local = local.split('+')[0]
#     local = local.replace('.','')
#
#     sett.add(local + '@' + domain)
#
# print(len(sett))

# =====================================================================

# 2716

# s = "baadccab"
# txt = set(s)
# print(len(txt))

# ==================================================================

# 989

# num = [1,2,0,0]
# k = 34
#
# result = 0
# for i in num:
#     result = result * 10 + i
# result += k
#
# smth = [int(i) for i in str(result)]
# print(smth)

# ==========================================================

# 1748

# from collections import Counter
#
# nums = [1,2,3,2]
# count = Counter(nums)
# total = 0
# for i,j in count.items():
#     if j == 1:
#         total += i
# print(total)

# ======================================================================

# from collections import Counter
#
# nums = [1,2,2,3,1,4]
# lst = Counter(nums)
# maxi = max(lst.values())
# count = 0
# for value in lst.values():
#     if value == maxi:
#         count += 1
# print(count)

# ==========================

# nums = [1,100]
# nums.sort()
# average = set()
# while len(nums) > 1:
#     smth = (nums.pop(0) + nums.pop()) / 2
#     average.add(smth)
# print(len(average))


# ==================================================================

# 2032

# from collections import Counter
#
# nums1 = [3,1]
# nums2 = [2,3]
# nums3 = [1,2]
# result = []
# counter = Counter(nums2) + Counter(nums2) + Counter(nums3)
# for i,j in counter.items():
#     if j > 1:
#         result.append(i)
# print(result)

# =======================================================

# 2108

# def firstPalindrome(words: list[str]) -> str:
#     for w in words:
#         if w == w[::-1]:
#             return w
#     return ""
# print(firstPalindrome(words = ["abc","car","ada","racecar","cool"]))

# ===============================================================


# 169

# nums = [2,2,1,1,1,2,2]
# d = {}
# for i in nums:
#     d[i] = d.get(i,0) + 1
# print(max(d.items(), key=lambda x : x[1])[0])

# 2099

# nums = [2,1,3,3]
# k = 2
# while len(nums) > k:
#     nums.remove(min(nums))
# print(nums)

# =======================================================

# 2744

# words = ["cd","ac","dc","ca","zz"]
# d = {}
# count = 0
# for i in words:
#     reverse = i[::-1]
#     if reverse in d.keys() and d.get(reverse,0) != 0:
#         d[reverse] = d.get(reverse,0) - 1
#         count += 1
#     else:
#         d[i] = d.get(i,0) + 1
# print(count)

# =============================================================

# numRows = 5
# result = [[1], [1,1]]
# if numRows <= 2:
#     print(result[:numRows])
# for i in range(numRows-2):
#     tmp = [1]
#     last_l = result[-1]
#     for j in range(len(last_l)-1):
#         tmp.append(sum(last_l[j:j+2]))
#     result.append(tmp + [1])
# print(result)

# ==================================================

# 414

# nums = [3,2,1]
# nums = sorted(set(nums),reverse=True)
# smth = nums[0] if len(nums) < 3 else nums[2]
# print(smth)

# ====================================================================

# 2154

# nums = [2,7,9]
# original = 4
# st = set(nums)
# while original in st:
#     original *= 2
# print(original)

# =============================================

# 2404

# from collections import Counter
#
# nums = [0,1,2,2,4,4,1]
# even_nums = []
# for i in nums:
#     if i % 2 == 0:
#         even_nums.append(i)
# if not even_nums:
#     print(-1)
# count = Counter(even_nums)
# max_frequent = max(count.values())


# ====================================================

# 1572

# mat = [[1,1,1,1],
#        [1,1,1,1],
#        [1,1,1,1],
#        [1,1,1,1]]
#
# matrix = len(mat)
# total = 0
# for i in range(matrix):
#     total += mat[i][i]
#     total += mat[i][matrix-i-1]
# if matrix % 2 == 1:
#     total -= mat[matrix // 2][matrix//2]
#
# print(total)

# ====================================

# 2828
#
# words = ["alice","bob","charlie"]
# s = "abc"
# result = ""
# for i in words:
#     result = result + i[0]
# if result == s:
#     print(True)
# else:
#     print(False)


# ======================================

# 3232

# nums = [5,5,5,25]
# one_digit = []
# two_digit = []
# for i in nums:
#     if 0 <= i < 10:
#         one_digit.append(i)
#     elif 10 <= i < 100:
#         two_digit.append(i)
#
# total = sum(nums)
#
# total1 = sum(one_digit)
# total2 = sum(two_digit)
#
# if total1 > total - total1 or total2 > total - total2:
#     print(True)
# else:
#     print(False)

# =================================================

# 2085

# from collections import Counter
#
# words1 = ["leetcode","is","amazing","as","is"]
# words2 = ["amazing","leetcode","is"]
# count1 = Counter(words1)
# count2 = Counter(words2)
# count = 0
# for i in count1:
#     if count1[i] == 1 and count2[i] == 1 :
#         count += 1
#
# print(count)

# ========================================

# 1790

# s1 = "attack"
# s2 = "defend"
#
# if s1 == s2:
#     print(True)
#
# lst = []
# for i in range(len(s1)):
#     if s1[i] != s2[i]:
#         lst.append(i)
# if len(lst) == 2:
#     i,j = lst
#     print(s1[i] == s2[j] and s1[j] == s2[i])


# ===========================================

# 1108

# address = "1.1.1.1"
# print(address.replace(".","[.]"))

# ===============================================

# 2114

# sentences = ["alice and bob love leetcode", "I think so too", "this is a great thanks very much"]
# result = 0
# for char in sentences:
#     smth = len(char.split())
#     result = max(result,smth)
# print(result)

# ==================================================

# 2042

"""s = "1 box has 3 blue 4 red 6 green and 12 yellow marbles"
words = s.split()
result = []
for i in words:
    if i.isdigit():
        result.append(int(i))
print(result)"""

# ====================================================

# 2788

# words = ["one.two.three","four.five","six"]
# separator = "."
# result = []
# for i in words:
#     txt = i.split(separator)
#     for j in txt:
#         if j:
#             result.append(j)
# print(result)

# ==============================================================

# 1816

# s = "Hello how are you Contestant"
# k = 4
# txt = s.split()
# smth = ' '.join(txt[:k])
# print(smth)

# ===============================================================================================

# 2733

# nums = [3,2,1,4]
# if len(nums) < 3:
#     print(-1)
# nums.sort()
# print(nums[1])

# ==============================================

# 1636

# from collections import Counter
#
# nums = [1,1,2,2,2,3]
# count = Counter(nums)
# smth = sorted(nums, key=lambda x: (count[x],-x))
# print(smth)

# =====================================================

# 3158

# from collections import Counter
#
# nums = [1,2,2,1]
# count = Counter(nums)
# result = 0
# for i,j in count.items():
#     if j == 2:
#         result ^= i
# print(result)

# ================================================

# 2441

# nums = [-1,2,-3,3]
# lst = set(nums)
# smth = -1
#
# for i in nums:
#     if i > 0 and -i in lst:
#         smth = max(smth,i)
# print(smth)

# =====================================================

# 2215

# nums1 = [1,2,3,3]
# nums2 = [1,1,2,2]
# set1 = set(nums1)
# set2 = set(nums2)
#
# print([list(set1-set2), list(set2-set1)])

# ==================================================

# 1394

# from collections import Counter
#
# arr = [2,2,3,4]
# counter = Counter(arr)
# for i in sorted(counter.keys(), reverse=True):
#     if counter[i] == i:
#         print(i)
# else:
#     print(-1)

# =======================================================

# 383

# ransomNote = "a"
# magazine = "b"
#
# print(not (Counter(ransomNote) - Counter(magazine)))


# 1260

# from itertools import chain
#
# grid = [[1,2,3],[4,5,6],[7,8,9]]
# k = 1
# col = len(grid[0])
# row = len(grid)
# if k > row*col:
#     k = k % (row*col)
# chain_matrix = list(chain(*grid))
# chain_matrix = chain_matrix[-k:] + chain_matrix[:-k]
# new_matrix = []
#
# for i in range(row):
#     new_matrix.append(chain_matrix[i*col:i*col+col])
# print(new_matrix)


# ===============================================================

# 2154

# nums = [5,3,6,1,12]
# original = 3
# st = set(nums)
# while original in st:
#     original *= 2
# print(original)

# ====================================================================

# 821

# s = "loveleetcode"
# c = "e"
# result = []
# for i,v in enumerate(s):
#     if v == c:
#         result.append(i)
#
# smth = []
# for i in range(len(s)):
#     smth.append(abs(i - min(result, key = lambda x : abs(x - i))))
# print(smth)

# ======================================================

# def areAlmostEqual( s1: str, s2: str) -> bool:
#
#     if s1 == s2:
#         return True
#
#     result = []
#
#     for i in range(len(s1)):
#         if s1[i] != s2[i]:
#             result.append(i)
#
#     if len(result) == 2:
#         i,j = result
#
#         return s1[i] == s2[j] and s1[j] == s2[i]
#     return False
# print(areAlmostEqual(s1 = "bank", s2 = "kanb"))

# =======================================

# 500

# first_row = set("qwertyuiop")
# second_row = set("asdfghjkl")
# third_row = set("zxcvbnm")
# words = ["Hello","Alaska","Dad","Peace"]
# result = []
# for word in words:
#     w_lower = word.lower()
#     if set(w_lower) & first_row == set(w_lower) or set(w_lower) & second_row == set(w_lower) or set(w_lower) & third_row == set(w_lower):
#         result.append(word)
# print(result)


# ===================================================================================

# 1678

# command = "G()(al)"
# txt = command.replace('()', 'o').replace('(al)','al')
# print(txt)

# ===============================================

# 2259

# number = "1231"
# digit = "1"
# result = ""
# found = False
# for i in range(len(number)):
#     if number[i] == digit and not found:
#         found = True
#         continue
#     result += number[i]
#
# print(result)

# =============================================

# 1935

# text = "hello world"
# brokenLetters = "ad"
# txt = text.split()
# count = 0
# for i in range(len(txt)):
#     for char in txt[i]:
#         if char not in brokenLetters:
#             count += 1
# print(count)

# =====================================================

# 1662

# word1 = ["ab", "c"]
# word2 = ["a", "bc"]
#
# txt1 = ''.join(word1)
# txt2 = ''.join(word2)
#
# if txt1 == txt2:
#     print(True)
# else:
#     print(False)

# ==================================================

# 412

# n = 15
# result = []
#
# for i in range(1, n + 1):
#     if i % 15 == 0:
#         result.append("FizzBuzz")
#     elif i % 5 == 0:
#         result.append("Buzz")
#     elif i % 3 == 0:
#         result.append("Fizz")
#     else:
#         result.append(str(i))
#
# print(result)

# =========================================================================

# 2089

# nums = [1,2,5,2,3]
# target = 2
# nums.sort()
# result = []
#
# for i in range(len(nums)):
#     if nums[i] == target:
#         result.append(i)
#
# print(result)

# ================================================================

# 1979

# nums = [2,5,6,9,10]
# st = set(nums)
# mini = min(st)
# maxi = max(st)
#
# for i in range(mini,0,-1):
#     if mini % i == 0 and maxi % i == 0:
#         print(i)
#     else:
#         print(1)


# ====================================================

# nums1 = [4,9,5]
# nums2 = [9,4,9,8,4]
#
# print(list(set(nums1) & set(nums2)))

# ========================================================

# 1929

# nums = [1,2,1]
# result = nums+nums
# print(result)

# ==============================================================

# 2347

# from collections import Counter
#
# ranks = [4,4,2,4,4]
# suits = ["d","a","a","b","c"]
# if len(set(suits)) == 1:
#     print("Flush")
#
# count = Counter(ranks)
# max_count = max(count.values())
#
# if max_count >= 3:
#     print("Three of a Kind")
# elif max_count == 2:
#     print("Pair")
# else:
#     print("High Card")


# ==========================================================

# 2423

# from collections import Counter
#
# word = "abcc"
# count = Counter(word)

# ==============================================================

# 575

# candyType = [1,1,2,3]
# result = len(candyType) // 2
# for i in candyType:
#
# print(result)


# ==================================================================

# 922

# nums = [4,2,5,7]
# result = []
# odd_nums = []
# even_nums = []
# for i in range(len(nums)):
#     if nums[i] % 2 == 0:
#         even_nums.append(nums[i])
#     else:
#         odd_nums.append(nums[i])
#
# for x in range(len(odd_nums)):
#     result.append(even_nums[x])
#     result.append(odd_nums[x])
# print(result)

# =======================================================================


# 3280

# date = "2080-02-29"
# smth = date.split('-')
# result = []
# for i in smth:
#     result.append(bin(int(i))[2:])
# print("-".join(result))

# 2315

# s = "yo|uar|e**|b|e***au|tifu|l"
# count = 0
# smth = False
# for i in s:
#     if i == '|':
#         smth = not smth
#     elif i == '*' and not smth:
#         count += 1
#
# print(count)

# 1752

# nums = [3,4,5,1,2]
# nums.append(nums[0])
# count = 0
# for i in range(len(nums)-1):
#     if nums[i] > nums[i+1]:
#         count += 1
#         if count > 1:
#             print(False)
#             break
# else:
#     print(True)


# ==========================================================

# 3238

# n = 4
# pick = [[0,0],[1,0],[1,0],[2,1],[2,1],[2,0]]

# 1672

# accounts = [[1,5],[7,3],[3,5]]
# print(max(map(sum,accounts)))

# 1582

# mat = [[1,0,0],[0,0,1],[1,0,0]]
#
#
#
# count = 0
# for i in range(len(mat)):
#     for j in range(len(mat[0])):
#         if mat[i][j] == 1:
#             count += 1
# print(count)


# =======================================================================

# 1961

# s = "iloveleetcode"
# words = ["apple", "i","love","leetcode"]
#
# for i in range(1,len(s) + 1):
#     if s == ''.join(words[:i]):
#         print(True)
# else:
#     print(False)


# 1967

# patterns = ["a","abc","bc","d"]
# word = "abc"
# count = 0
#
# for i in range(len(patterns)):
#     if patterns[i] in word:
#         count += 1
#
# print(count)


# 28

# haystack = "sadbutsad"
# needle = "sad"


# 125

# s = "0P"
# res = ""
# for i in s:
#     if i.isalnum():
#         res += i.lower()
#
# if res == res[::-1]:
#     print(True)
# else:
#     print(False)


# 345

# s = "IceCreAm"
# vowels = 'AEUIOaeuio'
# res = ""
# for i in s:
#     if i in vowels:
#         res += i
#
# print(res[::-1])

# 392

# s = "abc"
# t = "ahbgdc"
#
# for i in range(len(s)):
#     if


"""✅ https://leetcode.com/problems/kth-distinct-string-in-an-array/description/?envType=problem-list-v2&envId=string"""

# arr = ["d","b","c","b","c","a"]
# k = 2
# smth = [i for i in arr if arr.count(i) == 1]
# print("")if len(smth) < k else print(smth[k-1])


"""✅ https://leetcode.com/problems/unique-morse-code-words/description/?envType=problem-list-v2&envId=string"""

# words = ["gin","zen","gig","msg"]
# tmp = ""
# lst = []
# dct = {'a':".-", 'b':"-...", 'c':"-.-.", 'd':"-..", 'e':".",
#            'f':"..-.", 'g':"--.", 'h':"....", 'i':"..", 'j':".---",
#            'k':"-.-", 'l':".-..", 'm':"--", 'n':"-.", 'o':"---", 'p':".--.",
#            'q':"--.-", 'r':".-.", 's':"...", 't':"-", 'u':"..-", 'v':"...-",
#            'w':".--", 'x':"-..-", 'y':"-.--", 'z':"--.."}
# for word in words:
#     for letter in word:
#         tmp += dct[letter]
#     lst.append(tmp)
#     tmp = ''
#
# print(len(set(lst)))

"""✅ https://leetcode.com/problems/find-common-characters/description/?envType=problem-list-v2&envId=string"""

# words = ["bekka","label","roller"]
# result = []
# if len(words) < 2:
#     for word in words:
#         for i in word:
#             result.append(i)
# else:
#     word = set(words[0])
#     for char in word: # a ,b e , l
#         smth = min([word.count(char) for word in words])
#         result += [char] * smth
# print(result)


"""✅ https://leetcode.com/problems/maximum-number-of-balloons/description/"""

# text = "nlaebolkoballoondfgwr"
# print(min(text.count('b'),text.count('a'),text.count('l')//2,text.count('o')//2,text.count('n')))


"""✅ https://leetcode.com/problems/island-perimeter/description/"""

# grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
# a = len(grid)
# b = len(grid[0])
# res = 0
# for i in range(a):
#     for j in range(b):
#         if grid[i][j] == 1:
#             if (j > 0 and grid[i][j-1] == 0) or j == 0:
#                 res += 1
#             if (i > 0 and grid[i-1][j] == 0) or i == 0:
#                 res += 1
#             if (j < b - 1 and grid[i][j-1] == 0) or j == b - 1:
#                 res += 1
#             if (i < a - 1 and grid[i-1][j] == 0) or i == a - 1:
#                 res += 1
#
# print(res)


"""✅ https://leetcode.com/problems/relative-ranks/description/"""

# score = [10,3,8,9,4]
# temp = sorted(score, reverse=True)
# lst = []
# for i in score:
#     rank = temp.index(i) + 1
#     if rank == 1:
#         lst.append("Gold Medal")
#     elif rank == 2:
#         lst.append("Silver Medal")
#     elif rank == 3:
#         lst.append("Bronze Medal")
#     else:
#         lst.append(str(rank))
#
# print(lst)


"""
✅ https://leetcode.com/problems/longest-common-prefix/
"""

# strs = ["flower", "flow", "flight"]
# tmp = ''
# result = ''
# word = min(strs, key=len)
# for i in range(len(word)):
#     for str in strs:
#         if str[i] == word[i]:
#             tmp += str[i]
#     if len(tmp) < len(strs):
#         break
#     result += tmp[0]
#     tmp = ''
# print(result)


"""
✅ https://leetcode.com/problems/move-zeroes/
"""

# nums = [0,1,0,3,12]
# for i in nums:
#     if i == 0:
#         nums.append(0)
#         nums.remove(0)
# print(nums)

"""
✅ https://leetcode.com/problems/excel-sheet-column-number/description/
"""

# letters = string.ascii_uppercase
# dct = {}
# for index, value in enumerate(letters):
#     dct[value] = index + 1
#
# res = 0
# columnTitle = "A"
# i = len(columnTitle)-1
# for column in columnTitle:
#     temp = dct[column]
#     res += temp * (26 ** i)
#     i -= 1
#
# print(res)


"""
✅ https://leetcode.com/problems/duplicate-zeros/description/
"""

# arr = [8,5,0,9,0,3,4,7]
# cut = len(arr)
# i = 0
# while i <= cut-2:
#     if arr[i] == 0:
#         arr.insert(i+1, 0)
#         i += 2
#     else:
#         i += 1
# print(arr[:cut])


"""
✅ https://leetcode.com/problems/find-the-town-judge/description/
"""

# n = 4
# trust = [[1,3],[1,4],[2,3],[2,4],[4,3]]
# if n == 1:
#     print(n)
# elif n == 2 and len(trust) == 0:
#     print(-1)
# else:
#     first = [t[0] for t in trust]
#     second = [t[1] for t in trust]
#
#     temp = Counter(second)
#     max_voice = max(temp, key=temp.get)
#     num_of_voices = temp.get(max_voice)
#
#     if num_of_voices == n-1 and max_voice not in first:
#         print(max_voice)
#     else:
#         print(-1)


"""
✅ https://leetcode.com/problems/score-of-a-string/description/
"""

# s = "hello"
# print(sum(abs(ord(s[char]) - ord(s[char + 1])) for char in range(len(s) - 1)))


"""
✅ https://leetcode.com/problems/divisible-and-non-divisible-sums-difference/description/
"""

# n = 10
# m = 3
# lst = list(range(1, n + 1))
# lst1 = [i for i in lst if i % m == 0]
# lst2 = [i for i in lst if i % m != 0]
# print(sum(lst2) - sum(lst1))


"""
✅ https://leetcode.com/problems/find-the-maximum-achievable-number/description/
"""

# num = 4
# t = 1
# print(num + 2 * t)


"""
✅ https://leetcode.com/problems/find-words-containing-character/description/
"""

# words = ["abc","bcd","aaaa","cbc"]
# x = "a"
# temp = [i for i, word in enumerate(words) if x in word]
# print(temp)


"""
✅ https://leetcode.com/problems/convert-the-temperature/description/
"""
# Kelvin = Celsius + 273.15
# Fahrenheit = Celsius * 1.80 + 32.00

# celsius = 36.50
# res = [celsius + 273.15, celsius * 1.80 + 32.00]
# print(res)


"""
✅ https://leetcode.com/problems/power-of-two/
"""

# 2**4 = 16
# m = 0
# if m <= 0:
#     print(False)
# smth = int(math.log2(m))
# if 2 ** smth == m:
#     print(True)
# else:
#     print(False)


"""
✅ https://leetcode.com/problems/partition-array-according-to-given-pivot/description/
"""

# nums = [9, 12, 5, 10, 14, 3, 10]
# pivot = 10
# lst1 = [i for i in nums if i > pivot]
# lst2 = [i for i in nums if i < pivot]
# lst3 = [i for i in nums if i == pivot]
# print(lst2 + lst3 + lst1)


"""
✅ https://leetcode.com/problems/transform-array-by-parity/description/
"""

# nums = [4,3,2,1]
# res = []
# for n in nums:
#     if n % 2 == 0:
#         res.append(0)
#     else:
#         res.append(1)
# print(sorted(res))


"""
✅ https://leetcode.com/problems/final-value-of-variable-after-performing-operations/description/
"""

# operations = ["X++","++X","--X","X--"]
# res = 0
# dct = {
#     'X--' : -1,
#     '--X' : -1,
#     'X++' : 1,
#     '++X' : 1,
# }
# for op in operations:
#     res += dct[op]
#
# print(res)


"""
✅ https://leetcode.com/problems/divisor-game/description/
"""

# class Solution:
#     def divisorGame(self, n: int) -> bool:
#         return n % 2 == 0


"""
✅ https://leetcode.com/problems/sqrtx/description/
"""

# x = 4
# print(int(sqrt(4)))


"""
✅ https://leetcode.com/problems/jewels-and-stones/description/
"""

# jewels = "aA"
# stones = "aAAbbbb"
# set_jewels = set(jewels)
# print(sum(s in set_jewels for s in stones))


"""
✅ https://leetcode.com/problems/shuffle-the-array/description/
"""

# nums = [2,5,1,3,4,7]
# n = 3
# res = []
# x = nums[:n]
# y = nums[n:]
#
# for i in range(n):
#     res.append(x[i])
#     res.append(y[i])
#
# print(res)


"""
✅ https://leetcode.com/problems/the-two-sneaky-numbers-of-digitville/description/
"""

# nums = [0,3,2,1,3,2]
# res = []
# count_nums = Counter(nums)
# print(count_nums)
# for n in count_nums.items():
#     if n[1] == 2:
#         res.append(n[0])
#
# print(sorted(res))

"""
✅ https://leetcode.com/problems/count-the-number-of-consistent-strings/description/
"""

# allowed = "ab"
# words = ["ad", "bd", "aaab", "baa", "badab"]
# count = 0
# for word in range(len(words)):
#     temp1 = set(words[word])
#     temp2 = set(allowed)
#     if temp1.issubset(temp2):
#         count += 1
# print(count)


"""
✅ https://leetcode.com/problems/smallest-even-multiple/description/
"""

# n = 5
# print((n*2) // math.gcd(n, 2))


"""
✅ https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/description/
"""

# candies = [4,2,1,1,2]
# extraCandies = 1
# res = []
# for candy in range(len(candies)):
#     if (candies[candy] + extraCandies) >= max(candies):
#         res.append(True)
#     else:
#         res.append(False)
# print(res)


"""
✅ https://leetcode.com/problems/add-two-integers/description/
"""

# num1 = -10
# num2 = 4
# print(num1+num2)


"""
✅ https://leetcode.com/problems/find-most-frequent-vowel-and-consonant/description/
"""

# s = "successes"
# counter = Counter(s)
# vowels = 'aeiou'
# max_vowels = max([counter[i] for i in vowels], default=0)
# max_consonants = max([counter[i] for i in counter if i not in vowels], default=0)
# print(max_vowels+max_consonants)


"""
✅ https://leetcode.com/problems/number-of-employees-who-met-the-target/description/
"""

# hours = [5, 1, 4, 2, 2]
# target = 6
# print(len([hour for hour in hours if hour >= target]))

"""
✅ https://leetcode.com/problems/reverse-degree-of-a-string/description/
"""

# s = "zaza"
# letters = reversed(string.ascii_lowercase)
# dct = {}
# total = 0
# for index, value in enumerate(letters):
#     dct[value] = index + 1
# for index, value in enumerate(s):
#     total += dct.get(value) * (index + 1)
#
# print(total)


"""
✅ https://leetcode.com/problems/count-integers-with-even-digit-sum/description/
"""

# num = 30
# count = 0
# for n in range(1, num+1):
#     if n < 9 and n % 2 == 0:
#         count += 1
#     elif n > 9:
#         res = str(n)
#         summ = 0
#         for t in res:
#             summ += int(t)
#         if summ % 2 == 0 :
#             count += 1
#
# print(count)


"""
✅ https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/description/
"""

# nums = [8, 1, 2, 2, 3]
# lst = [sorted(nums).index(i) for i in nums]
# print(lst)


"""
✅ https://leetcode.com/problems/minimum-operations-to-make-array-sum-divisible-by-k/description/
"""

# nums = [3, 9, 7]
# k = 5
# print(sum(nums) % k)


"""
✅ https://leetcode.com/problems/running-sum-of-1d-array/description/
"""

# nums = [1, 2, 3, 4]
# lst = []
# for num in range(len(nums)):
#     lst.append(sum(nums[:num + 1]))
#
# print(lst)

# print([sum(nums[:num + 1]) for num in range(len(nums))])


"""
✅ https://leetcode.com/problems/separate-the-digits-in-an-array/
"""

# nums = [13,25,83,77]
# res = []
# for num in nums:
#     if num > 9:
#         for i in str(num):
#             res.append(int(i))
#     else:
#         res.append(num)
#
# print(res)


"""
https://leetcode.com/problems/difference-between-element-sum-and-digit-sum-of-an-array/
"""

# nums = [1,15,6,3]
# res = []
# for num in nums:
#     if num > 9:
#         for i in str(num):
#             res.append(int(i))
#     else:
#         res.append(num)
#
# print(abs(sum(nums)-sum(res)))


"""
https://leetcode.com/problems/find-closest-person/description/
"""

# x = 2
# y = 5
# z = 6
#
# if abs(x - z) < abs(y - z):
#     print(1)
# elif abs(y - z) < abs(x - z):
#     print(2)
# else:
#     print(0)
#
# print(1 if abs(x - z) < abs(y - z) else 2 if abs(y - z) < abs(x - z) else 0)


"""
https://leetcode.com/problems/restore-finishing-order/description/
"""

# order = [3,1,2,5,4]
# friends = [1,3,4]
#
# result = []
# for i in order:
#     if i in friends:
#         result.append(i)
#
# print(result)


"""
https://leetcode.com/problems/number-of-good-pairs/description/
"""

# nums = [1,2,3,1,1,3]
# count = {}
# res = 0
# for i in nums:
#     if i in count:
#         res += count[i]
#         count[i] += 1
#     else:
#         count[i] = 1
#
# print(res)


"""
https://leetcode.com/problems/compute-alternating-sum/description/
"""

# nums = [1,3,5,7]
# result = 0
# for i in range(len(nums)):
#     if i % 2 == 0:
#         result += nums[i]
#     else:
#         result -= nums[i]
#
# print(result)
# print(sum(num if i % 2 == 0 else -num for i, num in enumerate(nums)))


"""
https://leetcode.com/problems/generate-binary-strings-without-adjacent-zeros/description/
"""

# def validStrings(self, n: int) -> str:
#     res = []
#
#     def func(a, b, last_char):
#         if a == n:
#             res.append(b)
#             return
#         func(a + 1, b + '1', '1')
#         if last_char != '0':
#             func(a + 1, b + '0', '0')
#
#     func(0, '', '')
#     return res


"""
https://leetcode.com/problems/permutation-difference-between-two-strings/description/
"""

# s = "abc"
# t = "bac"
# t1 = {}
# for i, char in enumerate(t):
#     t1[char] = i
# difference = 0
# for i, char in enumerate(s):
#     difference += abs(i - t1[char])
# print(difference)


"""
https://leetcode.com/problems/group-the-people-given-the-group-size-they-belong-to/description/
"""

# groupSizes = [3,3,3,3,3,1,3]
# res = []
# cnt = defaultdict(list)
# for person, size in (enumerate(groupSizes)):
#     cnt[size].append(person)
#     if len(cnt[size]) == size:
#         res.append(cnt[size])
#         cnt[size] = []
# print(res)


"""
https://leetcode.com/problems/minimum-number-of-moves-to-seat-everyone/description/
"""

# seats = [3,1,5]
# students = [2,7,4]
# count = 0
# seats.sort()
# students.sort()
# for s, t in zip(students, seats):
#     count += abs(s - t)
# print(count)


"""
https://leetcode.com/problems/split-a-string-in-balanced-strings/description/
"""

# s = "RLRRLLRLRL"
# count = 0
# balance = 0
# for i in s:
#     if i == 'L':
#         balance += 1
#     else:
#         balance -= 1
#
#     if balance == 0:
#         count += 1
# print(count)


"""
https://leetcode.com/problems/final-array-state-after-k-multiplication-operations-i/description/
"""

# nums = [2, 1, 3, 5, 6]
# k = 5
# multiplier = 2
# for _ in range(k):
#     idx = nums.index(min(nums))
#     nums[idx] *= multiplier
#
# print(nums)


"""
https://leetcode.com/problems/find-center-of-star-graph/description/
"""

# edges = [[1, 2], [5, 1], [1, 3], [1, 4]]
# u1, v1 = edges[0]
# u2, v2 = edges[1]
# if u1 == u2 or u1 == v2:
#     print(u1)
# else:
#     print(v1)



