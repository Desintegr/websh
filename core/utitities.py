import cgi

class Utilities:

  @staticmethod
  def format(l, words_per_line = 5, ljust = 15):
    s = ''
    for i, e in enumerate(l):
      s += cgi.escape(e.ljust(ljust, ' ')).replace(' ', '&nbsp;')
      if (i + 1) % words_per_line == 0 and i != len(l) - 1:
        s += "<br/>\n"

    return s

  @staticmethod
  def tab(l, ljust = 15):
    s = ''
    for e in l:
      s += cgi.escape(e.ljust(ljust, ' ')).replace(' ', '&nbsp;')

    return s

  @staticmethod
  def longest_common_prefix(l):
    if not l:
      return ''

    prefix = l[0]
    for item in l:
      for i in range(len(prefix)):
        if prefix[:i+1] != item[:i+1]:
          prefix = prefix[:i]
          if i == 0:
            return ''
          break

    return prefix

