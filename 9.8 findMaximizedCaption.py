from heapq import heappush,heappop
class Solution:
	def findMaximizedCapital(self, k, w, profits, capital):
		astlist = list(zip(profits,capital))
		astlist.sort(key=lambda x:x[1])
		big_root = []
		# 设置工作指针不重复的遍历项目
		work = 0
		for i in range(k):
			# heappush 过程
			while work < len(astlist) and astlist[work][1] <= w:
				heappush(big_root,-astlist[work][0])
				work += 1
			# heappop 过程
			if big_root:
				w += heappop(big_root) * (-1)
			else:
				return w
		return w