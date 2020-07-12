def wordPatternMatch(p, s) -> bool:
    map_ = {}
    p_len = len(p)
    s_len = len(s)

    def helper(p_idx, s_idx):

        # exit condition
        if p_idx == p_len:
            return s_idx == s_len

        if p[p_idx] in map_:
            word = map_[p[p_idx]]
            if word == s[s_idx: s_idx + len(word)]:
                return helper(p_idx + 1, s_idx + len(word))
            else:
                return False

        else:
            for i in range(1, s_len - s_idx + 1):
                word = s[s_idx: s_idx + i]

                if word in map_.values():
                    continue

                map_[p[p_idx]] = word

                if helper(p_idx + 1, s_idx + len(word)):
                    return True

                del map_[p[p_idx]]


    return helper(0, 0)



print(wordPatternMatch("abab","redblueredblue"))
