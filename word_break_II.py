class Solution:
    def wordBreak2(self, s, wordDict):
        memo = {}

        def helper(rem):
            if rem in memo:
                return memo[s]
            if not rem:
                return []

            res = []
            for word in wordDict:
                if not rem.startswith(word):
                    continue
                if len(word) == len(rem):
                    res.append(word)
                else:
                    resultOfTheRest = helper(rem[len(word):])
                    for item in resultOfTheRest:
                        item = word + ' ' + item
                        res.append(item)
            memo[s] = res
            return res

        return helper(s)