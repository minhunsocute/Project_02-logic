import os
from const import OR
class HandleFile:
    def read_file(filename):
        file = open(filename, "r")
        
        firstLine = file.readline()

        no_clause = int(file.readline())
        KB = set({})

        for i in range(no_clause):
            clause = file.readline()
            KB.add(standardize(clause))
        file.close()
        return KB, standardize(firstLine)
    def write_file(filename):
        print(1)

def standardize(clause):
        return tuple((x.strip() for x in clause.split(OR)))
