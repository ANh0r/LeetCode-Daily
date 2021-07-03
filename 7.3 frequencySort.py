class Solution:
    def frequencySort(self, s: str) -> str:
        char_dict = {}
        # 更新字典
        for char in s:
            if char_dict.__contains__(char):
                char_dict[char] += 1
            else:
                char_dict.setdefault(char, 1)

        char_dict_list = sorted(char_dict.items(), key=lambda kv: (kv[1], kv[0]), reverse=True)
        final_str = ''
        for tup in char_dict_list:
            for i in range(tup[1]):
                final_str += tup[0]
        return final_str