def read_file(file_name):
    clauses = []
    with open(file_name, 'r') as f:
        lines = f.readlines()

    for line in lines:
        clauses.append(line.split())

    no_var = clauses[0][0]

    for i in range(len(clauses)):
        clauses[i] = clauses[i][:-1]

    return clauses[1:], no_var


def main():
    clauses, no_var = read_file('sat2.txt')
    graph = {}
    for i in range(1, int(no_var) + 1):
        graph[i] = []
        graph[-i] = []
    for i, j in clauses:
        graph[-int(i)].append(int(j))
        graph[-int(j)].append(int(i))
    return


if __name__ == '__main__':
    main()
