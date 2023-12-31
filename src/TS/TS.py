from TS.utils import *
from Formula.utils import print_formula_list, formula_list_equal


class TS():
    def change_init(self, init_states: list[int] | None) -> None:
        if init_states == None:
            self.init_states = self.back_init
            return
        self.init_states = []
        for i in init_states:
            self.init_states.append(self.states[i])

    def __init__(self, n_states: int, init_states: list[int], action_map: dict[int, str], ap_map: dict[int, LTLBaseFormula], trans: list[tuple[int, int, int]], ap_states: list[list[int]]) -> None:
        self.states = []
        self.init_states = []
        for i in range(n_states):
            prop = []
            for ap in ap_states[i]:
                if ap == -1:
                    continue
                prop.append(ap_map[ap])
            self.states.append(TSState(i, prop))
            if i in init_states:
                self.init_states.append(self.states[i])
        for src, act, dst in trans:
            trans = TSTransition(action_map[act], self.states[dst])
            self.states[src].trans.append(trans)
        self.back_init = self.init_states.copy()

    def print(self):
        print('Printing Transition System...')
        print('n_states: {}, n_init_states: {}'.format(
            len(self.states), len(self.init_states)))
        print('initial states are:')
        for s in self.init_states:
            print(self.states.index(s), end=' ')
        print()
        print('formula at each state are:')
        for i in range(len(self.states)):
            print('{}: '.format(i), end='')
            print_formula_list(self.states[i].prop)
        print('transitions are:')
        for i in range(len(self.states)):
            print('{}: '.format(i), end='')
            for trans in self.states[i].trans:
                print(self.states.index(trans.dst), end=' ')
            print()
