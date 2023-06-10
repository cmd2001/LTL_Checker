# Generated from LTL.g4 by ANTLR 4.13.0
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,12,33,2,0,7,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,
        0,1,0,1,0,3,0,17,8,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,5,0,28,
        8,0,10,0,12,0,31,9,0,1,0,0,1,0,1,0,0,1,1,0,10,11,39,0,16,1,0,0,0,
        2,3,6,0,-1,0,3,4,5,1,0,0,4,17,3,0,0,9,5,6,5,2,0,0,6,17,3,0,0,8,7,
        8,5,3,0,0,8,17,3,0,0,7,9,10,5,4,0,0,10,17,3,0,0,6,11,17,5,9,0,0,
        12,13,5,7,0,0,13,14,3,0,0,0,14,15,5,8,0,0,15,17,1,0,0,0,16,2,1,0,
        0,0,16,5,1,0,0,0,16,7,1,0,0,0,16,9,1,0,0,0,16,11,1,0,0,0,16,12,1,
        0,0,0,17,29,1,0,0,0,18,19,10,5,0,0,19,20,7,0,0,0,20,28,3,0,0,6,21,
        22,10,4,0,0,22,23,5,5,0,0,23,28,3,0,0,5,24,25,10,3,0,0,25,26,5,6,
        0,0,26,28,3,0,0,4,27,18,1,0,0,0,27,21,1,0,0,0,27,24,1,0,0,0,28,31,
        1,0,0,0,29,27,1,0,0,0,29,30,1,0,0,0,30,1,1,0,0,0,31,29,1,0,0,0,3,
        16,27,29
    ]

class LTLParser ( Parser ):

    grammarFileName = "LTL.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'!'", "'G'", "'F'", "'X'", "'->'", "'U'", 
                     "'('", "')'", "<INVALID>", "'/\\'", "'\\/'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "Identifier", "AndOp", "OrOp", "WS" ]

    RULE_formula = 0

    ruleNames =  [ "formula" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    Identifier=9
    AndOp=10
    OrOp=11
    WS=12

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.0")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class FormulaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return LTLParser.RULE_formula

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class Formula_in_parenthesesContext(FormulaContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LTLParser.FormulaContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def formula(self):
            return self.getTypedRuleContext(LTLParser.FormulaContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFormula_in_parentheses" ):
                return visitor.visitFormula_in_parentheses(self)
            else:
                return visitor.visitChildren(self)


    class Logic_formulaContext(FormulaContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LTLParser.FormulaContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def formula(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LTLParser.FormulaContext)
            else:
                return self.getTypedRuleContext(LTLParser.FormulaContext,i)

        def AndOp(self):
            return self.getToken(LTLParser.AndOp, 0)
        def OrOp(self):
            return self.getToken(LTLParser.OrOp, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogic_formula" ):
                return visitor.visitLogic_formula(self)
            else:
                return visitor.visitChildren(self)


    class Not_formulaContext(FormulaContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LTLParser.FormulaContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def formula(self):
            return self.getTypedRuleContext(LTLParser.FormulaContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNot_formula" ):
                return visitor.visitNot_formula(self)
            else:
                return visitor.visitChildren(self)


    class G_formulaContext(FormulaContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LTLParser.FormulaContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def formula(self):
            return self.getTypedRuleContext(LTLParser.FormulaContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitG_formula" ):
                return visitor.visitG_formula(self)
            else:
                return visitor.visitChildren(self)


    class Atomic_propositionContext(FormulaContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LTLParser.FormulaContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def Identifier(self):
            return self.getToken(LTLParser.Identifier, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAtomic_proposition" ):
                return visitor.visitAtomic_proposition(self)
            else:
                return visitor.visitChildren(self)


    class U_formulaContext(FormulaContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LTLParser.FormulaContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def formula(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LTLParser.FormulaContext)
            else:
                return self.getTypedRuleContext(LTLParser.FormulaContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitU_formula" ):
                return visitor.visitU_formula(self)
            else:
                return visitor.visitChildren(self)


    class X_formulaContext(FormulaContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LTLParser.FormulaContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def formula(self):
            return self.getTypedRuleContext(LTLParser.FormulaContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitX_formula" ):
                return visitor.visitX_formula(self)
            else:
                return visitor.visitChildren(self)


    class Implication_formulaContext(FormulaContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LTLParser.FormulaContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def formula(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LTLParser.FormulaContext)
            else:
                return self.getTypedRuleContext(LTLParser.FormulaContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitImplication_formula" ):
                return visitor.visitImplication_formula(self)
            else:
                return visitor.visitChildren(self)


    class F_formulaContext(FormulaContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LTLParser.FormulaContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def formula(self):
            return self.getTypedRuleContext(LTLParser.FormulaContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitF_formula" ):
                return visitor.visitF_formula(self)
            else:
                return visitor.visitChildren(self)



    def formula(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = LTLParser.FormulaContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 0
        self.enterRecursionRule(localctx, 0, self.RULE_formula, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 16
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                localctx = LTLParser.Not_formulaContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 3
                self.match(LTLParser.T__0)
                self.state = 4
                self.formula(9)
                pass
            elif token in [2]:
                localctx = LTLParser.G_formulaContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 5
                self.match(LTLParser.T__1)
                self.state = 6
                self.formula(8)
                pass
            elif token in [3]:
                localctx = LTLParser.F_formulaContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 7
                self.match(LTLParser.T__2)
                self.state = 8
                self.formula(7)
                pass
            elif token in [4]:
                localctx = LTLParser.X_formulaContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 9
                self.match(LTLParser.T__3)
                self.state = 10
                self.formula(6)
                pass
            elif token in [9]:
                localctx = LTLParser.Atomic_propositionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 11
                self.match(LTLParser.Identifier)
                pass
            elif token in [7]:
                localctx = LTLParser.Formula_in_parenthesesContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 12
                self.match(LTLParser.T__6)
                self.state = 13
                self.formula(0)
                self.state = 14
                self.match(LTLParser.T__7)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 29
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 27
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
                    if la_ == 1:
                        localctx = LTLParser.Logic_formulaContext(self, LTLParser.FormulaContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_formula)
                        self.state = 18
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 19
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==10 or _la==11):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 20
                        self.formula(6)
                        pass

                    elif la_ == 2:
                        localctx = LTLParser.Implication_formulaContext(self, LTLParser.FormulaContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_formula)
                        self.state = 21
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 22
                        self.match(LTLParser.T__4)
                        self.state = 23
                        self.formula(5)
                        pass

                    elif la_ == 3:
                        localctx = LTLParser.U_formulaContext(self, LTLParser.FormulaContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_formula)
                        self.state = 24
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 25
                        self.match(LTLParser.T__5)
                        self.state = 26
                        self.formula(4)
                        pass

             
                self.state = 31
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[0] = self.formula_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def formula_sempred(self, localctx:FormulaContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 3)
         




