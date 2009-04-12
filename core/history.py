class History:

  def __init__(self):
    self.history = []
    self.history.append('')
    self.position = 0

  def append(self, command):
    if len(self.history) < 100: # size limit
      self.history.insert(0, command)

    self.position = 0

  def up(self):
    if self.position < len(self.history) - 1:
      self.position += 1

    return self.history[self.position - 1]

  def down(self):
    if self.position > 0:
      self.position -= 1

    return self.history[self.position - 1]

