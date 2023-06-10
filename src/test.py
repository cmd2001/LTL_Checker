import sys
from antlr4 import *
from parser.LTLLexer import LTLLexer
from parser.LTLParser import LTLParser
from parser.LTLVisitor import LTLVisitor
from utils.FormulaUtil import closure, gen_subsets, check_elementary


def main(argv):
    input_stream = FileStream(argv[1])
    lexer = LTLLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = LTLParser(stream)
    tree = parser.formula()
    root_formula = LTLVisitor().visit(tree)
    print(root_formula.__str__())
    cl = closure(root_formula)
    for f in cl:
        print(f.__str__(), end=' || ')
    print()
    print(len(cl))
    sss = gen_subsets(cl)
    for ss in sss:
        if check_elementary(ss, cl):
            for f in ss:
                print(f.__str__(), end=' || ')
            print()


if __name__ == '__main__':
    main(sys.argv)
