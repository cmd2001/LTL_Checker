from Formula.LTLFormula import LTLBaseFormula


class TSState:
    def __init__(self, id: str, prop: list[LTLBaseFormula]) -> None:
        self.id = id
        self.prop = prop
        self.trans = []


class TSTransition:
    def __init__(self, action: str, dst: TSState) -> None:
        self.action = action
        self.dst = dst
