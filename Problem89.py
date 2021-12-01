"""
Roman numerals
"""

if __name__ == '__main__':
    f = open('pe089.txt')
    src = ''
    r = ''
    for line in f:
        src += line
        s = line.replace('DCCCC', 'CM')
        s = s.replace('CCCC', 'CD')
        s = s.replace('LXXXX', 'XC')
        s = s.replace('XXXX', 'XL')
        s = s.replace('VIIII', 'IX')
        s = s.replace('IIII', 'IV')
        r += s
    print(len(src) - len(r))