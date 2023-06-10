from Formula.LTLFormula import *

class BANode:
    def __init__(self, id_formula: list[LTLBaseFormula]) -> None:
        self.id_formula = id_formula
        self.edges = []
class BAEdge:
    def __init__(self, symbol_formula: list[LTLBaseFormula], dst: list) -> None:
        self.symbol_formula = symbol_formula
        self.dst = dst