import re

class Plugin:

  def __init__(self, shell):
    self.shell = shell

  def execute(self, command):
    l = re.split('\s+', command)
    base = l[0]
    args = ', '.join("'%s'" % i for i in l[1:])
    eval('self.' + base + '(' + args + ')')
