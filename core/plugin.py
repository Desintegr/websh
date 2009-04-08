class Plugin:

  def __init__(self, shell):
    self.shell = shell

  def execute(self, command):
    eval('self.' + command + '()')
