from unittest import TestCase

from src.DiGraph import DiGraph
from src.GraphAlgo import GraphAlgo


class TestGraphAlgo(TestCase):

    def setUp(self) -> None:
        graph = DiGraph()
        graph.add_node(0, (5, 10, 0))
        graph.add_node(1, (15, 10, 0))
        graph.add_node(2, (15, 5, 0))
        graph.add_node(3, (5, 5, 0))
        graph.add_node(4, (12, 3, 0))
        graph.add_node(5, (15, 3, 0))
        graph.add_node(6, (17, 2, 0))
        graph.add_edge(0, 1, 10)
        graph.add_edge(1, 2, 10)
        graph.add_edge(0, 2, 15)
        graph.add_edge(2, 4, 1.5)
        graph.add_edge(3, 4, 2)
        graph.add_edge(2, 3, 10)
        graph.add_edge(3, 0, 5)
        graph.add_edge(4, 5, 0.5)
        graph.add_edge(5, 6, 2.5)
        graph.add_edge(5, 4, 0.3)

        self.graph = GraphAlgo(graph)

    def test_load_save_from_json(self):
        self.graph.save_to_json("File")
        algo2 = GraphAlgo()
        algo2.load_from_json("File")

        for key in algo2.m_graph.m_vertices.keys():
            self.assertTrue(self.graph.m_graph.m_vertices[int(key)].key == int(algo2.m_graph.m_vertices[key].key))

        for i in range(self.graph.m_graph.v_size()):
            list1 = [value for value in algo2.m_graph.all_out_edges_of_node(str(i)).values()]
            list2 = [value for value in self.graph.m_graph.all_out_edges_of_node(i).values()]
            self.assertTrue(list2 == list1)

    def test_shortest_path(self):
        self.assertTrue(self.graph.shortest_path(0, 6) == (19.5, [0, 2, 4, 5, 6]))
        self.assertTrue(self.graph.shortest_path(0, 5) == (17, [0, 2, 4, 5]))
        self.graph.m_graph.remove_edge(5, 6)
        self.assertTrue(self.graph.shortest_path(0, 6) == (float("inf"), []))

    def test_connected_component(self):
        self.assertTrue(self.graph.connected_component(1) == [0, 3, 2, 1])
        self.assertTrue(self.graph.connected_component(4) == [4, 5])
        self.assertTrue(self.graph.connected_component(6) == [6])

    def test_connected_components(self):
        self.assertTrue([[0, 3, 2, 1], [4, 5], [6]] == self.graph.connected_components())

    def test_plot_graph(self):
        self.graph.plot_graph()
