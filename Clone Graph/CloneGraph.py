import collections
import networkx as nx
import matplotlib.pyplot as plt


class Node(object):
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors= neighbors if neighbors is not None else []
    # for debugging
    def __repr__(self):
        return f'Node(val: {self.val}, neighbors:{[i.val for i in self.neighbors]})'


def show_graph(dict):
    graph = nx.Graph()
    for v in dict.values():
        graph.add_node(v)
        graph.add_edges_from([(v, _v) for _v in v.neighbors])
    pos = nx.spring_layout(graph, seed=100)
    nx.draw(graph, pos, with_labels=True, font_weight='bold')
    plt.show()


def create_graph(x):
    if not x: return x

    def create_nodes(x):
        _node_list = [Node(i+1) for i in range(len(x))]
        return _node_list

    node_list = create_nodes(x)
    for node, _neighbors in zip(node_list, graph_list):
        node.neighbors = [node_list[index-1] for index in _neighbors]

    return node_list[0]


class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: A reference of a node in a connected undirected graph.
        :rtype: Node
        """
        if not node: return node
        visited, queue = set(), collections.deque([node])
        copy_dict = {}

        while queue:
            current_node = queue.popleft()
            if current_node in visited: continue
            visited.add(current_node)

            if current_node not in copy_dict:
                copy_dict[current_node] = Node(current_node.val)

            for neighbor in current_node.neighbors:
                if neighbor not in copy_dict:
                    copy_dict[neighbor] = Node(neighbor.val)
                copy_dict[current_node].neighbors.append(copy_dict[neighbor])

                queue.append(neighbor)

            show_graph(copy_dict)  # draw graph

        return copy_dict[node]


if __name__ == '__main__':
    graph_list = [[2,4],[1,3],[2,4],[1,3]]
    graph_list = [[2, 4, 6], [1, 3, 4, 6], [2, 4], [1, 2, 3], [], [1, 2]]
    graph = create_graph(graph_list)
    # print(graph)

    solution = Solution()
    ans = solution.cloneGraph(graph)

