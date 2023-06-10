# Generated from LTL.g4 by ANTLR 4.13.0
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,12,57,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,
        6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,1,0,1,0,1,1,1,
        1,1,2,1,2,1,3,1,3,1,4,1,4,1,4,1,5,1,5,1,6,1,6,1,7,1,7,1,8,1,8,1,
        9,1,9,1,9,1,10,1,10,1,10,1,11,4,11,52,8,11,11,11,12,11,53,1,11,1,
        11,0,0,12,1,1,3,2,5,3,7,4,9,5,11,6,13,7,15,8,17,9,19,10,21,11,23,
        12,1,0,2,1,0,97,122,3,0,9,10,13,13,32,32,57,0,1,1,0,0,0,0,3,1,0,
        0,0,0,5,1,0,0,0,0,7,1,0,0,0,0,9,1,0,0,0,0,11,1,0,0,0,0,13,1,0,0,
        0,0,15,1,0,0,0,0,17,1,0,0,0,0,19,1,0,0,0,0,21,1,0,0,0,0,23,1,0,0,
        0,1,25,1,0,0,0,3,27,1,0,0,0,5,29,1,0,0,0,7,31,1,0,0,0,9,33,1,0,0,
        0,11,36,1,0,0,0,13,38,1,0,0,0,15,40,1,0,0,0,17,42,1,0,0,0,19,44,
        1,0,0,0,21,47,1,0,0,0,23,51,1,0,0,0,25,26,5,33,0,0,26,2,1,0,0,0,
        27,28,5,71,0,0,28,4,1,0,0,0,29,30,5,70,0,0,30,6,1,0,0,0,31,32,5,
        88,0,0,32,8,1,0,0,0,33,34,5,45,0,0,34,35,5,62,0,0,35,10,1,0,0,0,
        36,37,5,85,0,0,37,12,1,0,0,0,38,39,5,40,0,0,39,14,1,0,0,0,40,41,
        5,41,0,0,41,16,1,0,0,0,42,43,7,0,0,0,43,18,1,0,0,0,44,45,5,47,0,
        0,45,46,5,92,0,0,46,20,1,0,0,0,47,48,5,92,0,0,48,49,5,47,0,0,49,
        22,1,0,0,0,50,52,7,1,0,0,51,50,1,0,0,0,52,53,1,0,0,0,53,51,1,0,0,
        0,53,54,1,0,0,0,54,55,1,0,0,0,55,56,6,11,0,0,56,24,1,0,0,0,2,0,53,
        1,6,0,0
    ]

class LTLLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    T__6 = 7
    T__7 = 8
    Identifier = 9
    AndOp = 10
    OrOp = 11
    WS = 12

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'!'", "'G'", "'F'", "'X'", "'->'", "'U'", "'('", "')'", "'/\\'", 
            "'\\/'" ]

    symbolicNames = [ "<INVALID>",
            "Identifier", "AndOp", "OrOp", "WS" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "Identifier", "AndOp", "OrOp", "WS" ]

    grammarFileName = "LTL.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.0")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


