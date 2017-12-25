# coding: utf8

"""
    pef uninstall pip-installed package with all its dependencies.
"""

import sys

import click
import pip

_ver = sys.version_info

# Python 2.x?
is_py2 = (_ver[0] == 2)

# Python 3.x?
is_py3 = (_ver[0] == 3)


def _encode(u):
    """
    :param u:
    :return:
    """
    if is_py2 and isinstance(u, unicode):
        return u.encode('utf8')

    return u


class DistInfo(object):
    # @TODO: to be expanded
    SKIP_MODULES = ['wheel', 'setuptools', 'pip']

    def __init__(self, dist):
        self.keys = list()
        self.requires = dict()
        self.references = dict()
        for d in dist:
            if d.key not in self.SKIP_MODULES:
                self.keys.append(d.key)
                if d.key not in self.requires:
                    self.requires[d.key] = list()
                for r in d.requires():
                    self.requires[d.key].append(r.key)
                    if r.key not in self.references:
                        self.references[r.key] = 0
                    self.references[r.key] += 1

    def __repr__(self):
        return 'keys:{0}\nrequires:{1}\nreferences:{2}'.format(self.keys, self.requires, self.references)

    def dfs(self, root, vis=list()):
        """
        :param root:
        :param vis:
        :return:
        """
        tree = list()
        tree.append(root)
        if not vis:
            vis.append(root)
        for r in self.requires.get(root, list()):
            if r not in vis:
                vis.append(r)
                tree.extend(self.dfs(r, vis))

        return tree


@click.command()
@click.argument('packages', nargs=-1)
def cli(packages):
    """Uninstall packages with all its dependencies."""
    pkg = pip.get_installed_distributions()
    di = DistInfo(pkg)
    for p in packages:
        tree = di.dfs(_encode(p))
        print(tree)


if __name__ == '__main__':
    cli()
