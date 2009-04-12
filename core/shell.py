from builtins import Builtins
from completion import Completion
from history import History
from plugin import Plugin, UnknownCommandError

import string

class Shell:

  def __init__(self):
    self.directory = '~'
    self.log = ''
    self.javascript = ''

    self.builtins = Builtins(self)

    self.history = History()
    self.completion = Completion(self)

  def execute(self, command):
    self.add_log(self.__prompt() + command)
    self.history.append(command)

    # no command
    if not command:
      return

    # execute builtins command
    try:
      self.builtins.execute(command)
    except UnknownCommandError, e:
      self.not_found(e.command)
    except Exception, e:
      print 'error in builtins : {0}'.format(e)

  def add_log(self, log=''):
    self.log += "{0}<br/>\n".format(log)

  def not_found(self, command):
      self.add_log('websh: command not found: {0}'.format(command))

  def __prompt(self):
    return '<span class="blue">{0}</span> <span class="green">$</span> '.format(self.directory)

  def __javascript(self):
    javascript = self.javascript
    self.javascript = ''
    return javascript

  def __str__(self):
    # read template file
    file = open('data/template.html', 'r')
    template = string.Template(file.read())
    file.close()

    return template.substitute(prompt=self.__prompt(),
                               log=self.log,
                               javascript=self.__javascript())

