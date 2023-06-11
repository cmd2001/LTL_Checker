from Formula.LTLFormula import *
from Formula.utils import cross_formula_list, formula_in_list, print_formula_list
from BA.utils import BANode, BAEdge


class GNBA:
    @staticmethod
    def check_edge(src: list[LTLBaseFormula], dst: list[LTLBaseFormula], cl: list[LTLBaseFormula]) -> bool:
        for f in cl:
            if isinstance(f, LTLNextFormula):
                phi_in_src = formula_in_list(f, src)
                child_in_dst = formula_in_list(f.child, dst)
                if phi_in_src != child_in_dst:
                    return False
            if isinstance(f, LTLUntilFormula):
                phi_in_src = formula_in_list(f, src)
                phi_in_dst = formula_in_list(f, dst)
                left_in_src = formula_in_list(f.left, src)
                right_in_src = formula_in_list(f.right, src)
                flag1 = phi_in_src
                flag2 = (right_in_src or (left_in_src and phi_in_dst))
                if flag1 != flag2:
                    return False
        return True

    def __init__(self, elememtary_sets: list[list[LTLBaseFormula]], atomic_formulas: list[LTLAtomicFormula], cl: list[LTLAtomicFormula], root_formula: LTLBaseFormula) -> None:
        self.nodes = []
        self.start_nodes = []
        for elememtary_set in elememtary_sets:
            node = BANode(elememtary_set)
            self.nodes.append(node)
            if formula_in_list(root_formula, elememtary_set):
                self.start_nodes.append(node)
        for node in self.nodes:
            symbol = cross_formula_list(node.id_formula, atomic_formulas)
            for dst in self.nodes:
                if GNBA.check_edge(node.id_formula, dst.id_formula, cl):
                    node.edges.append(BAEdge(symbol, dst))
        self.accept_sets = []
        for formula in cl:
            if isinstance(formula, LTLUntilFormula):
                node_set = []
                for node in self.nodes:
                    phi_in = formula_in_list(formula, node.id_formula)
                    right_in = formula_in_list(formula.right, node.id_formula)
                    if not phi_in or right_in:
                        node_set.append(node)
                self.accept_sets.append(node_set)

    def print(self):
        print('Printing GNBA')
        print('n_nodes: {}, n_start_nodes: {}, n_accept_sets: {}'.format(
            len(self.nodes), len(self.start_nodes), len(self.accept_sets)))
        print('start nodes are:')
        for n in self.start_nodes:
            print(self.nodes.index(n), end=' ')
        print()
        print('accept sets are:')
        for accept_set in self.accept_sets:
            for i in accept_set:
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
