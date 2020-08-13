import collections

class Solution:
    def originalDigits(self, s: str) -> str:
        # building hashmap letter -> its frequency
        count = collections.Counter(s)

        # building hashmap digit -> its frequency 
        out = {}
        # letter "z" is present only in "zero"
        out["0"] = count["z"]
        # letter "w" is present only in "two"
        out["2"] = count["w"]
        # letter "u" is present only in "four"
        out["4"] = count["u"]
        # letter "x" is present only in "six"
        out["6"] = count["x"]
        # letter "g" is present only in "eight"
        out["8"] = count["g"]
        # letter "h" is present only in "three" and "eight"
        out["3"] = count["h"] - out["8"]
        # letter "f" is present only in "five" and "four"
        out["5"] = count["f"] - out["4"]
        # letter "s" is present only in "seven" and "six"
        out["7"] = count["s"] - out["6"]
        # letter "i" is present in "nine", "five", "six", and "eight"
        out["9"] = count["i"] - out["5"] - out["6"] - out["8"]
        # letter "n" is present in "one", "nine", and "seven"
        out["1"] = count["n"] - out["7"] - 2 * out["9"]

        # building output string
        output = [key * out[key] for key in sorted(out.keys())]
        return "".join(output)

'''
构造单词和字母的一一映射，实在无法避免的可以先排除掉可能性之一然后继续映射

因此，我们需要寻找一些独特的标志。注意到，所有的偶数都包含一个独特的字母：

“z” 只在 “zero” 中出现。
“w” 只在 “two” 中出现。
“u” 只在 “four” 中出现。
“x” 只在 “six” 中出现。
“g” 只在 “eight” 中出现。
因此，从偶数开始是一个很好的思路。

这也是计算 3，5 和 7 的关键，因为有些单词只在一个奇数和一个偶数中出现（而且偶数已经被计算过了）：

“h” 只在 “three” 和 “eight” 中出现。
“f” 只在 “five” 和 “four” 中出现。
“s” 只在 “seven” 和 “six” 中出现。
接下来只需要处理 9和 0，思路依然相同。

“i” 在 “nine”，“five”，“six” 和 “eight” 中出现。
“n” 在 “one”，“seven” 和 “nine” 中出现。


'''