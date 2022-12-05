import os
from const import OR
from clause import *
class HandleFile:
    def read_file(filename):
        file = open(filename, "r")
        alpha = file.readline()
        no_clause = int(file.readline())
        KB = set({})
        for i in range(no_clause):
            clause = file.readline()
            KB.add(standardize(clause))
        file.close()
        return KB, standardize(alpha)

    def write_file(filename, clauses:Clause): 
        file = open(filename, 'w') 
        for item1 in clauses.clauses:
            file.write(str(len(item1)) + '\n')
            for item2 in item1:
                write_set(file, item2)
                file.write('\n')
        if clauses.result:
            file.write("YES")
        else:
            file.write("NO")

        file.close()

   
def write_set(file, set):
    if len(set) == 0:
        file.write('{}')
        return
    for i in range(len(set)):
        # file.write(str(item))
        if i < len(set)-1:
            file.write(str(set[i]) + ' OR ')
        else:
            file.write(str(set[i]))

def standardize(clause):
    return tuple((x.strip() for x in clause.split(OR)))

