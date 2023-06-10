from utils.LTLFormula import *
from utils.FormulaUtil import cross_formula_list, formula_in_list, print_formula_list

class GNBA:
    class GNBANode:
        def __init__(self, id_formula: list[LTLBaseFormula]) -> None:
            self.id_formula = id_formula
            self.edges = []
    class GNBAEdge:
        def __init__(self, symbol_formula: list[LTLBaseFormula], dst: list) -> None:
            self.symbol_formula = symbol_formula
            self.dst = dst
    
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
    
    def __init__(self, elememtary_sets: list[list[LTLBaseFormula]], atomic_formulas: list[LTLAtomicFormula], cl: list[LTLAtomicFormula], root_formula: LTLBaseFormula):
        self.nodes = []
        self.start_nodes = []
        for elememtary_set in elememtary_sets:
            node = GNBA.GNBANode(elememtary_set)
            self.nodes.append(node)
            if formula_in_list(root_formula, elememtary_set):
                self.start_nodes.append(node)
            # print_formula_list(elememtary_set)
        for node in self.nodes:
            symbol = cross_formula_list(node.id_formula, atomic_formulas)
            for dst in self.nodes:
                if GNBA.check_edge(node.id_formula, dst.id_formula, cl):
                    # get the index of node in self.nodes
                    id1 = self.nodes.index(node)
                    id2 = self.nodes.index(dst)
                    node.edges.append(GNBA.GNBAEdge(symbol, dst))
        self.finish_function = []
        for formula in cl:
            if isinstance(formula, LTLUntilFormula):
                node_set = []
                for node in self.nodes:
                    phi_in = formula_in_list(formula, node.id_formula)
                    right_in = formula_in_list(formula.right, node.id_formula)
                    if not phi_in or right_in:
                        node_set.append(node)
                self.finish_function.append(node_set)