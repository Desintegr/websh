import string

class Shell:

  def __init__(self):
    # read template file
    file = open('data/template.html', 'r')
    self.template = string.Template(file.read())
    file.close()

    self.prompt = '<span class="directory">~</span> <span class="prompt">$</span> '
    self.log = ''

  def execute(self, prompt):
    self.log += self.prompt + prompt + '<br/>' + "\n"

  def __str__(self):
    return self.template.substitute(prompt=self.prompt, log=self.log)
