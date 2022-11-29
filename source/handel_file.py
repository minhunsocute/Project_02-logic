import os

def read_file(filename):
    file = open(filename, "r")
    
    firstLine = file.readline()

    no_clause = int(file.readline())
    KB = set({})
    
    for i in range(no_clause):
        clause = file.readline()
        print(clause)
    file.close()


def write_file(filename):
    print(1)


def pl_resolution(KB, alpha, output_path):
    clauses = set({})
    no = 0 #
    clauses.upate(KB) #add KB to clauses 

    print(1)

def read_write_folder():
    # path to SRC folder
    dir_path = os.path.dirname(os.path.realpath(__file__))
    # path to /SRC/input folder
    input_folder = os.path.join(dir_path, "input")
    # path to /SRC/output folder
    output_folder = os.path.join(dir_path, "output")

    for file in os.listdir(input_folder):
        # path to input path
        input_path = os.path.join(input_folder, file)
        # path to output path, respectively
        output_path = os.path.join(output_folder, 'output' + input_path[-5] + '.txt')
        read_file(input_path)

if __name__ == "__main__":
    read_write_folder()