import Queue

from State import State
from State import StateHeuristic
from Variable import Variable


__author__ = 'ryuzakinho'


def breadth_search(clause_list_, nbr_variable):
    """
    Performs breadth search on a cnf file in order to find a model that satisfies our clauses.
    :rtype : State
    """
    state_queue = Queue.Queue(0)
    state = State(clause_list_)
    state_queue.put(state)
    nbr_states = 1
    nbr_bad_states = 0
    max_size_queue = 1
    # LOOP
    while True:
        if state_queue.empty():
            return None
        else:
            if state_queue.qsize() > max_size_queue:
                max_size_queue = state_queue.qsize()
            state = state_queue.get()
            if len(state.unsat_clause_list) == 0:
                return state, nbr_states, nbr_bad_states, max_size_queue
            else:
                if state.variable is not None:
                    var_num = state.variable.variable_number + 1
                    if var_num > nbr_variable:
                        return None
                else:
                    var_num = 1

                while len(Variable.where_is_the_variable(clause_list_, var_num)) == 0:
                    var_num += 1

                child1 = State.create_child_state(var_num, state.already_assigned_variables, state.unsat_clause_list,
                                                  True)
                child2 = State.create_child_state(var_num, state.already_assigned_variables, state.unsat_clause_list,
                                                  False)
                if child1 is not None:
                    nbr_states += 1
                    if len(child1.unsat_clause_list) == 0:
                        return child1, nbr_states, nbr_bad_states, max_size_queue
                    state_queue.put(child1)
                else:
                    nbr_bad_states += 1
                if child2 is not None:
                    nbr_states += 1
                    if len(child2.unsat_clause_list) == 0:
                        return child2, nbr_states, nbr_bad_states, max_size_queue
                    state_queue.put(child2)
                else:
                    nbr_bad_states += 1

def depth_search(clause_list_, nbr_variable):
    """
    This function looks for a solution that satisfies our clauses using depth first strategy.
    :param clause_list_:
    :param nbr_variable:
    :return: tuple
    """
    state_queue = Queue.LifoQueue(0)
    state = State(clause_list_)
    state_queue.put(state)
    nbr_states = 1
    nbr_bad_states = 0
    max_size_queue = 0
    # LOOP
    while True:
        if state_queue.empty():
            return None
        else:
            if state_queue.qsize() > max_size_queue:
                max_size_queue = state_queue.qsize()
            state = state_queue.get()
            if len(state.unsat_clause_list) == 0:
                return state, nbr_states, nbr_bad_states, max_size_queue
            else:
                if state.variable is not None:
                    var_num = state.variable.variable_number + 1
                    if var_num > nbr_variable:
                        return None
                else:
                    var_num = 1

                while len(Variable.where_is_the_variable(clause_list_, var_num)) == 0:
                    var_num += 1

                child1 = State.create_child_state(var_num, state.already_assigned_variables, state.unsat_clause_list,
                                                  True)
                child2 = State.create_child_state(var_num, state.already_assigned_variables, state.unsat_clause_list,
                                                  False)
                if child2 is not None:
                    nbr_states += 1
                    if len(child2.unsat_clause_list) == 0:
                        return child2, nbr_states, nbr_bad_states, max_size_queue
                    state_queue.put(child2)
                else:
                    nbr_bad_states += 1
                if child1 is not None:
                    nbr_states += 1
                    if len(child1.unsat_clause_list) == 0:
                        return child1, nbr_states, nbr_bad_states, max_size_queue
                    state_queue.put(child1)
                else:
                    nbr_bad_states += 1


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


def a_star(clause_list_, nbr_variable, heuristic):
    """
    Uses the heuristic that calculates the smallest number of non satisfied clauses in state.
    :param clause_list_:
    :param nbr_variable : Integer
    :param heuristic : Integer
    :return: tuple
    """
    open_list = list()
    # close_list = list()
    state = StateHeuristic(clause_list_)
    state.g = state.h = 0
    open_list.append(state)
    nbr_states = 1
    nbr_bad_states = 0
    max_size_list = 1

    while len(open_list) > 0:
        if len(open_list) > max_size_list:
            max_size_list = len(open_list)
        open_state = find_smallest_f(open_list)
        state = open_list.pop(open_list.index(open_state))
        if len(state.unsat_clause_list) == 0:
            return state, nbr_states, nbr_bad_states, max_size_list

        if len(state.already_assigned_variables) > nbr_variable:
            return None
        if heuristic == 1:
            child1 = StateHeuristic.create_child_state_heuristic_min_unsat_clauses(len(state.already_assigned_variables)+1,
                                                                 state.already_assigned_variables, state.unsat_clause_list,
                                                                 True)
            child2 = StateHeuristic.create_child_state_heuristic_min_unsat_clauses(len(state.already_assigned_variables)+1,
                                                             state.already_assigned_variables, state.unsat_clause_list,
                                                             False)
        elif heuristic == 2:
            child1 = StateHeuristic.create_child_state_heuristic_max_occuring_vars(len(state.already_assigned_variables)+1,
                                                                 state.already_assigned_variables, state.unsat_clause_list, len(clause_list_),
                                                                 True)
            child2 = StateHeuristic.create_child_state_heuristic_max_occuring_vars(len(state.already_assigned_variables)+1,
                                                             state.already_assigned_variables, state.unsat_clause_list, len(clause_list_),
                                                             False)
        elif heuristic == 3:
            child1 = StateHeuristic.create_child_state_heuristic_sum_two(len(state.already_assigned_variables)+1,
                                                                 state.already_assigned_variables, state.unsat_clause_list, len(clause_list_),
                                                                 True)
            child2 = StateHeuristic.create_child_state_heuristic_sum_two(len(state.already_assigned_variables)+1,
                                                             state.already_assigned_variables, state.unsat_clause_list, len(clause_list_),
                                                             False)

        if child1 is not None:
            nbr_states += 1
            open_list.append(child1)
        else:
            nbr_bad_states += 1

        if child2 is not None:
            nbr_states += 1
            open_list.append(child2)
        else:
            nbr_bad_states += 1

            # close_list.append(state)
