__author__ = 'ryuzakinho'
import copy


class State(object):
    """
    This class is a state. It contains all the elements of tree's state.
    """
    def __init__(self, variable, truth_assignement, already_assigned_variables):
        """
        This constructor is used starting from the second level of the search tre.
        :param variable:
        :param truth_assignement:
        :param already_assigned_variables:
        """
        self.variable = variable
        self.variable.variable_value = truth_assignement
        self.already_assigned_variables =already_assigned_variables

    def __init__(self, variable, truth_assignement):
        """
        This constructor is used when we first instantiate a state.
        We create the already_assigned_variables list for the first time
        :param variable:
        :param truth_assignement:
        """
        self.variable = variable
        self.variable.variable_value = truth_assignement
        self.already_assigned_variables = list()