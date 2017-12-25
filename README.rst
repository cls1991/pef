pef
===

.. image:: https://img.shields.io/pypi/l/pef.svg
    :target: https://pypi.python.org/pypi/pef

.. image:: https://img.shields.io/pypi/v/pef.svg
    :target: https://pypi.python.org/pypi/pef

.. image:: https://img.shields.io/pypi/pyversions/pef.svg
    :target: https://pypi.python.org/pypi/pef

Enhancement for pip uninstall command, that it removes all dependencies of an uninstalled package.

.. image:: https://asciinema.org/a/YlzQlq8TSaIs9NcVA9r9uN07L.png
    :target: https://asciinema.org/a/YlzQlq8TSaIs9NcVA9r9uN07L

☤ Quickstart
------------

Uninstall package, e.g, qu:

::

    $ pef qu -y

Uninstall multiple packages, e.g, qu, gy:

::

    $ pef qu gy -y

☤ Installation
--------------

You can install "pef" via pip from `PyPI <https://pypi.python.org/pypi/pef>`_:

::

    $ pip install pef
	
☤ Usage
-------

::

    $ pef --help
    Usage: pef [OPTIONS] [PACKAGES]...

      Uninstall packages with all its dependencies.

    Options:
      -y, --yes  Don't ask for confirmation of uninstall deletions.
      --help     Show this message and exit.
