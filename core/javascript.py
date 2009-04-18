class Javascript:

  def __init__(self):
    self.javascript = []

  def append(self, javascript):
    self.javascript.append(javascript)

  def __str__(self):
    javascript = self.javascript
    self.javascript = []
    return ''.join(javascript)

