from typing import List

from GraphAlgoInterface import GraphAlgoInterface


class GraphAlgo(GraphAlgoInterface):
    def load_from_json(self, file_name: str) -> bool:
        pass

    def save_to_json(self, file_name: str) -> bool:
        pass

    def shortest_path(self, id1: int, id2: int) -> (float, list):
        pass

    def connected_component(self, id1: int) -> list:
        pass

    def connected_components(self) -> List[list]:
        pass

    def plot_graph(self) -> None:
        pass

    # class GNode:
    # static_key = 0
    # m_neighbors = {}
    #
    # def __init__(self):
    #     self.key = self.static_key
    #     GNode.static_key += 1
    #
    # def add_neighbor(self, neighbor):
    #     self.m_neighbors[neighbor.key] = neighbor
