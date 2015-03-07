__author__ = 'ryuzakinho'
from file import File
from State import State
from Variable import Variable
import Queue
import copy


def create_child_state(var_num, already_assigned_variables, unsat_clause_list, truth_assignement):
    """
    Generates the child states to be put in the queue.
    :rtype : State
    """
    var_position_child = Variable.where_is_the_variable(unsat_clause_list, var_num)
    if len(var_position_child) == 0:
        return None
    unsat_clause_list_child = copy.deepcopy(unsat_clause_list)

    if truth_assignement:
        while len(var_position_child) > 0:
            position = var_position_child[0]
            if unsat_clause_list_child[position[0]][position[1]] > 0:
                unsat_clause_list_child.pop(position[0])
            else:
                unsat_clause_list_child[position[0]].pop(position[1])
                if len(unsat_clause_list_child[position[0]]) == 0:
                    return None

            var_position_child = Variable.where_is_the_variable(unsat_clause_list_child, var_num)
    else:
        while len(var_position_child) > 0:
            position = var_position_child[0]
            if unsat_clause_list_child[position[0]][position[1]] < 0:
                unsat_clause_list_child.pop(position[0])
            else:
                unsat_clause_list_child[position[0]].pop(position[1])
                if len(unsat_clause_list_child[position[0]]) == 0:
                    return None

            var_position_child = Variable.where_is_the_variable(unsat_clause_list_child, var_num)

    already_assigned_variables_child = copy.deepcopy(already_assigned_variables)
    already_assigned_variables_child.append((var_num, truth_assignement))

    child = State(var_num, truth_assignement, already_assigned_variables_child, unsat_clause_list_child)
    return child


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
                    var_num = state.variable.variable_number+1
                    if var_num > nbr_variable:
                        return None
                else:
                    var_num = 1
                child1 = create_child_state(var_num, state.already_assigned_variables, state.unsat_clause_list, True)
                child2 = create_child_state(var_num, state.already_assigned_variables, state.unsat_clause_list, False)
                if child1 is not None:
                    if len(child1.unsat_clause_list) == 0:
                        return child1
                    state_queue.put(child1)
                if child2 is not None:
                    if len(child2.unsat_clause_list) == 0:
                        return child2
                    state_queue.put(child2)

def depth_search(clause_list_, nbr_variable):
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
                    var_num = state.variable.variable_number+1
                    if var_num > nbr_variable:
                        return None
                else:
                    var_num = 1
                child1 = create_child_state(var_num, state.already_assigned_variables, state.unsat_clause_list, True)
                child2 = create_child_state(var_num, state.already_assigned_variables, state.unsat_clause_list, False)
                if child1 is not None:
                    if len(child1.unsat_clause_list) == 0:
                        return child1
                    state_queue.put(child1)
                if child2 is not None:
                    if len(child2.unsat_clause_list) == 0:
                        return child2
                    state_queue.put(child2)


cnf_file = File("uf20-01.cnf")
clause_list = cnf_file.get_clause_info
print clause_list
print Variable.where_is_the_variable(clause_list, 1)
etat = depth_search(clause_list, cnf_file.get_file_info['nbr_variable'])
print etat.already_assigned_variables