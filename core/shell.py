from builtins import Builtins
from completion import Completion
from history import History
from javascript import Javascript
from log import Log
from plugin import Plugin, UnknownCommandError
from prompt import Prompt

import json
import string

class Shell:

  def __init__(self):
    self.builtins = Builtins(self)
    self.completion = Completion(self)
    self.history = History()
    self.javascript = Javascript()
    self.log = Log()
    self.prompt = Prompt()

  def execute(self, command):
    self.log.append(str(self.prompt) + command)
    self.history.append(command)

    if command:
      # execute builtins command
      try:
        self.builtins.execute(command)
      except UnknownCommandError as e:
        self.log.append('websh: command not found: {0}'.format(e.command))
      except Exception as e:
        print 'Error in builtins: {0}'.format(e)

    return json.dumps({'javascript': str(self.javascript),
                       'log': str(self.log),
                       'prompt': str(self.prompt)})

  def template(self):
    # read template file
    file = open('data/template.html', 'r')
    template = string.Template(file.read())
    file.close()

    return template.substitute(log = str(self.log),
                               prompt = str(self.prompt))
