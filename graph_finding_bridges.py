
class Graph:
    def __init__(self, num_of_nodes, directed = False, weight = False):

        self.num_of_nodes = num_of_nodes 

        self.m_directed = directed

        self.m_weight = weight

        self.m_adj_list = {node: set() for node in range(self.num_of_nodes)}      

        self.bridge_visited = [False]*self.num_of_nodes

        self.list_of_bridges = []

    def add_edge(self, node1, node2, weight = 1):
        if self.m_weight:
            self.m_adj_list[node1 - 1].add((node2 - 1, weight))
            if not self.m_directed:
                self.m_adj_list[node2 - 1].add((node1 - 1, weight))

        else:
            self.m_adj_list[node1 - 1].add(node2 - 1)
            if not self.m_directed:
                self.m_adj_list[node2 - 1].add(node1 - 1)

    def print_adj_list(self):
        for key in self.m_adj_list.keys():
            print("Node", key, ": ", self.m_adj_list[key])


    def bridge_dfs(self, node, timer, parent = -1, tin = [], low = []):
        # ref: https://cp-algorithms.com/graph/bridge-searching.html#implementation
        self.bridge_visited[node] = True

        # Gán giá trị khởi đầu cho tin[] và low[]
        timer += 1
        tin[node] = low[node] = timer + 1

        for to in self.m_adj_list[node]:
            if to == parent: 
                continue
            if self.bridge_visited[to]:
                low[node] = min(low[node], tin[to])
            else:
                self.bridge_dfs(to, timer, node, tin , low)
                low[node] = min(low[node], low[to])
                if low[to] > tin[node]:   
                    self.list_of_bridges.append((node, to))

    def get_bridges(self):
        self.find_bridges()
        if self.list_of_bridges is not None:
            return self.list_of_bridges
        else:
            return None
            
    def find_bridges(self):
        timer = 0
        parent = - 1
        tin = [-1]*self.num_of_nodes
        low =  [-1]*self.num_of_nodes

        for i in range(self.num_of_nodes):
            if not self.bridge_visited[i]:
                self.bridge_dfs(i,timer, parent, tin, low)


def main():
    graph = Graph(6, directed = False)
    graph.add_edge(1,2)
    graph.add_edge(2,3)        
    graph.add_edge(3,4)   
    graph.add_edge(4,5)
    graph.add_edge(5,6)
    graph.add_edge(4,6)
    ans = graph.get_bridges()
    print(ans)

if __name__ == "__main__":
    try: 
        main()
    except:
        print('Loser!!! You suck at coding')

