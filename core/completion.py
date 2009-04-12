import json
import re

class Completion:

  def __init__(self, shell):
    self.shell = shell

  def complete(self, comp):
    commands = []

    for attr in dir(self.shell.builtins):
      if callable(eval('self.shell.builtins.{0}'.format(attr))) \
         and not attr.startswith('__') \
         and not attr == 'execute' \
         and re.match(comp, attr):
         commands.append(attr)

    if len(commands) == 1:
      completion = commands[0]
    else:
      completion = ''
      for i, command in enumerate(commands):
        completion += command.ljust(15, ' ').replace(' ', '&nbsp;')
        if (i + 1) % 5 == 0 and i != len(commands) - 1:
          completion += "<br/>\n"

    return json.dumps({'count': len(commands),
                       'completion': completion})
