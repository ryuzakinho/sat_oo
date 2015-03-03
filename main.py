__author__ = 'ryuzakinho'
from file import File
from Variable import where_is_the_variable


f1 = File("uf20-01.cnf")

print(where_is_the_variable(f1.get_clause_info(), 4))


