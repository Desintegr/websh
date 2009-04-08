from plugin import Plugin

class Builtins(Plugin):

  def clear(self):
    """clear the terminal screen"""
    self.shell.log = ''

  def help(self):
    """display help text"""
    commands = []

    for attr in dir(self):
      if callable(eval('self.' + attr)) \
         and not attr.startswith('__') \
         and not attr == 'execute':
         commands.append(attr)

    self.shell.addlog('<span class="grey">help</span>')
    self.shell.addlog()
    self.shell.addlog('<span class="grey">' \
                      + 'command'.ljust(15, ' ').replace(' ', '&nbsp;') \
                      + '</span>' \
                      + '<span class="grey">function</span>')

    for command in commands:
      doc = eval('self.' + command).__doc__
      if not doc:
        doc = 'not documented'
      self.shell.addlog(command.ljust(15, ' ').replace(' ', '&nbsp;') + doc)

    self.shell.addlog()

  def ls(self):
    """list commands"""
    commands = []

    for attr in dir(self):
      if callable(eval('self.' + attr)) \
         and not attr.startswith('__') \
         and not attr == 'execute':
         commands.append(attr)

    ls = ''
    for i, command in enumerate(commands):
      ls += command.ljust(15, ' ').replace(' ', '&nbsp;')
      if (i + 1) % 5 == 0 and i != len(commands) - 1:
        ls += "<br/>\n"

    self.shell.addlog(ls)
    self.shell.addlog()
