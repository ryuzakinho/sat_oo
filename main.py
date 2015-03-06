__author__ = 'ryuzakinho'
from file import File
from State import State
from Variable import Variable
import Queue
import copy


def create_child_state(var_num, already_assigned_variables, unsat_clause_list, truth_assignement):
    """

    :rtype : State
    """
    var_position_child = Variable.where_is_the_variable(unsat_clause_list, var_num)
    unsat_clause_list_child = copy.deepcopy(unsat_clause_list)

    if truth_assignement:
        while len(var_position_child) > 0:
            position = var_position_child[0]
            if unsat_clause_list_child[position[0]][position[1]] > 0:
                unsat_clause_list_child.pop(position[0])
            else:
                unsat_clause_list_child[position[0]].pop(position[1])

            var_position_child = Variable.where_is_the_variable(unsat_clause_list_child, var_num)
    else:
        while len(var_position_child) > 0:
            position = var_position_child[0]
            if unsat_clause_list_child[position[0]][position[1]] < 0:
                unsat_clause_list_child.pop(position[0])
            else:
                unsat_clause_list_child[position[0]].pop(position[1])

            var_position_child = Variable.where_is_the_variable(unsat_clause_list_child, var_num)

    already_assigned_variables_child = copy.deepcopy(already_assigned_variables)
    already_assigned_variables_child.append((var_num, truth_assignement))

    child = State(var_num, truth_assignement, already_assigned_variables_child, unsat_clause_list_child)
    return child


def breadth_search(clause_list_):
    state_queue = Queue.Queue(0)
    state = State(clause_list_)
    state_queue.put(state)
    var_num = 0
    # LOOP
    unsat_clause_list = state.unsat_clause_list
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
                else:
                    var_num = 1
                child1 = create_child_state(var_num, state.already_assigned_variables, state.unsat_clause_list, True)
                child2 = create_child_state(var_num, state.already_assigned_variables, state.unsat_clause_list, False)
                state_queue.put(child1)
                state_queue.put(child2)
                if len(child1.unsat_clause_list) == 0:
                    return child1
                elif len(child2.unsat_clause_list) == 0:
                    return child2


cnf_file = File("uf20-01.cnf")
clause_list = cnf_file.get_clause_info
print clause_list
print Variable.where_is_the_variable(clause_list, 1)
etat = breadth_search(clause_list)
print etat.already_assigned_variables