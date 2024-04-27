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
    ssc_map = tarjan(graph)
    for i in range(1, int(no_var) + 1):
        if ssc_map[i] == ssc_map[-i]:
            print('UNSATISFIABLE')
            return False
    print('SATISFIABLE')
    return True


def tarjan(graph):
    index = 1
    stack = []
    ssc_map = {}
    low_link = {}
    index_map = {}
    for key in graph.keys():
        ssc_map[key] = 0
        low_link[key] = 0
        index_map[key] = 0

    for key in graph.keys():
        if index_map[key] == 0:
            index = strong_connect(graph, key, index, stack, ssc_map, low_link, index_map)
    return ssc_map


def strong_connect(graph, key, index, stack, ssc_map, low_link, index_map):
    index_map[key] = index
    low_link[key] = index
    index += 1
    stack.append(key)

    for neighbor in graph[key]:
        if index_map[neighbor] == 0:
            index = strong_connect(graph, neighbor, index, stack, ssc_map, low_link, index_map)
            low_link[key] = min(low_link[key], low_link[neighbor])
        elif ssc_map[neighbor] == 0:
            low_link[key] = min(low_link[key], index_map[neighbor])

    if low_link[key] == index_map[key]:
        while True:
            node = stack.pop()
            ssc_map[node] = low_link[key]
            if node == key:
                break
    return index


if __name__ == '__main__':
    main()
