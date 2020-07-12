from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDict = set(wordDict)
        memo = {}

        def helper(rem):
            if rem == '' or rem in wordDict:
                return True

            for i in range(len(rem)):
                if rem[0:i] in wordDict:
                    search = rem[i:]
                    if search not in memo:
                        memo[search] = helper(search)

                    if memo[search]:
                        return True

            return False

        return helper(s)