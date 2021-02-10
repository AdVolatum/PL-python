import argparse


def validate(value):
    if len(value) in range(2, 37):
        return value
    else:
        raise argparse.ArgumentTypeError('Введены некорректные данные')


parser = argparse.ArgumentParser()
parser.add_argument('nb', help='Число', type=str)
parser.add_argument('base_src', help='Исходная СС', type=validate)
parser.add_argument('base_dst', help='Конечная СС', type=validate)
args = parser.parse_args()


def convert(a, b, c):
    b = len(str(b))
    c = len(str(c))
    ten = 0
    x = []
    ans = []
    alp = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for i in range(len(a)):
        if a[i] not in alp[:b]:
            return 'Указанное число не входит в исходную СС'
        else:
            continue
    for k in range(len(a)):
        for j in range(len(alp)):
            if a[k] == alp[j]:
                x.append(j)
    elm = list(reversed(range(len(x))))
    for k in range(len(x)):
        ten += x[k] * b ** elm[k]
    while ten // c >= ten % c:
        el = ten % c
        ten //= c
        ans.append(alp[el])
    if ten % c == 0:
        return reversed(ans)
    else:
        ost2 = ten % c
        ans.append(alp[ost2])
        if ten // c != 0:
            ost3 = ten // c
            ans.append(alp[ost3])
        return reversed(ans)


print(*convert(args.nb, args.base_src, args.base_dst), sep='')
