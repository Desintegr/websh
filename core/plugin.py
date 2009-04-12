import re

class UnknownCommandError(Exception):

  def __init__(self, command):
    self.command = command


class Plugin:

  def __init__(self, shell):
    self.shell = shell

  def execute(self, command):
    l = re.split('\s+', command)
    base = l[0]

    if base not in dir(self):
      raise UnknownCommandError(base)

    args = ', '.join("'{0}'".format(i) for i in l[1:])
    eval('self.{0}({1})'.format(base, args))
