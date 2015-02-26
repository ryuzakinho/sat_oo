__author__ = 'ryuzakinho'
from clause_variable_element import Clause
from clause_variable_element import Variable
from file import File


f1 = File("uf20-01.cnf")
clause = f1.where_is_the_variable(f1.get_clause_info(), 2)
print clause

print "fdsf"


