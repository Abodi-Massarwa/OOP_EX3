import random

from GraphInterface import GraphInterface


class DiGraph(GraphInterface):

    def __init__(self):
        self.m_mc = 0
        self.m_vertices = dict()
        self.m_edges = dict()  # {1:{2:EdgeData,3:EdgeData,......k:Edge}
        self.m_edges_inverted = dict()
        self.edge_quantity = 0

    class GEdge:
        def __init__(self, src: int, dst: int, weight: float):
            self.src = src
            self.dst = dst
            self.weight = weight

    class GNode:
        static_key = 0

        def __init__(self, key=-1, coordinate: tuple = None):

            if key == -1:
                self.key = self.static_key
                DiGraph.GNode.static_key += 1
            else:
                self.key = key
            self.coordinate = coordinate
            if coordinate is None:
                self.coordinate=(random.uniform(0,20),random.uniform(0,20),random.uniform(0,20))


        def __int__(self, key: int):
            self.key = id

    def v_size(self) -> int:
        return len(self.m_vertices)
        pass

    def e_size(self) -> int:
        return self.edge_quantity

    def get_mc(self) -> int:
        return self.m_mc
        pass

    def add_edge(self, id1: int, id2: int, weight: float) -> bool:
        if id1 not in self.m_vertices.keys() or id2 not in self.m_vertices.keys():
            return False
        if id2 in self.m_edges[id1]:
            return False
        edge = self.GEdge(id1, id2, weight)
        self.m_edges_inverted[id2][id1] = edge
        self.m_edges[id1][id2] = edge
        self.m_mc += 1
        self.edge_quantity += 1
        return True
        pass

    def add_node(self, node_id: int, pos: tuple = None) -> bool:
        if node_id in self.m_vertices.keys():
            return False
        self.m_vertices[node_id] = DiGraph.GNode(node_id, pos)
        self.m_edges[node_id] = {}
        self.m_edges_inverted[node_id] = {}
        self.m_mc += 1
        return True
        pass

    def remove_node(self, node_id: int) -> bool:
        if node_id not in self.m_vertices.keys():
            return False
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
            # removing the node a source from both m_edges & m_edges_inverted
            receivers = list(self.m_edges[node_id].keys())
            for target in receivers:
                self.m_edges_inverted[target].pop(node_id)

            self.m_edges.pop(node_id)
            # self.m_edges[node_id]={} # to prevent any KeyError in future calls
            # removing all the edges involved in our desired node as a destination node
            for senders in list(self.m_edges_inverted[node_id].keys()):
                self.m_edges[senders].pop(node_id)

                k += 1
            self.m_mc += 1
            self.m_edges_inverted.pop(node_id)
            self.edge_quantity -= k

            return True

    # we must also delete the edges using this node as src/dst

    def remove_edge(self, node_id1: int, node_id2: int) -> bool:
        # when removing an edge we must
        # 1) remove it from the m_edges dict (id1->id2)
        # 2) remove it from the m_edges_inverted dict (id2->id1)
        # TODO : retrun false when
        # TODO 1) there is no such edge (id1 or id2 doesn't exist in our node list)
        # TODO 2) edge already been removed (nodes do exist but edge doesnt)

        if node_id2 not in self.m_vertices or node_id1 not in self.m_vertices:
            return False

        if node_id2 not in self.m_edges[node_id1].keys():
            return False

        # else we will do the described above
        self.m_edges[node_id1].pop(node_id2)
        self.m_edges_inverted[node_id2].pop(node_id1)
        self.m_mc += 1
        self.edge_quantity -= 1

        # if node_id2 not in self.m_edges[node_id1].keys():
        #     return False
        # temp = self.m_mc
        #
        # for key in list((self.m_edges[node_id1]).keys()):
        #
        #     if key == node_id2:
        #         self.m_edges[node_id1].pop(key)
        #         self.m_mc += 1
        #
        # if temp == self.m_mc:
        #     return False
        # self.edge_quantity -= 1
        # return True

    def get_all_v(self) -> dict:
        return dict((x, y) for x, y in self.m_vertices.items())

    def all_in_edges_of_node(self, id1: int) -> dict:
        return dict((x, y.weight) for x, y in self.m_edges_inverted[id1].items())

    def all_out_edges_of_node(self, id1: int) -> dict:
        return dict((x, y.weight) for x, y in self.m_edges[id1].items())

# def parse_json(graph: DiGraph):
#     graph_copy = DiGraph()
#     graph_copy.m_mc = graph.m_mc
#     graph_copy.m_vertices = graph.m_vertices
#     graph_copy.m_edges = graph.m_edges
#     graph_copy.m_edges_inverted = graph.m_edges_inverted
#     graph_copy.edge_quantity = graph.edge_quantity
#
#     dict = graph_copy.__dict__
#     for x, y in dict['m_vertices'].items():
#         dict['m_vertices'][x] = y.__dict__
#
#     l = list(dict['m_edges'].keys())
#     for key in l:
#         for x, y in dict['m_edges'][key].items():
#             dict['m_edges'][key][x] = y.__dict__
#
#     l_inverted = list(dict['m_edges_inverted'].keys())
#     for key in l:
#         for x, y in dict['m_edges_inverted'][key].items():
#             dict['m_edges_inverted'][key][x] = y.__dict__
#
#     return dict
