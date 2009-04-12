import BaseHTTPServer
import re
import urllib

class Handler(BaseHTTPServer.BaseHTTPRequestHandler):

  def do_HEAD(self):
    self.send_response(200)
    self.send_header('Content-type', 'text/html')
    self.end_headers()

  def do_GET(self):
    # serve static files
    if self.path == '/static/style.css':
      self.__serve_file('data/style.css', 'text/css')
    elif self.path == '/static/favicon.png':
      self.__serve_file('data/terminal.png', 'text/html')
    elif self.path == '/static/jquery.js':
      self.__serve_file('data/jquery.js', 'text/javascript')
    elif self.path == '/static/ajax.js':
      self.__serve_file('data/ajax.js', 'text/javascript')

    # ajax requests
    elif self.path == '/ajax/history_up':
      self.send_response(200)
      self.send_header('Content-Type', 'text/plain')
      self.end_headers()
      self.wfile.write(self.server.shell.history.up())
    elif self.path == '/ajax/history_down':
      self.send_response(200)
      self.send_header('Content-Type', 'text/plain')
      self.end_headers()
      self.wfile.write(self.server.shell.history.down())

    else:
      self.send_response(200)
      self.send_header('Content-Type', 'text/html')
      self.end_headers()

      self.wfile.write(self.server.shell)

  def do_POST(self):
    self.send_response(200)
    self.send_header('Content-Type', 'text/html')
    self.end_headers()

    # get POST content
    length = int(self.headers.getheader('Content-Length'))
    content = self.rfile.read(length)
    prompt = re.search('^prompt=(.*)$', content).group(1)
    # replace HTML espaces by their single-character equivalent
    prompt = urllib.unquote_plus(prompt)

    self.server.shell.execute(prompt)
    self.wfile.write(self.server.shell)

  def __serve_file(self, file, type):
    self.send_response(200)
    self.send_header('Content-Type', type)
    self.end_headers()

    # read file
    f = open(file, 'r')
    content = f.read()
    f.close()

    self.wfile.write(content);
