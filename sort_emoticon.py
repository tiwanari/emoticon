# coding: utf-8

if __name__ == '__main__':
    filename = 'source.txt'
    data = []

    with open(filename, 'r') as f:
        for line in f:
            data += [line[:-1].split('\t')]

    data = sorted(data, key=lambda x: x[0])

    with open(filename, 'w') as f:
        for row in data:
            f.write(row[0] + '\t' + row[1] + '\t' + row[2] + '\n')
