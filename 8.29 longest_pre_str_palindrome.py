def longest_palindrome_prefix(s):
    if not s:
        return 0
    s = s + '#' + s[::-1] + '$'
    i = 0
    j = -1
    nt = [0] * len(s)
    nt[0] = -1
    while i < len(s) - 1:
        if j == -1 or s[i] == s[j]:
            i += 1
            j += 1
            nt[i] = j
            # print(nt)
        else:
            j = nt[j]
            # print(nt)
    return nt[len(s) - 1]

def pre_to_ans(k,s):
    print(k)
    print(s[:k-1:-1])
    print(s[k])
    return s[:k-1:-1]+s


strt = "abcd"
print(pre_to_ans(longest_palindrome_prefix(strt), strt))