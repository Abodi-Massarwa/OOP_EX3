import copy
from typing import List
import json
from GraphAlgoInterface import GraphAlgoInterface
from src.DiGraph import DiGraph
import matplotlib.pyplot as plt


class GraphAlgo(GraphAlgoInterface):

    def __init__(self, graph: DiGraph = None):
        self.m_graph = graph

    def load_from_json(self, file_name: str) -> bool:

        with open(f'{file_name}.json') as f:
            data = json.load(f)

        self.m_graph = DiGraph()
        self.m_graph.m_mc = data['m_mc']
        self.m_graph.m_vertices = data['m_vertices']
        self.m_graph.m_edges = data['m_edges']
        self.m_graph.m_edges_inverted = data['m_edges_inverted']
        self.m_graph.edge_quantity = data['edge_quantity']

        for x, y in data['m_vertices'].items():
            data['m_vertices'][x] = DiGraph.GNode(x, y["pos"])

        for key, inner_dictionary in list(self.m_graph.m_edges.items()):
            for src, edge in list(inner_dictionary.items()):
                inner_dictionary[src] = DiGraph.GEdge(inner_dictionary[src]["src"], inner_dictionary[src]["dst"],
                                                      inner_dictionary[src]["weight"])

        for key, inner_dictionary in list(self.m_graph.m_edges_inverted.items()):
            for src, edge in list(inner_dictionary.items()):
                inner_dictionary[src] = DiGraph.GEdge(inner_dictionary[src]["src"], inner_dictionary[src]["dst"],
                                                      inner_dictionary[src]["weight"])

    def save_to_json(self, file_name: str) -> bool:
        dictionary_vertices = copy.deepcopy(self.m_graph.m_vertices)
        dictionary_edges = copy.deepcopy(
            self.m_graph.m_edges)  # we need to make the edges more readable EdgeData -> {src:x , dst:y, weight: z}
        dictionary_edges_inverted = copy.deepcopy(self.m_graph.m_edges_inverted)
        mc = self.m_graph.m_mc
        quantity = self.m_graph.edge_quantity
        # print(f"new edges : {dictionary_edges}")
        # print(f"new inverted :{dictionary_edges_inverted}")
        for x, y in dictionary_vertices.items():
            dictionary_vertices[x] = {"key": str(y.key), "pos": y.coordinate}

        for x, y in dictionary_edges.items():
            for id, edge in y.items():
                dictionary_edges[x][id] = {"src": edge.src, "dst": edge.dst, "weight": edge.weight}

        for x, y in dictionary_edges_inverted.items():
            for id, edge in y.items():
                dictionary_edges_inverted[x][id] = {"src": edge.src, "dst": edge.dst, "weight": edge.weight}

        dict = {"m_mc": mc, "edge_quantity": quantity, "m_vertices": dictionary_vertices, "m_edges": dictionary_edges,
                "m_edges_inverted": dictionary_edges_inverted}

        with open(f'{file_name}.json', 'w') as f:
            json.dump(dict, f)

    def shortest_path(self, id1: int, id2: int) -> (float, list):
        pass

    def connected_component(self, id1: int) -> list:
        pass

    def connected_components(self) -> List[list]:
        pass

    def plot_graph(self) -> None:
        coordinates = {}
        g_nodes = self.m_graph.get_all_v()
        for key in g_nodes.keys():
            coordinates[key] = g_nodes[key].coordinate
            x_axis = g_nodes[key].coordinate[0]
            y_axis = g_nodes[key].coordinate[1]
            # z axis is useless since we're not working with 3d graph
            plt.plot(x_axis, y_axis, marker="o", c="b", ms=14)
            plt.text(x_axis + 0.10, y_axis + 0.10, key, size=10, c="r")
        # now let's draw the edges for each one of the vertices using the methods we impl'd
        for key in g_nodes.keys():
            neighbors = self.m_graph.all_out_edges_of_node(key)
            for target in neighbors.keys():
                start = coordinates[key]
                end = coordinates[target]
                x = start[0]
                y = start[1]
                xd = end[0]
                yd = end[1]
                weight_x_axis = (x + xd) / 2
                weight_y_axis = (y + yd) / 2
                plt.arrow(x, y, xd - x, yd - y, ec="r", joinstyle="round", fc="r", width=0.04, head_width=10 * 0.025,
                          head_length=0.5, length_includes_head=True)
                plt.text(weight_x_axis + 0.10, weight_y_axis + 0.10, neighbors[target], color="r")

        plt.show()
