from utilities import Utilities

import json
import re
import urllib

class Completion:

  def __init__(self, shell):
    self.shell = shell

  def complete(self, input):
    l = re.split('\s+', input)

    matches = [m for m in self.shell.builtins.commands() if re.match(l[0], m)]
    matches_length = len(matches)

    # matches found
    if matches_length > 0:

      # partial or exact match
      if not l[1:]: # only on first word

        # many matches found
        if matches_length > 1:
          command = Utilities.longest_common_prefix(matches)
          completion = Utilities.format(matches)

        # one match found
        elif matches_length == 1:
          command = matches[0]
          completion = ''

      # exact match with space added for sub completion
      elif re.match('{0}\s+'.format(l[0]), input):

        try:
          submatches = \
            [m for m in eval('self.shell.builtins._{0}_completion()'.format(l[0])) if \
              re.match(' '.join(l[1:]).strip(), m)]
          submatches_length = len(submatches)

          # many submatches found
          if submatches_length > 1:
            command = '{0} {1}'.format(l[0], Utilities.longest_common_prefix(submatches))
            completion = Utilities.format(submatches)

          # one submatch found
          elif submatches_length == 1:
            command = '{0} {1}'.format(l[0], submatches[0])
            completion = ''

          # no submatch found
          else:
            command = input
            completion = ''

        # _xxx_completion() does not exist
        except AttributeError:
          command = input
          completion = ''

      # no match
      else:
        command = input
        completion = ''

    # no match found
    else:
      command = input
      completion = ''

    return json.dumps({'command': command,
                       'completion': completion})

