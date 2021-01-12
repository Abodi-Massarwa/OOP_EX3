import json
import jsonpickle

from DiGraph import DiGraph
from GraphAlgo import GraphAlgo


def check():
    """
    Graph: |V|=4 , |E|=5
    {0: 0: |edges out| 1 |edges in| 1, 1: 1: |edges out| 3 |edges in| 1, 2: 2: |edges out| 1 |edges in| 1, 3: 3: |edges out| 0 |edges in| 2}
    {0: 1}
    {0: 1.1, 2: 1.3, 3: 10}
    (3.4, [0, 1, 2, 3])
    [[0, 1], [2], [3]]
    (2.8, [0, 1, 3])
    (inf, [])
    2.062180280059253 [1, 10, 7]
    17.693921758901507 [47, 46, 44, 43, 42, 41, 40, 39, 15, 16, 17, 18, 19]
    11.51061380461898 [20, 21, 32, 31, 30, 29, 14, 13, 3, 2]
    inf []
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], [14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47]]
    """
    check0()
    check1()
    check2()


def check0():
    """
    This function tests the naming (main methods of the DiGraph class, as defined in GraphInterface.
    :return:
    """
    g = DiGraph()  # creates an empty directed graph
    for n in range(4):
        g.add_node(n)
    g.add_edge(0, 1, 1)
    g.add_edge(1, 0, 1.1)
    g.add_edge(1, 2, 1.3)
    g.add_edge(2, 3, 1.1)
    g.add_edge(1, 3, 1.9)
    g.remove_edge(1, 3)
    g.add_edge(1, 3, 10)
    print(g)  # prints the __repr__ (func output)
    print(g.get_all_v())  # prints a dict with all the graph's vertices.
    print(g.all_in_edges_of_node(1))
    print(g.all_out_edges_of_node(1))
    g_algo = GraphAlgo(g)
    print(g_algo.shortest_path(0, 3))
    g_algo.plot_graph()


def check1():
    """
       This function tests the naming (main methods of the GraphAlgo class, as defined in GraphAlgoInterface.
    :return:
    """
    g_algo = GraphAlgo()  # init an empty graph - for the GraphAlgo
    file = "../data/T0.json"
    g_algo.load_from_json(file)  # init a GraphAlgo from a json file
    print(g_algo.connected_components())
    print(g_algo.shortest_path(0, 3))
    print(g_algo.shortest_path(3, 1))
    g_algo.save_to_json(file + '_saved')
    g_algo.plot_graph()


def check2():
    """ This function tests the naming, basic testing over A5 json file.
      :return:
      """
    g_algo = GraphAlgo()
    file = '../data/A5'
    g_algo.load_from_json(file)
    g_algo.get_graph().remove_edge(13, 14)
    g_algo.save_to_json(file + "_edited")
    dist, path = g_algo.shortest_path(1, 7)
    print(dist, path)
    dist, path = g_algo.shortest_path(47, 19)
    print(dist, path)
    dist, path = g_algo.shortest_path(20, 2)
    print(dist, path)
    dist, path = g_algo.shortest_path(2, 20)
    print(dist, path)
    print(g_algo.connected_component(0))
    print(g_algo.connected_components())
    g_algo.plot_graph()


if __name__ == '__main__':
    # check()
    first = DiGraph.GNode()
    second = DiGraph.GNode()
    third = DiGraph.GNode()
    # first.add_neighbor(third)
    # third.add_neighbor(second)
    # second.add_neighbor(first)
    graph = DiGraph()
    graph.add_node(first.key,(1,2,3))
    graph.add_node(second.key)
    graph.add_node(third.key)
    graph.add_edge(first.key, third.key, 100)
    graph.add_edge(third.key, second.key, 100)
    graph.add_edge(second.key, first.key, 100)
    # print("graph edges number using the attribute edge quantity")
    # print(graph.edge_quantity)
    # print(first.key)
    # print(second.key)
    # print(third.key)
    # print(graph.v_size())
    # print(graph.e_size())
    # print(graph.m_edges)
    # print(graph.m_vertices)
    # graph.remove_edge(2,1)
    # print(graph.e_size())
    # print(graph.edge_quantity)
    # graph.remove_node(0)
    # print(graph.e_size())
    # print(graph.m_edges)
    # print(graph.v_size())
    # print(graph.edge_quantity)
    # l=[(x,y)for x,y in graph.m_vertices.items()]
    # print(l)
    # print(graph.get_all_v())
    # graph.add_node(3)
    # print(graph.m_edges[1])
    # graph.add_edge(1,3,1337)
    # print(graph.m_edges[1])
    # print(graph.all_in_edges_of_node(1))
    # print(graph.all_out_edges_of_node(1))
    # print(graph.v_size())
    # print(graph.e_size())
    # graph.remove_node(3)
    # print(graph.v_size())
    # print(graph.e_size())
    # print(a.m_neighbors.values())
    #
    # algo = GraphAlgo(graph)
    # algo.save_to_json("D.I.E")
    #
    # algo_2 = GraphAlgo()
    # algo_2.load_from_json('D.I.E')
    #
    # print (algo_2.m_graph.m_vertices)
    # print(algo.m_graph.m_vertices)
    # print(f"the vertices {graph.m_vertices}")
    # print(graph.m_edges)
    # print(graph.m_edges_inverted)
    algo= GraphAlgo(graph)
    algo.save_to_json("NoorBsoul")
    algo2=GraphAlgo(graph)
    algo2.load_from_json("NoorBsoul")
    print(algo.m_graph.m_edges)
    print(algo.m_graph.m_edges_inverted)
    # print(algo2.m_graph.m_edges)
