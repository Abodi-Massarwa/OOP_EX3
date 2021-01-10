from GraphInterface import GraphInterface


class DiGraph(GraphInterface):
    m_mc=0

    def __init__(self):
        self.m_vertices=dict()
        self.m_edges=dict()
        pass

    def v_size(self) -> int:
        return len(self.m_vertices)
        pass

    def e_size(self) -> int:
        return len(self.m_edges)
        pass

    def get_mc(self) -> int:
        return DiGraph.m_mc
        pass

    def add_edge(self, id1: int, id2: int, weight: float) -> bool:
        self.m_edges[id1][id2]=weight
        DiGraph.m_mc+=1
        return True
        pass

    def add_node(self, node_id: int, pos: tuple = None) -> bool:
        self.m_vertices[node_id]=node_id
        DiGraph.m_mc+=1
        return True
        pass

    def remove_node(self, node_id: int) -> bool:
        self.m_vertices.pop(node_id)
        DiGraph.m_mc += 1
        return True
        pass

    def remove_edge(self, node_id1: int, node_id2: int) -> bool:
        self.m_edges[node_id1].pop(node_id2)
        DiGraph.m_mc += 1
        return True
        pass
