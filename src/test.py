import sys
from antlr4 import *
from Parser.LTLLexer import LTLLexer
from Parser.LTLParser import LTLParser
from Parser.LTLVisitor import LTLVisitor
from Formula.utils import closure, gen_elementary_subsets, collect_atomic_formula, print_formula_list
from Formula.LTLFormula import *
from BA.GNBA import GNBA
from BA.NBA import NBA
from TS.TS import TS

TS_PATH = 'TS.txt' if len(sys.argv) < 2 else sys.argv[1]
BENCHMARK_PATH = 'benchmark.txt' if len(sys.argv) < 3 else sys.argv[2]


def build_ts():
    with open(TS_PATH) as f_ts:
        n_states, n_trans = map(int, f_ts.readline().split())
        init_states = list(map(int, f_ts.readline().split()))
        action_map = {}
        for action in list(map(str, f_ts.readline().split())):
            action_map[len(action_map)] = action
        ap_map = {}
        for ap in list(map(str, f_ts.readline().split())):
            f = LTLAtomicFormula(ap)
            ap_map[len(ap_map)] = f
        trans = []
        for _ in range(n_trans):
            src, act, dst = map(int, f_ts.readline().split())
            trans.append((src, act, dst))
        ap_states = []
        for _ in range(n_states):
            ap_states.append(list(map(int, f_ts.readline().split())))
        return TS(n_states, init_states, action_map, ap_map, trans, ap_states)


def build_NBA(formula_str: str):
    input_stream = InputStream(formula_str)
    lexer = LTLLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = LTLParser(stream)
    tree = parser.formula()
    root_formula = LTLVisitor().visit(tree)
    cl = closure(root_formula)
    # print_formula_list(cl)

    elementary_sets = gen_elementary_subsets(cl)
    atomic_formulas = collect_atomic_formula(root_formula)
    # print_formula_list(atomic_formulas)
    gnba = GNBA(elementary_sets, atomic_formulas, cl, root_formula)
    # gnba.print()
    nba = NBA(gnba)
    nba.print()
    return nba


def parse_benchmark():
    ret = []
    with open(BENCHMARK_PATH) as f_benchmark:
        n, m = map(int, f_benchmark.readline().split())
        for _ in range(n):
            formula_str = f_benchmark.readline()
            ret.append([None, formula_str])
        for _ in range(m):
            sp = f_benchmark.readline().split()
            init_node = int(sp[0])
            formula_str = ' '.join(sp[1:])
            ret.append([[init_node], formula_str])
    return ret


def main():
    ts = build_ts()
    ts.print()
    bcs = parse_benchmark()
    print(bcs)
    for bc in bcs:
        print(bc[1])
        build_NBA(bc[1])


if __name__ == '__main__':
    main()
