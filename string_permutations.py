def permute_unique(s: str):
    res = []
    chars = sorted(list(s))  # sort to handle duplicates
    used = [False] * len(chars)

    def backtrack(path):
        if len(path) == len(chars):
            res.append("".join(path))
            return

        for i in range(len(chars)):
            # Skip used characters
            if used[i]:
                continue
            # Skip duplicates: if current char is same as previous and previous not used
            if i > 0 and chars[i] == chars[i - 1] and not used[i - 1]:
                continue

            used[i] = True
            path.append(chars[i])
            backtrack(path)
            path.pop()
            used[i] = False

    backtrack([])
    return res


# ---- Test cases ----
print(permute_unique("abc"))   # ["abc", "acb", "bac", "bca", "cab", "cba"]
print(permute_unique("aab"))   # ["aab", "aba", "baa"]
print(permute_unique("aaa"))   # ["aaa"]
print(permute_unique("a"))     # ["a"]
