class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        l = len(endWord)

        ws = set(wordList)

        head = {beginWord}
        tail = {endWord}
        tmp = list('abcdefghijklmnopqrstuvwxyz')
        res = 1
        while head:
            if len(head) > len(tail):
                head, tail = tail, head

            q = set()
            for cur in head:
                for i in range(l):
                    for j in tmp:
                        word = cur[:i] + j + cur[i + 1:]

                        if word in tail:
                            return res + 1

                        if word in ws:
                            q.add(word)
                            ws.remove(word)
            head = q
            res += 1

        return 0
"""
这道题，简单来说就是求图的两点最短路径，每个单词是一个点，只有相差一个字符的点之间才有路径，路径权值全部为1.

一开始递归深度遍历，超时。看来测试用例的数量级还是比较大。

修改，非递归，加节点访问map，依然超时。

再修改，广度遍历。

将第一个单词节点加入队列，并设置这个节点的值为1
从队列取出一个单词节点开始，遍历列表，遇到符合条件的节点，那么这个节点的路径值等于前一个节点值+1
将符合条件的单词节点加入队列。
队列为空结束
返回endWord的节点值即可。
结果遇到了一个长度4535的测试用例，又超时。

再看，感觉判断两个单词是否符合条件的方式会耗时很久，每一位比较，每一轮都要比较很多次。

反正都是小写字母，每次只变动一位，干脆拿到一个节点时生成所有可能的下一个节点，新生成的节点只要再列表中就参与计算。

这次终于通过了，不过耗时几百毫秒。

再想怎么优化，发现这个变化，正向反向都一样，耗时久都在新节点的处理上，那么正，反无所谓，每次都只遍历节点最少的中间队列，降低节点计算。

这次终于迈进100毫秒以内了。
"""