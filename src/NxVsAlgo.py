import json
import time
from unittest import TestCase

import networkx

from src.DiGraph import DiGraph
from src.GraphAlgo import GraphAlgo
import networkx as nx


class TestGraphAlgo(TestCase):

    def setUp(self) -> None:
        self.graph_algo = GraphAlgo()

    def testShortestPath(self):
        self.graph_algo.load_from_json('../data/A5')
        start_time = time.time()
        self.graph_algo.shortest_path(0, 100)

        end_time = time.time()
        print(float(end_time - start_time))

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
