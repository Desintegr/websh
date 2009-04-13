from utitities import Utilities

import json
import re
import urllib

class Completion:

  def __init__(self, shell):
    self.shell = shell

  def complete(self, input):
    l = input.split(' ')

    matches = [m for m in self.shell.builtins.commands() if re.match(l[0], m)]
    matches_length = len(matches)

    # many matches found
    if matches_length > 1:
        command = input
        completion = Utilities.format(matches)

    # one match found
    elif len(matches) == 1:

      # space added for sub completion
      if re.match('{0}\s+'.format(matches[0]), input):
        try:
          submatches = \
            [m for m in eval('self.shell.builtins._{0}_completion()'.format(matches[0])) if \
              re.match(l[1], m)]
          submatches_length = len(submatches)

          # many submatches found
          if submatches_length > 1:
            command = input
            completion = Utilities.format(submatches)

          # one submatch found
          elif submatches_length == 1:
            command = '{0} {1}'.format(matches[0], submatches[0])
            completion = ''

          # no submatch found
          else:
            command = input
            completion = ''

        # _xxx_completion() does not exist
        except AttributeError:
          command = input
          completion = ''

      # partial or exact input
      else:
        command = matches[0]
        completion = ''

    # no match found
    else:
      command = input
      completion = ''

    return json.dumps({'command': command,
                       'completion': completion})
