from utitities import Utilities

import json
import re

class Completion:

  def __init__(self, shell):
    self.shell = shell

  def complete(self, comp):
    commands = [c for c in self.shell.builtins.commands() if re.match(comp, c)]

    length = len(commands)
    if length == 1:
      completion = commands[0]
    else:
      completion = Utilities.format(commands)

    return json.dumps({'count': length,
                       'completion': completion})
