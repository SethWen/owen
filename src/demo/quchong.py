"""
    author: Shawn
    time  : 7/21/18 5:25 PM
    desc  :
    update: Shawn 7/21/18 5:25 PM
"""


def xie_zheng(infile, outfile):
    infopen = open(infile, 'r', encoding='utf-8')
    outopen = open(outfile, 'w', encoding='utf-8')
    lines = infopen.readlines()
    list_l = []
    for line in lines:

        if line not in list_l:
            list_l.append(line)

            outopen.write(line)

    infopen.close()
    outopen.close()


if __name__ == '__main__':
    xie_zheng('old.txt', 'xie_zheng.txt')
