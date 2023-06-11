grammar LTL;

formula
    : '!' formula                           # not_formula
    | 'G' formula                           # g_formula
    | 'F' formula                           # f_formula
    | 'X' formula                           # x_formula
    | formula op = (AndOp | OrOp) formula   # logic_formula
    | formula '->' formula                  # implication_formula
    | formula 'U' formula                   # u_formula
    | LogicTrue                             # logic_true
    | Identifier                             # atomic_proposition
    | '(' formula ')'                       # formula_in_parentheses
    ;


Identifier
    : [a-z]
    ;

AndOp
    : '/\\'
    ;

OrOp
    : '\\/'
    ;

LogicTrue:
    'true'
    ;

WS : [ \t\n\r]+ -> skip ;