from GraphInterface import GraphInterface


class DiGraph(GraphInterface):
    m_mc = 0

    def __init__(self):
        self.m_vertices = dict()
        self.m_edges = dict()
        self.m_edges_inverted = dict()
        self.edge_quantity = 0
        pass

    class GEdge:
        def __init__(self, src: int, dst: int, weight: float):
            self.src = src
            self.dst = dst
            self.weight = weight

    class GNode:
        static_key = 0

        def __init__(self, key=-1):
            self.m_neighbors = dict()
            if key == -1:
                self.key = self.static_key
                DiGraph.GNode.static_key += 1
            else:
                self.key = key

        def __int__(self, key: int):
            self.key = id

        def add_neighbor(self, neighbor):
            self.m_neighbors[neighbor.key] = neighbor

    def v_size(self) -> int:
        return len(self.m_vertices)
        pass

    def e_size(self) -> int:
        return self.edge_quantity

    def get_mc(self) -> int:
        return DiGraph.m_mc
        pass

    def add_edge(self, id1: int, id2: int, weight: float) -> bool:
        edge = self.GEdge(id1, id2, weight)
        # if id1 not in self.m_edges.keys():
        #     self.m_edges[id1]= {}
        # if id2 not in self.m_edges_inverted.keys():
        #     self.m_edges_inverted[id2] = {}

        self.m_edges_inverted[id2][id1] = edge
        self.m_edges[id1][id2] = edge
        DiGraph.m_mc += 1
        self.edge_quantity += 1
        return True
        pass

    def add_node(self, node_id: int, pos: tuple = None) -> bool:
        self.m_vertices[node_id] = DiGraph.GNode(node_id)
        self.m_edges[node_id]={}
        self.m_edges_inverted[node_id]={}
        DiGraph.m_mc += 1
        return True
        pass

    def remove_node(self, node_id: int) -> bool:
        # when removing any node we shall check for the edges going out of the node and delete them also we must
        # check for the edges this node receives , thus we have implemented an extra attribute called
        # self.m_edges_inverted with primary key as the receiving node exactly the opposite of self.m_edges this
        # would help us know our target nodes that sent the edge to the desired node we want to remove it saves us
        # runtime complexity since we wont have to traverse all the n-1 node instead we shall only traverse k nodes
        # such that k= number of nodes invloved in sending edges to our node that we want to delete
        # we must also count the edges that are going to be removed since it helps making self.esize O(1) achievable
        k = 0
        target = self.m_vertices[node_id]
        k += len(self.m_edges[node_id].keys())
        ans = self.m_vertices.pop(node_id)
        if type(ans) != DiGraph.GNode:
            return False
        else:
            self.m_edges.pop(node_id)
            for senders in self.m_edges_inverted[node_id].keys():
                self.m_edges[senders].pop(node_id)
                k += 1
            DiGraph.m_mc += 1
            self.edge_quantity -= k
            return True

    # we must also delete the edges using this node as src/dst

    def remove_edge(self, node_id1: int, node_id2: int) -> bool:

        temp = DiGraph.m_mc

        for key in list((self.m_edges[node_id1]).keys()):

            if key == node_id2:
                self.m_edges[node_id1].pop(key)
                DiGraph.m_mc += 1

        if temp == DiGraph.m_mc:
            return False
        self.edge_quantity -= 1
        return True

    def get_all_v(self) -> dict:
        return dict((x, y) for x, y in self.m_vertices.items())

    def all_in_edges_of_node(self, id1: int) -> dict:
        return dict((x,y.weight) for x,y in self.m_edges_inverted[id1].items())

    def all_out_edges_of_node(self, id1: int) -> dict:
        return dict((x, y.weight) for x, y in self.m_edges[id1].items())