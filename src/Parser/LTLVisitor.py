# Generated from LTL.g4 by ANTLR 4.13.0
from antlr4 import *
if "." in __name__:
    from .LTLParser import LTLParser
else:
    from LTLParser import LTLParser

# This class defines a complete generic visitor for a parse tree produced by LTLParser.

from Formula.LTLFormula import *


class LTLVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by LTLParser#formula_in_parentheses.
    def visitFormula_in_parentheses(self, ctx: LTLParser.Formula_in_parenthesesContext):
        # print(ctx.formula().getText())
        return self.visit(ctx.formula())

    # Visit a parse tree produced by LTLParser#logic_formula.
    def visitLogic_formula(self, ctx: LTLParser.Logic_formulaContext):
        # print('visit logic')
        return LTLLogicFormula(LTLFormulaBinaryOperator.AND if ctx.AndOp() else LTLFormulaBinaryOperator.OR, self.visit(ctx.formula()[0]), self.visit(ctx.formula()[1]))

    # Visit a parse tree produced by LTLParser#not_formula.
    def visitNot_formula(self, ctx: LTLParser.Not_formulaContext):
        # print('visit not')
        return build_not_formula(self.visit(ctx.formula()))

    # Visit a parse tree produced by LTLParser#g_formula.
    def visitG_formula(self, ctx: LTLParser.G_formulaContext):
        # print('visit G')
        return LTLAlwaysFormula(self.visit(ctx.formula()))

    # Visit a parse tree produced by LTLParser#atomic_proposition.
    def visitAtomic_proposition(self, ctx: LTLParser.Atomic_propositionContext):
        # print('visit Atomic')
        return LTLAtomicFormula(ctx.Identifier().getText())

    # Visit a parse tree produced by LTLParser#u_formula.
    def visitU_formula(self, ctx: LTLParser.U_formulaContext):
        # print('visit U')
        return LTLUntilFormula(self.visit(ctx.formula()[0]), self.visit(ctx.formula()[1]))

    # Visit a parse tree produced by LTLParser#x_formula.
    def visitX_formula(self, ctx: LTLParser.X_formulaContext):
        # print('visit X')
        return LTLNextFormula(self.visit(ctx.formula()))

    # Visit a parse tree produced by LTLParser#implication_formula.
    def visitImplication_formula(self, ctx: LTLParser.Implication_formulaContext):
        # print('visit IMPL')
        return LTLIMPLFormula(self.visit(ctx.formula()[0]), self.visit(ctx.formula()[1]))

    # Visit a parse tree produced by LTLParser#f_formula.
    def visitF_formula(self, ctx: LTLParser.F_formulaContext):
        # print('visit F')
        return LTLEventuallyFormula(self.visit(ctx.formula()))

    # Visit a parse tree produced by LTLParser#logic_true.
    def visitLogic_true(self, ctx: LTLParser.Logic_trueContext):
        return self.visitChildren(ctx)


del LTLParser
