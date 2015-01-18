"""
Lint factory.

Given an extension, will return a
registered Linter.
"""
from gerritlinter.linters.base_linter import NullLinter
from gerritlinter.linters.pylinter import Pylinter

class LinterException(Exception):
    pass

class LintFactory(object):
    PLUGINS = [Pylinter]

    @staticmethod
    def get_linter(ext):
        """
        Gets a Linter for the given extension.

        :param ext:
        :return:
        """
        for plugin in LintFactory.PLUGINS:
            if ext in plugin.EXTS:
                return plugin

        return NullLinter()

    @staticmethod
    def register_linter(linter):
        """
        Register a Linter class for file verification.

        :param linter:
        :return:
        """
        if hasattr(linter, "EXTS") and hasattr(linter, "run"):
            LintFactory.PLUGINS.append(linter)
        else:
            raise LinterException("Linter does not have 'run' method or EXTS variable!")