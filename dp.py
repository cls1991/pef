# coding: utf8

"""
    dp removes all dependencies of an uninstalled package.
"""

import click


@click.command()
@click.argument('packages', nargs=-1)
def cli(packages):
    """Remove packages and theirs dependencies."""
    click.secho('dp: {0}'.format(' '.join(packages)))


if __name__ == '__main__':
    cli()
