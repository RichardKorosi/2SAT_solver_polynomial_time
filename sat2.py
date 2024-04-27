def read_file(file_name):
    clausules = []
    no_lit = 0
    with open(file_name, 'r') as f:
        lines = f.readlines()

    for line in lines:
        clausules.append(line.split())


    no_lit = clausules[0][0]

    for i in range(len(clausules)):
        clausules[i] = clausules[i][:-1]

    return clausules[1:], no_lit



def main():
    clausles, no_lit = read_file('sat2.txt')
    print(clausles, no_lit)


if __name__ == '__main__':
    main()