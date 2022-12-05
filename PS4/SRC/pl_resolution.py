import os
from const import OR
from handel_file import *
from clause import *

def pl_resolution(KB, alpha, fileName):
    clauses = set({})
    clauses.update(KB) #add KB to clauses    
    out_clause = Clause(alpha, list(list({})),False)

    for i in alpha:
        clauses.add((set_negative_literal(i), )) # add alpha to clauses
    while True:
        temp_clauses  = set({})
        list_clause = list(clauses)
        for i in range(len(clauses)):
            for j in range(i+1, len(clauses)):
                checkClause , temp = check_two_clause(list_clause[i], list_clause[j])
                if checkClause and  (temp not in clauses):
                    temp_clauses.add(temp) 
                    # print(str(list_clause[i]) + ' + ' + str(list_clause[j]) + '\n')

        if len(temp_clauses)  == 0:
            out_clause.clauses.append([])
            break
        ltemp = []  
        for item in temp_clauses:
            if item == ():
                out_clause.result = True   
                ltemp.append({})   
            else :
                ltemp.append(item) 
 
        out_clause.clauses.append(ltemp)
        if out_clause.result:
            break
        clauses.update(temp_clauses)
    HandleFile.write_file(fileName,out_clause)
    # print("------------------------------")

def check_two_clause(clause1, clause2): 
    check_type = 0
    check1 = ''
    check2 = ''
    for i in range(len(clause1)):
        for j in range(len(clause2)):
            if check_des_litral(clause1[i], clause2[j]):
                check1 = clause1[i]
                check2 = clause2[j]
                check_type += 1
                if check_type > 1:
                    return (False, None)
                break
    if check_type == 0:
        return [False, None]
    if check_type ==  1 :
        if len(clause1) == 1 and len(clause2) == 1:
            return (True, ())
        else :
            result_check = set({})
            for item in clause1:
                if item != check1:
                    result_check.add(item)
            for item in clause2:
                if item !=  check2: 
                    result_check.add(item)
            return (True, tuple(sort_result(list(result_check))))
    return (False, None)

def sort_result(result_check):
    for i in range(len(result_check)):
        for j in range(i+1, len(result_check)):
            if set_abs_literal(result_check[i]) > set_abs_literal(result_check[j]):
                temp =  result_check[i]
                result_check[i] = result_check[j]
                result_check[j] = temp
    return result_check



def set_abs_literal(lit):
    return lit[1] if lit[0] == '-' else lit


def set_negative_literal(literal):
    return literal[1:] if literal[0] == '-' else '-' + literal

def check_des_litral(clause1, clause2):
    if clause1 ==  set_negative_literal(clause2):
        return True
    return False

def solve():
    absolutePath = os.path.abspath(os.path.dirname(__file__))
    input = os.path.join(absolutePath, "INPUT")
    output = os.path.join(absolutePath, "OUTPUT")
    
    for file in os.listdir(input):
        input_path = os.path.join(input, file)
        file_output_name = os.path.join(output, 'OUTPUT' + input_path[-5] + '.txt')
        KB , alpha = HandleFile.read_file(input_path)
        pl_resolution(KB, alpha,file_output_name)