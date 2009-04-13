import re

class Plugin:

  class UnknownCommandError(Exception):

    def __init__(self, command):
      self.command = command


  def __init__(self, shell):
    self.shell = shell

  def commands(self):
    return [attr for attr in dir(self) if \
              callable(eval('self.{0}'.format(attr))) \
              and not re.match('^(_|[A-Z])|execute|command', attr)]

  def execute(self, command):
    l = re.split('\s+', command)
    base = l[0]

    if base not in self.commands():
      raise self.UnknownCommandError(base)

    args = ', '.join("'{0}'".format(i) for i in l[1:])
    eval('self.{0}({1})'.format(base, args))
