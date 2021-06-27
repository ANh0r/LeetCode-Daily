class Solution:
    def numBusesToDestination(self, routes: List[List[int]], S: int, T: int) -> int:
        ### station is the target, no need to take bus
        if (S == T):
            return 0

        ### encode routes with unique IDs
        ### build graph: mapping route IDs to stops
        graph = collections.defaultdict(list)
        for i in range(len(routes)):
            for stop in routes[i]:
                graph[stop].append(i)
        # print(graph)

        ### initialize
        ### search occurs among graph, routes, queue
        ### graph: stops ---> routes
        ### routes: rountes ---> stops
        ### queue: current stops

        ### search logic:
        ### stop A --->
        ###            route S passing stop A
        ###            (extracted from graph)
        ###                                   ---> other stops on rounte S
        ###                                        (extracted from rountes)
        ###                                                          ----> | if target not found
        ###                                                                |
        ### looping until target is identified <---------------------------|

        visited = set()
        queue = deque()
        queue.append(S)
        cnt_buses = 0

        while queue:
            size = len(queue)
            cnt_buses += 1
            ### a new loop means 1 more bus exchange, since current bus route does NOT contain target station

            for i in range(size):
                cur = queue.popleft()

                for line in graph[cur]:
                    if line not in visited:
                        visited.add(line)

                        for s in routes[line]:
                            if s == T:
                                return cnt_buses
                            queue.append(s)
        return -1