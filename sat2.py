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

    ssc_map = kosaraju(graph)

    for i in range(1, int(no_var) + 1):
        if ssc_map[i] == ssc_map[-i]:
            print('UNSATISFIABLE')
            return False
    print('SATISFIABLE')
    return True


def kosaraju(graph):
    ssc_map = {}
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
            for j in ssc:
                ssc_map[j] = i

    return ssc_map


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


if __name__ == '__main__':
    main()
