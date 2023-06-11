from BA.NBA import NBA
from Formula.utils import print_formula_list, formula_list_equal, cross_formula_list, formula_in_list
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
            # print('s0 : {}'.format(ts.states.index(s0)))
            for q0 in nba.start_nodes:
                for edge in q0.edges:
                    prop = cross_formula_list(s0.prop, atomic_formulas)
                    symbol_formula = cross_formula_list(
                        edge.symbol_formula, atomic_formulas)
                    # print('prop:', end=' ')
                    # print_formula_list(prop)
                    # print('symbol_formula:', end=' ')
                    # print_formula_list(symbol_formula)
                    if formula_list_equal(prop, symbol_formula):
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
                        symbol_formula = cross_formula_list(
                            edge.symbol_formula, atomic_formulas)
                        if formula_list_equal(prop, symbol_formula):
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

    @staticmethod
    def list_exclude_list(l1: list, l2: list):
        ret = []
        for i in l1:
            if not i in l2:
                ret.append(i)
        return ret

    @staticmethod
    def push_list(l: list, x):
        if not x in l:
            l.append(x)

    def nested_dfs(self, root_formula: LTLBaseFormula):
        self.R = []
        self.U = []
        self.T = []
        self.V = []
        self.cycle_found = False
        self.root_formula = root_formula

        while len(ProductTS.list_exclude_list(self.init_states, self.R)) > 0 and not self.cycle_found:
            s = ProductTS.list_exclude_list(self.init_states, self.R)[0]
            # print('s = {}'.format(self.states.index(s)))
            self.reachable_cycle(s)
        if not self.cycle_found:
            return True
        else:
            # for state in self.V:
            #     print(self.states.index(state), end=' ')
            # print()
            return False

    def reachable_cycle(self, s: ProductTSState):
        ProductTS.push_list(self.U, s)
        ProductTS.push_list(self.R, s)
        while True:
            s1 = self.U[-1]
            # print('s1 = {}'.format(self.states.index(s1)))
            post = []
            for trans in s1.trans:
                post.append(trans.dst)
            excluded_list = ProductTS.list_exclude_list(post, self.R)
            if len(excluded_list):
                s2 = excluded_list[0]
                ProductTS.push_list(self.U, s2)
                ProductTS.push_list(self.R, s2)
            else:
                self.U.pop()
                if not formula_in_list(self.root_formula, s1.nba_node.id_formula):
                    # print('bad s1: {}'.format(self.states.index(s1)))
                    # print('id_formula is:', end='')
                    # print_formula_list(s1.nba_node.id_formula)
                    self.cycle_found = self.cycle_check(s1)
                # else:
                #     print('good s1: {}'.format(self.states.index(s1)))
                #     print('id_formula is:', end='')
                #     print_formula_list(s1.nba_node.id_formula)
            if len(self.U) == 0 or self.cycle_found:
                break

    def cycle_check(self, s: ProductTSState):
        cycle_found = False
        ProductTS.push_list(self.V, s)
        ProductTS.push_list(self.T, s)
        while True:
            s1 = self.V[-1]
            post = []
            for trans in s1.trans:
                post.append(trans.dst)
            if s in post:
                cycle_found = True
                ProductTS.push_list(self.V, s)
            else:
                excluded_list = ProductTS.list_exclude_list(post, self.T)
                if len(excluded_list):
                    s2 = excluded_list[0]
                    ProductTS.push_list(self.V, s2)
                    ProductTS.push_list(self.T, s2)
                else:
                    self.V.pop()
            if len(self.V) == 0 or cycle_found:
                break
        return cycle_found
