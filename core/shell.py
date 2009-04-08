from builtins import Builtins

import string

class Shell:

  def __init__(self):
    # read template file
    file = open('data/template.html', 'r')
    self.template = string.Template(file.read())
    file.close()

    self.directory = '~'
    self.log = ''
    self.builtins = Builtins(self)

  def execute(self, command):
    self.addlog(self.__prompt() + command)
    try:
      self.builtins.execute(command)
    except:
      self.addlog('websh: command not found: %s' % command)

  def addlog(self, log=''):
    self.log += log + "<br/>\n"

  def __prompt(self):
    return '<span class="blue">' \
           + self.directory \
           + ' </span> ' \
           + '<span class="green">$</span> '

  def __str__(self):
    return self.template.substitute(prompt=self.__prompt(), log=self.log)
