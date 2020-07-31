class Solution(object):
	def strToInt(self, str):
		if not str:
			return 0
		n = len(str)
		res = 0
		i = 0
		# 第一步，跳过前面若干个空格
		while i<n and str[i]==' ':
			i += 1
		# 如果字符串全是空格直接返回
		if i==n:
			return 0
		# 第二步，判断正负号
		is_negative = True if str[i]=='-' else False
		# 如果是正负号，还需要将指针i，跳过一位
		if str[i] in ('-','+'):
			i += 1
		# 第三步，循环判断字符是否在 0~9之间
		while i<n and str[i]>='0' and str[i]<='9':
			# '0'的ASCII码是48，'1'的是49，这么一减就从就可以得到真正的整数值
			tmp = ord(str[i])-ord('0')
			# 判断是否大于 最大32位整数
			if not is_negative and (res>214748364 or (res==214748364 and tmp>=7)):
				return 2147483647
			# 判断是否小于 最小32位整数
			if is_negative and (-res<-214748364 or (-res==-214748364 and tmp>=8)):
				return -2147483648
			res = res*10 + tmp
			i += 1
		# 如果有负号标记则返回负数
		return -res if is_negative else res


s = Solution()
print(s.strToInt("-32322132141"))