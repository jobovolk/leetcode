#387-first-unique-char-in-str
#this is correct, I believe, but failed the speed test on a very long string

import time

start_time = time.time()
class Solution:
    def firstUniqChar(self, s: str) -> int:
        for char in s:
            fi = s.find(char)
            li = s.rfind(char)

            if fi != li:
                return fi
            else:
                return 0
        return -1

s = Solution()
print(s.firstUniqChar("leetcode"))
print("should be 0")
print(s.firstUniqChar("loveleetcode"))
print("should be 2")
print(s.firstUniqChar("aabb"))
print("should be -1")

