#
# Skeleton file for the Python "Hello World" exercise.
#


def hello(name=''):
    if name:
        return u"Hello, {}!".format(unicode(name))
    return u"Hello, World!"
