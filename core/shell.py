from builtins import Builtins
from plugin import Plugin, UnknownCommandError

import string

class Shell:

  def __init__(self):
    self.directory = '~'
    self.log = ''
    self.builtins = Builtins(self)
    self.javascript = ''

  def execute(self, command):
    self.add_log(self.__prompt() + command)

    # no command
    if not command:
      return

    # execute builtins command
    try:
      self.builtins.execute(command)
    except UnknownCommandError, e:
      self.not_found(e.command)
    except Exception, e:
      print 'error in builtins : %s' % e

  def add_log(self, log=''):
    self.log += "%s<br/>\n" % log

  def not_found(self, command):
      self.add_log('websh: command not found: %s' % command)

  def __prompt(self):
    return '<span class="blue">%s</span> <span class="green">$</span> ' % self.directory

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

