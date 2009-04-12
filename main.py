#!/usr/bin/python

import sys

HOSTNAME = '127.0.0.1'
PORT = 8080

def check_python_version():
  if sys.version_info < (2, 6, 0):
    print 'Error: Python 2.6 or higher is required!'
    sys.exit(1)

if __name__ == '__main__':
  check_python_version()

  from core.handler import Handler
  from core.server import Server

  server = Server((HOSTNAME, PORT), Handler)
  print 'Server is running - open your web browser to http://{0}:{1}'.format(HOSTNAME, PORT)

  try:
    server.serve_forever()
  except KeyboardInterrupt:
    pass

  server.server_close()
