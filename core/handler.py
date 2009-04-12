import BaseHTTPServer
import re
import urllib

class Handler(BaseHTTPServer.BaseHTTPRequestHandler):

  def do_GET(self):
    # serve static files
    if self.path == '/static/style.css':
      self.serve_file('data/style.css', 'text/css')

    elif self.path == '/static/favicon.png':
      self.serve_file('data/terminal.png', 'text/html')

    elif self.path == '/static/jquery.js':
      self.serve_file('data/jquery.js', 'text/javascript')

    elif self.path == '/static/ajax.js':
      self.serve_file('data/ajax.js', 'text/javascript')

    # AJAX requests
    elif re.match('/ajax/command', self.path):
      self.send_response(200)
      self.send_header('Content-Type', 'application/json')
      self.end_headers()

      command = re.match('/ajax/command\?input=(.*)', self.path).group(1)
      command = urllib.unquote_plus(command)
      self.wfile.write(self.server.shell.execute(command))

    elif self.path == '/ajax/history_up':
      self.send_response(200)
      self.send_header('Content-Type', 'application/json')
      self.end_headers()

      self.wfile.write(self.server.shell.history.up())

    elif self.path == '/ajax/history_down':
      self.send_response(200)
      self.send_header('Content-Type', 'application/json')
      self.end_headers()

      self.wfile.write(self.server.shell.history.down())

    elif re.match('/ajax/completion', self.path):
      self.send_response(200)
      self.send_header('Content-Type', 'application/json')
      self.end_headers()

      complete = re.match('/ajax/completion\?input=(.*)', self.path).group(1)
      self.wfile.write(self.server.shell.completion.complete(complete))

    # default request
    else:
      self.send_response(200)
      self.send_header('Content-Type', 'text/html')
      self.end_headers()

      self.wfile.write(self.server.shell.template())

  def serve_file(self, file, type):
    self.send_response(200)
    self.send_header('Content-Type', type)
    self.end_headers()

    # read file
    f = open(file, 'r')
    content = f.read()
    f.close()

    self.wfile.write(content);
