from Formula.LTLFormula import *
from Formula.utils import cross_formula_list, formula_in_list, print_formula_list
from BA.utils import BANode, BAEdge
from BA.GNBA import GNBA


class NBA:
    def __init__(self, gnba: GNBA) -> None:
        if len(gnba.accept_sets) == 0:
            self.nodes = gnba.nodes
            self.start_nodes = gnba.start_nodes
            self.accept_set = []
            return

        self.nodes = []
        for _ in range(len(gnba.accept_sets)):
            for node in gnba.nodes:
                self.nodes.append(BANode(node.id_formula))

        def get_node(layer: int, gnba_node: BANode) -> BANode:
            return self.nodes[layer * len(gnba.nodes) + gnba.nodes.index(gnba_node)]

        def get_next_layer(layer: int):
            if layer < len(gnba.accept_sets) - 1:
                return layer + 1
            return 0

        self.start_nodes = []
        for node in gnba.start_nodes:
            self.start_nodes.append(get_node(0, node))

        self.accept_set = []
        for node in gnba.accept_sets[0]:
            self.accept_set.append(get_node(0, node))
        for layer in range(len(gnba.accept_sets)):
            accept_set = gnba.accept_sets[layer]
            for node in gnba.nodes:
                dst_layer = get_next_layer(
                    layer) if node in accept_set else layer
                for edge in node.edges:
                    get_node(layer, node).edges.append(
                        BAEdge(edge.symbol_formula, get_node(dst_layer, edge.dst)))

    def print(self):
        print('Printing GNBA')
        print('n_nodes: {}, n_start_nodes: {}, n_accept_set: {}'.format(
            len(self.nodes), len(self.start_nodes), len(self.accept_set)))
        print('start nodes are:')
        for n in self.start_nodes:
            print(self.nodes.index(n), end=' ')
        print()
        print('accept sets are:')
        for i in self.accept_set:
            print(self.nodes.index(i), end=' ')
        print()
        print('formula set at each node are:')
        for i in range(len(self.nodes)):
            print('{}: '.format(i), end='')
            print_formula_list(self.nodes[i].id_formula)
        print('edges are:')
        for i in range(len(self.nodes)):
            print('{}: '.format(i), end='')
            for edge in self.nodes[i].edges:
                print(self.nodes.index(edge.dst), end=' ')
            print()
