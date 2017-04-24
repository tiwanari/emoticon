# coding: utf-8

if __name__ == '__main__':
    data = []
    for line in open('emoticon.txt', 'r'):
        data += [line[:-1].split('\t')]

    data = sorted(data, key=lambda x: x[0])

    g = open('emoticon.txt', 'w')
    for row in data:
        g.write(row[0] + '\t' + row[1] + '\t' + row[2] + '\n')
