from plugin import Plugin
from utitities import Utilities

import re

class Builtins(Plugin):

  def clear(self, *args):
    """clear the terminal screen"""

    self.shell.log.clear()

  def help(self, *args):
    """
    display help text

    (command)?
    """

    commands = self.commands()

    if args:
      if args[0] not in commands:
        raise self.UnknownCommandError(args[0])
      commands = args[:1]
      self.shell.log.append('<span class="grey">help: </span> <span class="blue">{0}</span>'.format(args[0]))
    else:
      self.shell.log.append('<span class="grey">help</span>')

    self.shell.log.append()
    self.shell.log.append('<span class="grey">{0}</span>'.format(
                            Utilities.tab(('command', 'parameters', 'functions'))))

    for command in commands:
      # doc[0]: function
      # doc[1]: empty
      # doc[2]: parameters
      # doc[3]: details
      doc = ['not documented', '', '', '']

      docstring = eval('self.{0}'.format(command)).__doc__
      if docstring:
        for i, d in enumerate(d.strip() for d in docstring.strip().splitlines()):
          doc[i] = d

      self.shell.log.append(Utilities.tab((command, doc[2], doc[0])))

      if args and doc[3]:
        self.shell.log.append()
        self.shell.log.append(doc[3])

    self.shell.log.append()

  def ls(self, *args):
    """
    list commands

    (command)?
    this exists just for convenience. Use <span class="blue">help</span> for help.
    """

    commands = self.commands()

    if args:
      if args[0] not in commands:
        raise self.UnknownCommandError(args[0])
      commands = args[:1]

    self.shell.log.append(Utilities.format(commands))
    self.shell.log.append()

  def open(self, *args):
    """
    open urls in new windows

    (url)+
    """

    for arg in args:
      url = re.sub('^http://', '', arg)
      self.shell.javascript.append("window.open('http://{0}');".format(url))
