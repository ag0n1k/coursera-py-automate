import click


def logic(x: list, twice=False):
    res = 0
    for i, v in enumerate(x, start=1):
        if v == 0:
            continue
        if i > 0 and i % 4 == 0:
            res = res / v
            if twice:
                res = res / v
        else:
            res += v
            if twice:
                res += v
    return int(res)


@click.command('main')
@click.option('-t', '--twice', is_flag=True, default=False,
              help="Twice the operation.")
@click.argument('numbers', type=float, nargs=-1)
def cl(numbers, twice):
    res = logic(x=numbers, twice=twice)
    click.echo(res)
    return res


def main():
    output = cl.main(standalone_mode=False)
    return output


if __name__ == '__main__':
    main()
