from utils.LTLFormula import *


def neg_logic_operator(o: LTLFormulaBinaryOperator) -> LTLFormulaBinaryOperator:
    if o == LTLFormulaBinaryOperator.AND:
        return LTLFormulaBinaryOperator.OR
    if o == LTLFormulaBinaryOperator.OR:
        return LTLFormulaBinaryOperator.AND
    raise Exception("Not a logic operator")


def is_equal(a: LTLBaseFormula, b: LTLBaseFormula) -> bool:
    if a.__str__() == b.__str__():
        return True

    # solve not fiormula first
    if isinstance(a, LTLNotFormula):
        # test !!T and T
        if isinstance(a.child, LTLNotFormula):
            if is_equal(a.child.child, b):
                return True
        # test !(T/\V) = (!T)\/(!V)
        if isinstance(a.child, LTLLogicFormula):
            tempFormula = LTLLogicFormula(neg_logic_operator(
                a.child.operator), LTLNotFormula(a.child.left), LTLNotFormula(a.child.right))
            if is_equal(tempFormula, b):
                return True
        return a.__str__() == b.__str__()
    if isinstance(b, LTLNotFormula):
        return is_equal(b, a)

    # now b have no Not. a may have Not

    # a ? b = b ? a
    if isinstance(a, LTLLogicFormula):
        if not isinstance(b, LTLLogicFormula):
            return False
        if a.operator != b.operator:
            return False
        if is_equal(a.left, b.left) and is_equal(a.right, b.right):
            return True
        if is_equal(a.left, b.right) and is_equal(a.right, b.left):
            return True
        return False

    # a -> b = !b -> !a

    if isinstance(a, LTLIMPLFormula):
        if not isinstance(b, LTLIMPLFormula):
            return False
        if is_equal(a.left, a.left) and is_equal(a.right, b.right):
            return True
        if is_equal(LTLNotFormula(a.right), b.left) and is_equal(LTLNotFormula(a.left), b.right):
            return True
        return False

    return False


def formula_in_list(f: LTLBaseFormula, l: list[LTLBaseFormula]):
    for i in range(len(l)):
        if is_equal(f, l[i]):
            return True
    return False


def merge_formula_list(a: list[LTLBaseFormula], b: list[LTLBaseFormula]) -> list[LTLBaseFormula]:
    ret = [a[i] for i in range(len(a))]
    for i in range(len(b)):
        if not formula_in_list(b[i], ret):
            ret.append(b[i])
    return ret


def closure(f: LTLBaseFormula):
    ret = [f, LTLNotFormula(f)]
    for sub_formula in f.sub_formula():
        ret = merge_formula_list(ret, closure(sub_formula))
    return ret


def check_elementary(s: list[LTLBaseFormula], cl: list[LTLBaseFormula]):
    for f in cl:
        f_in = formula_in_list(f, s)
        negf_in = formula_in_list(LTLNotFormula(f), s)
        if f_in == negf_in:
            return False
        if isinstance(f, LTLLogicFormula) or isinstance(f, LTLUntilFormula):
            left_in = formula_in_list(f.left, s)
            right_in = formula_in_list(f.right, s)
        if isinstance(f, LTLLogicFormula) and f.operator == LTLFormulaBinaryOperator.AND:
            if f_in != left_in or f_in != right_in or left_in != right_in:
                return False
        if isinstance(f, LTLUntilFormula):
            if right_in and not f_in:
                return False
            if (f_in and not right_in) and not left_in:
                return False
    return True


def gen_subsets(s: list) -> list:
    if len(s) == 0:
        return [[]]
    ret = []
    gs = gen_subsets(s[1:])
    for g in gs:
        ret.append(g)
        ret.append([s[0]] + g)
    return ret
