class Solution:
    def topological_sort(self, items, indegree, neighbors):
        # 建立队列和访问顺序
        queue = collections.deque()
        res = []

        # 初始化队列
        for item in items:
            if not indegree[item]:
                queue.append(item)

        if not queue: return []

        # BFS
        while queue:
            cur = queue.popleft()
            res.append(cur)

            # 遍历邻居节点
            for neighbor in neighbors[cur]:
                indegree[neighbor] -= 1
                if not indegree[neighbor]:
                    queue.append(neighbor)

        return res

    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        max_group_id = m
        for task in range(n):
            if group[task] == -1:
                group[task] = max_group_id
                max_group_id += 1

        task_indegree = [0] * n
        group_indegree = [0] * max_group_id
        task_neighbors = [[] for _ in range(n)]
        group_neighbors = [[] for _ in range(max_group_id)]
        group_to_tasks = [[] for _ in range(max_group_id)]

        for task in range(n):
            group_to_tasks[group[task]].append(task)

            for prerequisite in beforeItems[task]:

                # 判断相关联的两个项目是否属于同一组
                if group[prerequisite] != group[task]:

                    # 不是同组，给小组建图
                    group_indegree[group[task]] += 1
                    group_neighbors[group[prerequisite]].append(group[task])
                else:
                    # 同组，给组内项目建图
                    task_indegree[task] += 1
                    task_neighbors[prerequisite].append(task)

        res = []

        # 得到小组的访问顺序
        group_queue = self.topological_sort([i for i in range(max_group_id)], group_indegree, group_neighbors)

        if len(group_queue) != max_group_id: return []

        for group_id in group_queue:
            # 得到每组项目的访问顺序
            task_queue = self.topological_sort(group_to_tasks[group_id], task_indegree, task_neighbors)

            if len(task_queue) != len(group_to_tasks[group_id]):
                return []
            res += task_queue

        return res
"""
公司共有 n 个项目和  m 个小组，每个项目要不无人接手，要不就由 m 个小组之一负责。

group[i] 表示第 i 个项目所属的小组，如果这个项目目前无人接手，那么 group[i] 就等于 -1。（项目和小组都是从零开始编号的）小组可能存在没有接手任何项目的情况。

请你帮忙按要求安排这些项目的进度，并返回排序后的项目列表：

同一小组的项目，排序后在列表中彼此相邻。
项目之间存在一定的依赖关系，我们用一个列表 beforeItems 来表示，其中 beforeItems[i] 表示在进行第 i 个项目前（位于第 i 个项目左侧）应该完成的所有项目。
如果存在多个解决方案，只需要返回其中任意一个即可。如果没有合适的解决方案，就请返回一个 空列表 。
"""