from plugin import Plugin, UnknownCommandError

import cgi
import re

class Builtins(Plugin):

  def clear(self, *args):
    """clear the terminal screen"""

    self.shell.log.clear()

  def help(self, *args):
    """
    display help text

    command?
    """

    # keep only the first argument
    args = list(args)
    del args[1:]

    commands = []

    for attr in args or dir(self):
      try:
        if callable(eval('self.{0}'.format(attr))) \
           and not attr.startswith('__') \
           and not attr == 'execute':
           commands.append(attr)
      except AttributeError:
        raise UnknownCommandError(attr)

    if not args:
      self.shell.log.append('<span class="grey">help</span>')
    else:
      self.shell.log.append('<span class="grey">help: </span> <span class="blue">{0}</span>'.format(args[0]))

    self.shell.log.append()
    self.shell.log.append('<span class="grey">{0}{1}{2}</span>'.format(
                            'command'.ljust(15, ' ').replace(' ', '&nbsp;'),
                            'parameters'.ljust(15, ' ').replace(' ', '&nbsp;'),
                            'function'.ljust(15, ' ').replace(' ', '&nbsp;')))

    for command in commands:
      docstring = eval('self.{0}'.format(command)).__doc__

      if not docstring:
        function = 'not documented'
        parameters = ''
        details = ''
      else:
        docstring = docstring.strip().splitlines()

        try:
          function = docstring[0].strip()
        except IndexError:
          function = ''

        try:
          parameters = docstring[2].strip()
        except IndexError:
          parameters = ''

        try:
          details = docstring[3].strip()
        except IndexError:
          details = ''

      self.shell.log.append('{0}{1}{2}'.format(
                              command.ljust(15, ' ').replace(' ', '&nbsp;'),
                              cgi.escape(parameters.ljust(15, ' ')).replace(' ', '&nbsp;'),
                              cgi.escape(function.ljust(15, ' ')).replace(' ', '&nbsp;')))

      if args and details:
        self.shell.log.append()
        self.shell.log.append(details)

    self.shell.log.append()

  def ls(self, *args):
    """
    list commands

    command?
    this exists just for convenience. Use <span class="blue">help</span> for help.
    """

    # keep only the first argument
    args = list(args)
    del args[1:]

    commands = []

    try:
      for attr in args or dir(self):
        if callable(eval('self.{0}'.format(attr))) \
           and not attr.startswith('__') \
           and not attr == 'execute':
           commands.append(attr)
    except AttributeError:
      raise UnknownCommandError(attr)

    # pretty formatting: 5 words max per line
    ls = ''
    for i, command in enumerate(commands):
      ls += command.ljust(15, ' ').replace(' ', '&nbsp;')
      if (i + 1) % 5 == 0 and i != len(commands) - 1:
        ls += "<br/>\n"

    self.shell.log.append(ls)
    self.shell.log.append()

  def open(self, *args):
    """
    open urls in new windows

    url+
    """

    for arg in args:
      url = re.sub('^http://', '', arg)
      self.shell.javascript.append("window.open('http://{0}');".format(url))
