from builtins import Builtins

import string

class Shell:

  def __init__(self):
    self.directory = '~'
    self.log = ''
    self.builtins = Builtins(self)
    self.javascript = 'focusOnInput();'

  def execute(self, command):
    self.add_log(self.__prompt() + command)

    # no command
    if not command:
      return

    # execute builtins command
    try:
      self.builtins.execute(command)
    except AttributeError:
      self.not_found(command)
    #except Exception, e:
    #  print 'error in builtins : %s' % e

  def add_log(self, log=''):
    self.log += log + "<br/>\n"

  def not_found(self, command):
      self.add_log('websh: command not found: %s' % command)

  def __prompt(self):
    return '<span class="blue">' \
           + self.directory \
           + ' </span> ' \
           + '<span class="green">$</span> '

  def __str__(self):
    # read template file
    file = open('data/template.html', 'r')
    template = string.Template(file.read())
    file.close()

    return template.substitute(prompt=self.__prompt(),
                               log=self.log,
                               javascript=self.javascript)

