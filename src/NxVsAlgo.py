import json
import time
from unittest import TestCase

import networkx
import switch as switch

from src.DiGraph import DiGraph
from src.GraphAlgo import GraphAlgo
import networkx as nx


class TestGraphAlgo(TestCase):

    def setUp(self) -> None:
        self.graph_algo = GraphAlgo()

    def testShortestPath(self):
        for file_num in range(1, 7):
            graph_path = get_path(file_num)
            self.graph_algo.load_from_json(graph_path)
            start_time = time.time()
            self.graph_algo.shortest_path(0, 9)
            end_time = time.time()
            print("")
            print("Testing shortest path - " + graph_path)
            print("graph algo: " + str(end_time - start_time))
            self.nx_from_json(graph_path)
            start_time = time.time()
            networkx.dijkstra_path_length(self.nx_graph, 0, 9)
            end_time = time.time()
            print("networkX graph: " + str(end_time - start_time))

    def testConnectedComponent(self):
        for file_num in range(1, 7):
            graph_path = get_path(file_num)
            self.graph_algo.load_from_json(graph_path)
            start_time = time.time()
            self.graph_algo.connected_component(8)
            end_time = time.time()
            print("")
            print("testing Connected Component - " + graph_path)
            print("graph algo: " + str(end_time - start_time))
            self.nx_from_json(graph_path)
            start_time = time.time()
            self.ConnectedComponent(self.nx_graph, 8)
            end_time = time.time()
            print("networkX graph: " + str(end_time - start_time))

    def testConnectedComponent(self):
        for file_num in range(1, 7):
            graph_path = get_path(file_num)
            self.graph_algo.load_from_json(graph_path)
            start_time = time.time()
            self.graph_algo.connected_components()
            end_time = time.time()
            print("")
            print("testing Connected Component - " + graph_path)
            print("graph algo: " + str(end_time - start_time))
            self.nx_from_json(graph_path)
            start_time = time.time()
            networkx.strongly_connected_components
            end_time = time.time()
            print("networkX graph: " + str(end_time - start_time))

    def nx_from_json(self, file_name):
        with open(f'{file_name}') as f:
            json_dict = json.load(f)
        try:
            self.graph = DiGraph()
            self.nx_graph = nx.DiGraph()
            vertices = json_dict['Nodes']
            edges = json_dict['Edges']
            vertex_coordinates = {}
            for v in vertices:
                key = v["id"]
                if v['pos'] is not None:
                    position_list = v['pos'].split(',')
                    coordinate = (float(position_list[0]), float(position_list[1]), float(position_list[2]))
                    vertex_coordinates[key] = coordinate
                    self.nx_graph.add_node(key)
            for edge in edges:
                w = edge['w']
                self.nx_graph.add_edge(edge['src'], edge['dest'], weight=w)
        except Exception as ex:
            print(ex)
            return False
        return vertex_coordinates

    @staticmethod
    def ConnectedComponent(gx, id1: int):
        for c_ls in networkx.strongly_connected_components(gx):
            if id1 in c_ls:
                return c_ls


def get_path(file_num):
    switcher = {
        1: '../data/G_10_80_1.json',
        2: '../data/G_100_800_1.json',
        3: '../data/G_1000_8000_1.json',
        4: '../data/G_10000_80000_1.json',
        5: '../data/G_20000_160000_1.json',
        6: '../data/G_30000_240000_1.json',
    }
    return switcher.get(file_num, "")
