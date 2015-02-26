__author__ = 'ryuzakinho'


class Clause(object):
    """
    This class represents a clause of the SAT problem.
    it has the following attributes:
    clause_number : int
    clause_value : int
    clause_variables : array of variables (Variable class defined in this file.)
    """

    def __init__(self, clause_number):
        """
        :param clause_number: int
        """
        self.__clause_number = clause_number
        self.__clause_value = -1
        self.__clause_variables = list()

    @property
    def clause_number(self):
        """
        I'm the clause number.
        :rtype : int
        """
        return self.__clause_number

    @clause_number.setter
    def clause_number(self, clause_number):
        """
        I'm setting the clause number
        :param : int
        """
        self.__clause_number = clause_number

    @property
    def clause_value(self):
        """
        I'm the clause value
        :rtype : int
        """
        return self.__clause_value

    @clause_value.setter
    def clause_value(self, clause_value):
        """
        I'm setting the clause value
        :param : int
        """
        self.__clause_value = clause_value

    @property
    def clause_variables(self):
        """
        :return: clause variables
        """
        return self.__clause_variables

    def add_variable(self, variable, sign):
        self.__clause_variables.append((variable, sign))

    def del_variable(self, variable):
        counter = 0
        for var in self.__clause_variables:
            if var.variable_number == variable.variable_number:
                self.__clause_variables.pop(counter)
            counter += 1

#############################################################################
#############################################################################
#############################################################################
#############################################################################


class Variable(object):
    """
    This class represents a logical variable used in the SAT problem
    it has the following attributes:
    variable_number : int
    variable_value : int
    variable_sign : int
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


