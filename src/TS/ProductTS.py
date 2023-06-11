from BA.NBA import NBA
from Formula.utils import print_formula_list, formula_list_equal, cross_formula_list
from TS.TS import TS
from TS.utils import *


class ProductTS():
    def state_index(self, ts_state: TSState, nba_node: BANode):
        return self.src_ts.states.index(ts_state) * len(self.src_nba.nodes) + self.src_nba.nodes.index(nba_node)

    def __init__(self, ts: TS, nba: NBA, atomic_formulas: list[LTLBaseFormula]):
        self.src_ts = ts
        self.src_nba = nba
        self.states = []
        self.init_states = []
        for i in range(len(ts.states)):
            for j in range(len(nba.nodes)):
                self.states.append(ProductTSState(ts.states[i], nba.nodes[j]))

        for s0 in ts.init_states:
            for q0 in nba.start_nodes:
                for edge in q0.edges:
                    if formula_list_equal(s0.prop, edge.symbol_formula):
                        q = edge.dst
                        self.init_states.append(
                            self.states[self.state_index(s0, q)])

        for s in ts.states:
            for q in nba.nodes:
                for trans in s.trans:
                    t = trans.dst
                    for edge in q.edges:
                        p = edge.dst
                        prop = cross_formula_list(t.prop, atomic_formulas)
                        if formula_list_equal(prop, edge.symbol_formula):
                            self.states[self.state_index(s, q)].trans.append(
                                ProductTSTransition(self.states[self.state_index(t, p)]))

    def print(self):
        print('Printing Transition System...')
        print('n_states: {}, n_init_states: {}'.format(
            len(self.states), len(self.init_states)))
        print('initial states are:')
        for s in self.init_states:
            print(self.states.index(s), end=' ')
        print()
        print('mapping to TS and NBA is:')
        for i in range(len(self.src_ts.states)):
            for j in range(len(self.src_nba.nodes)):
                print('{}: ({}, {})'.format(
                    i * len(self.src_nba.nodes) + j, i, j), end=' ')
            print()
        print('transitions are:')
        for i in range(len(self.states)):
            print('{}: '.format(i), end='')
            for trans in self.states[i].trans:
                print(self.states.index(trans.dst), end=' ')
            print()
