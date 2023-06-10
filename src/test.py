import sys
from antlr4 import *
from parser.LTLLexer import LTLLexer
from parser.LTLParser import LTLParser
from parser.LTLVisitor import LTLVisitor
from Formula.utils import closure, gen_elementary_subsets, collect_atomic_formula, print_formula_list
from Formula.LTLFormula import *
from BA.GNBA import GNBA

def main(argv):
    input_stream = FileStream(argv[1])
    lexer = LTLLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = LTLParser(stream)
    tree = parser.formula()
    root_formula = LTLVisitor().visit(tree)
    print(root_formula.__str__())
    cl = closure(root_formula)
    print_formula_list(cl)
    print(len(cl))
    
    elementary_sets = gen_elementary_subsets(cl)
    print(len(elementary_sets))
    atomic_formulas = collect_atomic_formula(root_formula)
    print_formula_list(atomic_formulas)
    gnba = GNBA(elementary_sets, atomic_formulas, cl, root_formula)
    print(len(gnba.nodes))


if __name__ == '__main__':
    main(sys.argv)
