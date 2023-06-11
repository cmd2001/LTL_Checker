from Formula.LTLFormula import LTLBaseFormula
from BA.utils import BANode


class TSState:
    def __init__(self, id: str, prop: list[LTLBaseFormula]) -> None:
        self.id = id
        self.prop = prop
        self.trans = []


class TSTransition:
    def __init__(self, action: str, dst: TSState) -> None:
        self.action = action
        self.dst = dst


class ProductTSState:
    def __init__(self, ts_state: TSState, nba_node: BANode) -> None:
        self.ts_state = ts_state
        self.nba_node = nba_node
        self.trans = []


class ProductTSTransition:
    def __init__(self, dst: TSState) -> None:
        self.dst = dst
