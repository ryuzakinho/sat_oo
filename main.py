from Searches import depth_search, breadth_search, a_star
from Variable import *

__author__ = 'ryuzakinho'
from File import File


cnf_file = File("uf20-0348.cnf")
clause_list = cnf_file.get_clause_info
print cnf_file.get_file_info
print clause_list
print Variable.where_is_the_variable(clause_list, 1)
tup = depth_search(clause_list, cnf_file.get_file_info['nbr_variable'])
print tup[0].already_assigned_variables
print tup[1]
print tup[2]
print tup[3]


tup = breadth_search(clause_list, cnf_file.get_file_info['nbr_variable'])
print tup[0].already_assigned_variables
print tup[1]
print tup[2]
print tup[3]

tup = a_star(clause_list, cnf_file.get_file_info['nbr_variable'], 1)
print tup[0].already_assigned_variables
print tup[1]
print tup[2]
print tup[3]

etat = a_star(clause_list, cnf_file.get_file_info['nbr_variable'], 2)
print tup[0].already_assigned_variables
print tup[1]
print tup[2]
print tup[3]

tup = a_star(clause_list, cnf_file.get_file_info['nbr_variable'], 3)
print tup[0].already_assigned_variables
print tup[1]
print tup[2]
print tup[3]