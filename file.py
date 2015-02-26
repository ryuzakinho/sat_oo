__author__ = 'ryuzakinho'
from clause_variable_element import Clause
from clause_variable_element import Variable
import re


class File(object):
    """
    This class represents a cnf file whith the following attributes:
    opening_type : str
    filneame : str
    """
    __opening_type = 'r'

    def __init__(self, filename):
        """
        :param filename: str
        """
        self.__filename = filename

    @property
    def opening_type(self):
        """
        I'm the opening type argument
        :rtype : str
        """
        return self.__opening_type

    @opening_type.setter
    def opening_type(self, opening_type):
        """
        I'm setting the opening type
        :param opening_type: str
        """
        self.__opening_type = opening_type

    @property
    def filename(self):
        """
        I'm the filename argument
        :rtype: str
        """
        return self.__filename

    @filename.setter
    def filename(self, filename):
        """
        I'm setting the filename
        :param filename: str
        """
        self.__filename = filename

    def get_file_info(self):
        """
        gets filename and opening types to gather information about cnf.
        :rtype : dict
        """
        clause_length = None
        with open(self.filename, self.opening_type) as f_handler:
            for line in f_handler:
                line = line.lstrip()
                find = re.search("clause length\s*=\s*([0-9]+)", line)
                if find is not None:
                    clause_length = find.group(1)
                    continue
                find = re.search("\s*p cnf ([0-9]+)\s*([0-9]+)", line)
                if find is not None:
                    nbr_variable = find.group(1)
                    nbr_clause = find.group(2)
                    return {"nbr_clause": int(nbr_clause), "nbr_variable": int(nbr_variable),
                            "clause_length": int(clause_length)}

    def get_clause_info(self):
        """
        This method opens a cnf file and gathers data about clauses (clause number, variables).
        It returns a list of clauses.
        :rtype : list
        """
        list_clause = list()
        nbr_clause = (self.get_file_info())['nbr_clause']
        for clause_number in range(1, nbr_clause + 1):
            list_clause.append(Clause(clause_number))
        with open(self.filename, self.opening_type) as file_handler:
            clause_counter = 0
            for line in file_handler:
                line.lstrip()   # We get rid of blanks at the beginning of the line
                find = re.search("([-]?[0-9]+)\s*([-]?[0-9]+)\s*([-]?[0-9]+)\s*0", line)
                if find is not None:
                    clause_length = (self.get_file_info())['clause_length']
                    for i in range(1, clause_length + 1):
                        variable = find.group(i)
                        print variable
                        if int(variable) > 0:
                            (list_clause[clause_counter]).add_variable(Variable(int(variable)), 1)
                        else:
                            list_clause[clause_counter].add_variable(Variable(-1 * int(variable)), -1)
                    clause_counter += 1
            return list_clause

    @staticmethod
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
