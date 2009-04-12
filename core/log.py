class Log:

  def __init__(self):
    self.log = ''

  def append(self, command = ''):
    self.log += "{0}<br/>\n".format(command)

  def clear(self):
    self.log = ''

  def __str__(self):
    return self.log
