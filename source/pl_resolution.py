import os
from const import OR
from handel_file import *

def pl_resolution(KB, alpha):
    clauses = set({})
    no = 0 #
    clauses.update(KB) #add KB to clauses    
    for i in alpha:
        clauses.add((set_negative(i), ))
    while True:
        no += 1
        temp_clause  = set({})
        list_clause = list(clauses)
        for i in range(len(clauses)):
            for j in range(i+1, len(clauses)):
                checkClause , listClause = check_clause(list_clause[i], list_clause[j])
                if checkClause and listClause not in clauses:
                    temp_clause.add(listClause) 
        check = False
        if len(temp_clause) == 0:
            print('NO\n')
            return False    
        else:
            print(len(temp_clause))
            for item in temp_clause:
                if item is ():
                    print("{}")
                else:
                    print(item)
                print('\n')
            # return True 
        clauses.update(temp_clause)
    print(1)

def sort_key(item):
    return item[-1]

def check_clause(clause1, clause2): 
    check_type = 0
    check1 = ''
    check2 = ''
    for i in range(len(clause1)):
        for j in range(len(clause2)):
            if clause1[i] == set_negative(clause2[j]):
                check1 = clause1[i]
                check2 = clause2[j]
                check_type += 1
                if check_type > 1:
                    return [False, None]
                break
    if check_type == 0:
        return [False, None]
    if check_type ==  1 :
        if len(clause1) == 1 and len(clause2) == 1:
            return [True, ()]
        else :
            result_check = set({})
            for item in clause1:
                if item != check1:
                    result_check.add(item)
            for item in clause2:
                if item !=  check2:
                    result_check.add(item)
            return [True, tuple(sorted(list(result_check), key = sort_key))]
    return [False, None]

def set_negative(literal):
    return literal[1:] if literal[0] == '-' else '-' + literal


def solve():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    input_folder = os.path.join(dir_path, "input")
    output_folder = os.path.join(dir_path, "output")


    for file in os.listdir(input_folder):
        # path to input path
        input_path = os.path.join(input_folder, file)
        # path to output path, respectively
        # output_path = os.path.join(output_folder, 'output' + input_path[-5] + '.txt')
        KB , alpha = HandleFile.read_file(input_path)
        pl_resolution(KB, alpha)