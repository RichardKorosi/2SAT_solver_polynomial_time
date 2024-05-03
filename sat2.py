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

    for clause in clauses:
        if len(clause) == 2:
            i, j = clause
            graph[-int(i)].append(int(j))
            graph[-int(j)].append(int(i))
        elif len(clause) == 1:
            i = clause[0]
            graph[-int(i)].append(int(i))

    sccs = kosaraju(graph)
    print("Clauses:", clauses)
    print("Graph:", graph)
    print('SSCs:', sccs)

    for scc in sccs:
        for element in scc:
            if -element in scc:
                print('NESPLNITELNA')
                return False
    print('SPLNITELNA')

    generate_values(sccs, int(no_var))
    return True


def kosaraju(graph):
    scc_list = []
    visited = {}
    stack = []

    for i in graph.keys():
        visited[i] = False

    for i in graph.keys():
        if not visited[i]:
            dfs(graph, i, visited, stack)

    reversed_graph = reverse_graph(graph)

    for i in graph.keys():
        visited[i] = False

    while stack:
        i = stack.pop()
        if not visited[i]:
            ssc = []
            dfs(reversed_graph, i, visited, ssc)
            scc_list.append(ssc)

    return scc_list


def dfs(graph, i, visited, stack):
    visited[i] = True
    for j in graph[i]:
        if not visited[j]:
            dfs(graph, j, visited, stack)
    stack.append(i)


def reverse_graph(graph):
    reversed_graph = {}
    for i in graph.keys():
        reversed_graph[i] = []

    for i in graph.keys():
        for j in graph[i]:
            reversed_graph[j].append(i)

    return reversed_graph


def generate_values(sccs, no_var):
    values = {}
    for i in range(1, no_var + 1):
        values[i] = None

    for scc in reversed(sccs):
        for element in scc:
            if values[abs(element)] is None:
                values[abs(element)] = True if element > 0 else False

    for i in values.keys():
        print('Value' + str(i) + ':', "PRAVDA" if values[i] else "NEPRAVDA")
    return True


if __name__ == '__main__':
    main()
