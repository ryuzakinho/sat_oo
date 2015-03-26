__author__ = 'ryuzakinho'
from Variable import Variable
import copy


class State(object):
    """
    This class is a state. It contains all the elements of tree's state.
    """

    def __init__(self, *args):
        """
        This constructor is used starting from the second level of the search tre.
        :param variable:
        :param truth_assignement:
        :param already_assigned_variables:
        """
        if len(args) == 4:
            self.variable = Variable(args[0])
            self.variable.variable_value = args[1]
            self.already_assigned_variables = args[2]
            self.unsat_clause_list = copy.deepcopy(args[3])
        elif len(args) == 1:
            self.variable = None
            self.already_assigned_variables = list()
            self.unsat_clause_list = copy.deepcopy(args[0])
        else:
            print "Wrong number of arguments"


    @staticmethod
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

        for i in range(0, len(unsat_clause_list_child)):
            if len(unsat_clause_list_child[i]) == 1:
                for j in range(i + 1, len(unsat_clause_list_child)):
                    if (len(unsat_clause_list_child[j]) == 1) and (
                                unsat_clause_list_child[j] == -1 * unsat_clause_list_child[i]):
                        return None

        already_assigned_variables_child = copy.deepcopy(already_assigned_variables)
        already_assigned_variables_child.append((var_num, truth_assignement))

        child = State(var_num, truth_assignement, already_assigned_variables_child, unsat_clause_list_child)
        return child


class StateHeuristic(State):
    g = None
    h = None

    @staticmethod
    def create_child_state_heuristic(var_num, already_assigned_variables, unsat_clause_list, truth_assignement):
        """
        Generates the child states to be put in the queue.
        :rtype : StateHeuristic
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

        for i in range(0, len(unsat_clause_list_child)):
            if len(unsat_clause_list_child[i]) == 1:
                for j in range(i + 1, len(unsat_clause_list_child)):
                    if (len(unsat_clause_list_child[j]) == 1) and (
                                unsat_clause_list_child[j] == -1 * unsat_clause_list_child[i]):
                        return None

        already_assigned_variables_child = copy.deepcopy(already_assigned_variables)
        already_assigned_variables_child.append((var_num, truth_assignement))

        child = StateHeuristic(var_num, truth_assignement, already_assigned_variables_child, unsat_clause_list_child)
        child.g = len(already_assigned_variables_child)
        child.h = len(unsat_clause_list_child)
        return child
