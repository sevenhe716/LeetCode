# Time:  O(n)
# Space: O(1)

# 解题思路：
#

class Solution:
    def possibleBipartition(self, N, dislikes):
        """
        :type N: int
        :type dislikes: List[List[int]]
        :rtype: bool
        """

        dicts = []
        for _ in range(N):
            dicts.append(set())

        A, B = set(), set()

        for d in dislikes:
            d[0] -= 1
            d[1] -= 1

        print(dislikes)
        for d in dislikes:
            dicts[d[0]].add(d[1])
            dicts[d[1]].add(d[0])

        while sum([len(d) for d in dicts]) > 0:
            max_dict = 0
            max_num = 0

            for i, d in enumerate(dicts):
                if len(d) > max_dict:
                    max_dict = len(d)
                    max_num = i

            if max_num in A and max_num in B:
                print('here1')
                return False

            if max_num not in A and max_num not in B:
                A.add(max_num)

            check_list = set()
            check_list.add(max_num)

            while check_list:
                new_check_list = set()
                for number in check_list:
                    if number in A:
                        # A.add(max_num)
                        for num in dicts[number]:
                            if num in A:
                                print(number)
                                print(num)
                                print('here2')
                                return False
                            else:
                                B.add(num)
                                new_check_list.add(num)
                                if number in dicts[num]:
                                    dicts[num].remove(number)
                    else:
                        # B.add(max_num)
                        for num in dicts[number]:
                            if num in B:
                                print('here3')
                                return False
                            else:
                                A.add(num)
                                new_check_list.add(num)
                                if number in dicts[num]:
                                    dicts[num].remove(number)
                    check_list = new_check_list

            print('A={}, B={}'.format(A, B))
            dicts[max_num] = set()
        return True


    def possibleBipartition2(self, N, dislikes):
        """
        :type N: int
        :type dislikes: List[List[int]]
        :rtype: bool
        """

        # Driver program to test above function
        g = Solution.Graph(N)

        for d in dislikes:
            d[0] -= 1
            d[1] -= 1

        g.graph = []
        for i in range(N):
            g.graph.append([0] * N)

        for d in dislikes:
            g.graph[d[0]][d[1]] = 1
            g.graph[d[1]][d[0]] = 1

        return True if g.isBipartite(0) else False


    class Graph():

        def __init__(self, V):
            self.V = V
            self.graph = [[0 for column in range(V)] \
                          for row in range(V)]

        # This function returns true if graph G[V][V]
        # is Bipartite, else false
        def isBipartite(self, src):

            # Create a color array to store colors
            # assigned to all veritces. Vertex
            # number is used as index in this array.
            # The value '-1' of  colorArr[i] is used to
            # indicate that no color is assigned to
            # vertex 'i'. The value 1 is used to indicate
            # first color is assigned and value 0
            # indicates second color is assigned.
            colorArr = [-1] * self.V

            # Assign first color to source
            colorArr[src] = 1

            # Create a queue (FIFO) of vertex numbers and
            # enqueue source vertex for BFS traversal
            queue = []
            queue.append(src)

            # Run while there are vertices in queue
            # (Similar to BFS)
            while queue:

                u = queue.pop()

                if self.graph[u][u] == 1:
                    return False;

                for v in range(self.V):

                    # An edge from u to v exists and destination
                    # v is not colored
                    if self.graph[u][v] == 1 and colorArr[v] == -1:

                        # Assign alternate color to this
                        # adjacent v of u
                        colorArr[v] = 1 - colorArr[u]
                        queue.append(v)

                    # An edge from u to v exists and destination
                    # v is colored with same color as u
                    elif self.graph[u][v] == 1 and colorArr[v] == colorArr[u]:
                        return False

            # If we reach here, then all adjacent
            # vertices can be colored with alternate
            # color
            return True

