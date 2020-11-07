"""
    Вывести из кода ниже с помощью функции getcomments() комментарий 'output this comment'
"""

import inspect
from io import StringIO
import tokenize

# This comment appears first
# and spans 2 lines.

# This comment does not show up in the output of getcomments().

"""Sample file to serve as the basis for inspect examples.
"""


def module_level_function(arg1, arg2='default', *args, **kwargs):
    """This function is declared in the module."""
    local_variable = arg1 * 2
    return local_variable


class A(object):
    """The A class."""

    def __init__(self, name):
        self.name = name

    def get_name(self):
        "Returns the name of the instance."
        return self.name


instance_of_a = A('sample_instance')


class B(A):
    """This is the B class.
    It is derived from A.
    """

    # This method is not part of A.
    def do_something(self):
        """Does some work"""

    # output this comment
    def get_name(self):
        "Overrides version from A"
        return 'B(' + self.name + ')'


# По каким-то причинам inspect.getcomments(B) у меня выдавал None

buf = StringIO(inspect.getsource(B))

for line in tokenize.generate_tokens(buf.readline):
    if line.type == tokenize.COMMENT:
        print(line.line)