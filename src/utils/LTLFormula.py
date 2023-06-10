from enum import Enum


class LTLFormulaType(Enum):
    UNARY = 1
    BINARY = 2
    ATOMIC = 3


class LTLFormulaUnaryOperator(Enum):
    NOT = 1
    G = 2
    F = 3
    X = 4


class LTLFormulaBinaryOperator(Enum):
    AND = 5
    OR = 6
    IMPL = 7
    U = 8


class LTLBaseFormula:
    def __init__(self, type: LTLFormulaType):
        self.type = type

    def __str__(self) -> str:
        raise NotImplementedError()

    def sub_formula(self) -> list:
        raise NotImplementedError()


class LTLUnaryFormula(LTLBaseFormula):
    def __init__(self, operator: LTLFormulaUnaryOperator, child: LTLBaseFormula):
        super().__init__(LTLFormulaType.UNARY)
        self.operator = operator
        self.child = child

    def sub_formula(self) -> list:
        return [self.child]

    def __str__(self) -> str:
        return f"{self.operator.name} ({self.child})"


class LTLNotFormula(LTLUnaryFormula):
    def __init__(self, child: LTLBaseFormula):
        super().__init__(LTLFormulaUnaryOperator.NOT, child)


class LTLNextFormula(LTLUnaryFormula):
    def __init__(self, child: LTLBaseFormula):
        super().__init__(LTLFormulaUnaryOperator.X, child)


class LTLAlwaysFormula(LTLUnaryFormula):
    def __init__(self, child: LTLBaseFormula):
        super().__init__(LTLFormulaUnaryOperator.G, child)


class LTLEventuallyFormula(LTLUnaryFormula):
    def __init__(self, child: LTLBaseFormula):
        super().__init__(LTLFormulaUnaryOperator.F, child)


class LTLBinaryFormula(LTLBaseFormula):
    def __init__(self, operator: LTLFormulaBinaryOperator, left: LTLBaseFormula, right: LTLBaseFormula):
        super().__init__(LTLFormulaType.BINARY)
        self.operator = operator
        self.left = left
        self.right = right

    def sub_formula(self) -> list:
        return [self.left, self.right]

    def __str__(self) -> str:
        return f"({self.left}) {self.operator.name} ({self.right})"


class LTLLogicFormula(LTLBinaryFormula):
    def __init__(self, operator: LTLFormulaBinaryOperator, left: LTLBaseFormula, right: LTLBaseFormula):
        super().__init__(operator, left, right)


class LTLIMPLFormula(LTLBinaryFormula):
    def __init__(self, left: LTLBaseFormula, right: LTLBaseFormula):
        super().__init__(LTLFormulaBinaryOperator.IMPL, left, right)


class LTLUntilFormula(LTLBinaryFormula):
    def __init__(self, left: LTLBaseFormula, right: LTLBaseFormula):
        super().__init__(LTLFormulaBinaryOperator.U, left, right)


class LTLAtomicFormula(LTLBaseFormula):
    def __init__(self, id: str):
        super().__init__(LTLFormulaType.ATOMIC)
        self.id = id

    def sub_formula(self) -> list:
        return []

    def __str__(self) -> str:
        return self.id
