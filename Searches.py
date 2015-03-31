import Queue

from State import State
from State import StateHeuristic


__author__ = 'ryuzakinho'


def breadth_search(clause_list_, nbr_variable):
    """
    Performs breadth search on a cnf file in order to find a model that satisfies our clauses.
    :rtype : State
    """
    state_queue = Queue.Queue(0)
    state = State(clause_list_)
    state_queue.put(state)
    # LOOP
    while True:
        if state_queue.empty():
            return None
        else:
            state = state_queue.get()
            if len(state.unsat_clause_list) == 0:
                return state
            else:
                if state.variable is not None:
                    var_num = state.variable.variable_number + 1
                    if var_num > nbr_variable:
                        return None
                else:
                    var_num = 1
                child1 = State.create_child_state(var_num, state.already_assigned_variables, state.unsat_clause_list,
                                                  True)
                child2 = State.create_child_state(var_num, state.already_assigned_variables, state.unsat_clause_list,
                                                  False)
                if child1 is not None:
                    if len(child1.unsat_clause_list) == 0:
                        return child1
                    state_queue.put(child1)
                if child2 is not None:
                    if len(child2.unsat_clause_list) == 0:
                        return child2
                    state_queue.put(child2)


def depth_search(clause_list_, nbr_variable):
    """
    This function looks for a solution that satisfies our clauses using depth first strategy.
    :param clause_list_:
    :param nbr_variable:
    :return:
    """
    state_queue = Queue.LifoQueue(0)
    state = State(clause_list_)
    state_queue.put(state)
    # LOOP
    while True:
        if state_queue.empty():
            return None
        else:
            state = state_queue.get()
            if len(state.unsat_clause_list) == 0:
                return state
            else:
                if state.variable is not None:
                    var_num = state.variable.variable_number + 1
                    if var_num > nbr_variable:
                        return None
                else:
                    var_num = 1
                child1 = State.create_child_state(var_num, state.already_assigned_variables, state.unsat_clause_list,
                                                  True)
                child2 = State.create_child_state(var_num, state.already_assigned_variables, state.unsat_clause_list,
                                                  False)
                if child2 is not None:
                    if len(child2.unsat_clause_list) == 0:
                        return child2
                    state_queue.put(child2)
                if child1 is not None:
                    if len(child1.unsat_clause_list) == 0:
                        return child1
                    state_queue.put(child1)


def find_smallest_f(open_list):
    """
    Looks for the state with the smallest f to apply A* algorithm.
    f = g + h
    :param open_list:
    :return: StateHeuristic
    """
    f = ((open_list[0]).g + (open_list[0]).h)
    smallest_f_state = open_list[0]
    for state in open_list:
        if (state.g + state.h) < f:
            smallest_f_state = state
            f = (state.g + state.h)
    return smallest_f_state


def exists_in_already_assigned_variables(var_number, already_assigned_variables):
    for tup in already_assigned_variables:
        if tup[0] == var_number:
            return True
    return False


def already_assigned_in_parent(var_number, open_state):
    """
    Checks wether a vraiable was already assigned.
    :param var_number:
    :param open_state:
    :return: bool
    """
    for variable in open_state.already_assigned_variables:
        if variable[0] == var_number:
            return True
    return False


def first_heuristic_search(clause_list_, nbr_variable):
    """
    Uses the heuristic that calculates the smallest number of non satisfied clauses in state.
    :param clause_list_:
    :param nbr_variable : Integer
    :return: StateHeuristic
    """
    open_list = list()
    # close_list = list()
    state = StateHeuristic(clause_list_)
    state.g = state.h = 0
    open_list.append(state)

    while len(open_list) > 0:
        open_state = find_smallest_f(open_list)
        state = open_list.pop(open_list.index(open_state))
        if len(state.unsat_clause_list) == 0:
            return state
        nbr = len(state.already_assigned_variables)
        if nbr > nbr_variable:
            return None
        child1 = StateHeuristic.create_child_state_heuristic(len(state.already_assigned_variables)+1,
                                                             state.already_assigned_variables, state.unsat_clause_list,
                                                             True)
        if child1 is not None:
            open_list.append(child1)
        child2 = StateHeuristic.create_child_state_heuristic(len(state.already_assigned_variables)+1,
                                                             state.already_assigned_variables, state.unsat_clause_list,
                                                             False)
        if child2 is not None:
            open_list.append(child2)

            # close_list.append(state)

def second_heuristic_search():
    print ""