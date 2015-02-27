__author__ = 'ryuzakinho'


class Variable(object):
    """
    This class represents a logical variable used in the SAT problem
    it has the following attributes:
    variable_number : int
    variable_value : int
    clauses_containing_the_variable : array of clause numbers
    """

    def __init__(self, variable_number):
        """
        :param variable_number: int
        """
        self.__variable_number = variable_number
        self.__variable_value = -1
        self.clauses_containing_the_variable = list()

    @property
    def variable_number(self):
        """
        I'm the variable number.
        :rtype : int
        """
        return self.__variable_number

    @variable_number.setter
    def variable_number(self, variable_number):
        """
        I'm the variable number setter.
        :param : int
        """
        self.__variable_number = variable_number

    @property
    def variable_value(self):
        """
        I'm the variable value.
        :rtype : int
        """
        return self.__variable_value

    @variable_value.setter
    def variable_value(self, variable_value):
        """
        I'm the variable value setter.
        :param variable_value: int
        """
        self.__variable_value = variable_value


def where_is_the_variable(clause_list, variable_number):
    """
    This is a static method that returns a list containing information about a variable position
    in a clause list.
    The returned list consists of a tuple in like this (clause index, variable index
    in the clause variables list)
    :param clause_list:
    :param variable_number:
    :return:
    """
    """
    :param clause_list:
    :param variable_number:
    :return:
    """
    variable_position = list()
    clause_list_index = 0
    for clause in clause_list:
        clause_variables_index = 0
        for variable in clause.clause_variables:
            if variable[0].variable_number == variable_number:
                variable_position.append((clause_list_index, clause_variables_index))
            clause_variables_index += 1
        clause_list_index += 1
    return variable_position
