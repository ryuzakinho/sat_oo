__author__ = 'ryuzakinho'
from file import File
from Variable import where_is_

f1 = File("uf20-01.cnf")

print(Variable.where_is_the_variable(f1.get_clause_info(), 4))

test = None
print test
test = True
print test




