import argparse


def logic(x: list, twice=False):
    res = 0
    for i, v in enumerate(x, start=1):
        if v == 0:
            continue
        if i > 0 and i % 4 == 0:
            res = res // v
            if twice:
                res = res // v
        else:
            res += v
            if twice:
                res += v
    return int(res)


def main():
    parser = argparse.ArgumentParser(description='Sum and divide')
    parser.add_argument('numbers', type=float, nargs='*', help='The data []')
    parser.add_argument('-t', '--twice', action='store_const', dest='twice', default=False, const=True,
                        help='Twice the operation')
    ns = parser.parse_args()
    return logic(ns.numbers, ns.twice)


if __name__ == '__main__':
    main()
