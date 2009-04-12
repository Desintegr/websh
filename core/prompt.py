class Prompt:

  def __init__(self):
    self.directory = '~'

  def __str__(self):
    return '<span class="blue">{0}</span> <span class="green">$</span> '.format(self.directory)
