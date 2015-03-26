from Searches import depth_search, breadth_search, first_heuristic_search
from Variable import *

__author__ = 'ryuzakinho'
from File import File


cnf_file = File("uf50-04.cnf")
clause_list = cnf_file.get_clause_info
print cnf_file.get_file_info
print clause_list
print Variable.where_is_the_variable(clause_list, 1)
#etat = depth_search(clause_list, cnf_file.get_file_info['nbr_variable'])
#print etat.already_assigned_variables

#etat = breadth_search(clause_list, cnf_file.get_file_info['nbr_variable'])
#print etat.already_assigned_variables

etat = first_heuristic_search(clause_list, cnf_file.get_file_info['nbr_variable'])
print etat.already_assigned_variables