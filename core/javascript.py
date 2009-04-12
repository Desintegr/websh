class Javascript:

  def __init__(self):
    self.javascript = ''

  def append(self, javascript):
    self.javascript += javascript

  def __str__(self):
    javascript = self.javascript
    self.javascript = ''
    return javascript

