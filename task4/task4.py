import argparse


parser = argparse.ArgumentParser()
parser.add_argument('first_str', help='Первая строка', type=str)
parser.add_argument('second_str', help='Вторая строка', type=str)
args = parser.parse_args()


def compare_str(a, b):
    ans = True
    min_str = min(len(a), len(b)) - 1
    for i in range(min_str):
        if a[i] != b[i] and b[i] != "*":
            ans = False
    if b[-1] != '*' and len(a) > len(b):
        ans = False
    return ans


final_ans = compare_str(args.first_str, args.second_str)
if final_ans:
    print('OK')
else:
    print('KO')
