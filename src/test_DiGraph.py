from unittest import TestCase

from src.DiGraph import DiGraph


class TestDiGraph(TestCase):
    n = 100000

    def setUp(self) -> None:
        # let's generate a star graph with 100,000 vertices and (99,999 *2 edges)
        self.graph = DiGraph()
        self.graph.add_node(0)  # 1
        for i in range(1, 100000):
            self.graph.add_node(i)  # 99,999
            self.graph.add_edge(0, i, 100)
            self.graph.add_edge(i, 0, 50)
            # 99,999 * 2
        pass

    def test_get_mc(self):
        expected = 100000 + (100000 - 1) * 2
        self.assertTrue(self.graph.get_mc() % expected == 0)
        for i in range (150000,200000): # 50,0000 action *4 = 200,000
            self.graph.add_node(i)
            self.graph.add_edge(i,0,4)
            self.graph.remove_edge(i,0)
            self.graph.remove_node(i)
        self.assertTrue(self.graph.get_mc() % (expected+200000) == 0)

    def test_v_size(self):
        self.assertEqual(self.graph.v_size(), 100000)

    def test_e_size(self):
        self.assertEqual(self.graph.e_size(), (100000 - 1) * 2)

    def test_add_edge(self):
        # let's add an edge with a node that doesn't exist in our graph
        # then add an edge that is already existent
        self.assertFalse(self.graph.add_edge(-1, -2, 500))
        for i in range(1, 100000):
            self.assertFalse(self.graph.add_edge(0, i, 100))
            self.assertFalse(self.graph.add_edge(i, 0, 100))

    def test_add_node(self):

        for i in range(100000):
            self.assertFalse(self.graph.add_node(i))

        for i in range(200000, 300000):
            self.assertTrue(self.graph.add_node(i))

    def test_remove_node(self):
        for i in range(200000, 300000):
            self.assertFalse(self.graph.remove_node(i))

        for j in range(100000):
            self.assertTrue(self.graph.remove_node(j))
        print(self.graph.e_size())
        print(self.graph.v_size())
        print(self.graph.m_vertices)
        print(self.graph.m_edges)
        print(self.graph.m_edges_inverted)

    def test_remove_edge(self):
        for i in range(200000, 300000):
            self.assertFalse(self.graph.remove_edge(i - 1, i))

    def test_get_all_v(self):
        self.assertTrue(len(self.graph.get_all_v()) == 100000)

    #
    def test_all_in_edges_of_node(self):
        self.assertTrue(len(self.graph.all_in_edges_of_node(0)) == self.graph.v_size() - 1)
        for i in range (50000,100000):
            self.graph.remove_edge(i, 0)
        self.assertTrue(len(self.graph.all_in_edges_of_node(0)) == self.graph.v_size()/2 - 1)


    #
    def test_all_out_edges_of_node(self):
        self.assertTrue(len(self.graph.all_out_edges_of_node(0)) == self.graph.v_size() - 1)
        for i in range(50000, 100000):
            self.graph.remove_edge(0, i)
        self.assertTrue(len(self.graph.all_out_edges_of_node(0)) == self.graph.v_size() / 2 - 1)