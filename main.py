#!/usr/bin/python

from core.handler import Handler
from core.server import Server

HOSTNAME = '127.0.0.1'
PORT = 8080

if __name__ == '__main__':
  server = Server((HOSTNAME, PORT), Handler)
  print 'server running - open your web browser to http://%s:%s' % (HOSTNAME, PORT)

  try:
    server.serve_forever()
  except KeyboardInterrupt:
    pass

  server.server_close()
