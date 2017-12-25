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
        self.requires = {}
        self.references = {}
        self.keys = [d.key for d in dist if d.key not in self.SKIP_MODULES]
        for d in dist:
            if d.key not in self.SKIP_MODULES:
                if d.key not in self.requires:
                    self.requires[d.key] = []
                for r in d.requires():
                    if r.key in self.keys:
                        self.requires[d.key].append(r.key)
                    if r.key not in self.references:
                        self.references[r.key] = 0
                    self.references[r.key] += 1

        self.rm = []
        self.kp = []

    def __repr__(self):
        return 'keys:{0}\nrequires:{1}\nreferences:{2}'.format(self.keys, self.requires, self.references)

    def purge(self, node):
        """
        :param node:
        :return:
        """
        rc = self.references.get(node)
        if rc:
            rc = 0 if rc < 0 else rc - 1
            self.references[node] = rc
            if rc > 0:
                if node not in self.kp:
                    self.kp.append(node)
                return
        for r in self.requires.get(node, []):
            self.purge(r)
        if not rc and node not in self.SKIP_MODULES:
            if node not in self.rm:
                self.rm.append(node)
            if node in self.keys:
                self.keys.remove(node)
            if self.requires.get(node):
                self.requires[node] = []
            if node in self.kp:
                self.kp.remove(node)


@click.command()
@click.argument('packages', nargs=-1)
@click.option('-y', '--yes', is_flag=True, help="Don't ask for confirmation of uninstall deletions.")
def cli(packages, yes):
    """Uninstall packages with all its dependencies."""
    if not hasattr(sys, "base_prefix"):
        click.secho(
            click.style("Warning! You are not in an active virtual environment. This may purge system-level packages!",
                        fg='red'))
        sys.exit(1)
    if not packages:
        click.secho(click.style("Packages can't be empty, please run `pef --help` for more details.", fg='yellow'))
        sys.exit(0)
    prune = []
    pkg = pip.get_installed_distributions()
    df = DistInfo(pkg)
    for p in packages:
        if p not in df.keys:
            click.secho(click.style('Cannot uninstall requirement {0}, not installed.'.format(p), fg='yellow'))
            continue
        df.purge(_encode(p))
        prune.extend(df.rm)

    if df.kp:
        click.secho(click.style(
            'Module {0} is referenced by more than one other modules, to remain unchanged.'.format(', '.join(df.kp)),
            fg='yellow'))
    if prune:
        cmd = ['uninstall']
        if yes:
            cmd.append('-y')
        cmd.extend(list(set(prune)))
        pip.main(cmd)


if __name__ == '__main__':
    cli()
