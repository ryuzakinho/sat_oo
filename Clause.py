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
        done = False
        clause_length = len(self.__clause_variables)
        while (done is False) and (counter < clause_length):
            if self.__clause_variables[counter] == variable.variable_number:
                self.__clause_variables.pop(counter)
                done = True
            counter += 1




