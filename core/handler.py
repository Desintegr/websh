import BaseHTTPServer
import re
import urllib

class Handler(BaseHTTPServer.BaseHTTPRequestHandler):

  def do_HEAD(self):
    self.send_response(200)
    self.send_header('Content-type', 'text/html')
    self.end_headers()

  def do_GET(self):
    # serve CSS
    if self.path == '/static/style.css':
      self.send_response(200)
      self.send_header('Content-Type', 'text/css')
      self.end_headers()

      self.wfile.write(self.server.css);

    # server favicon
    elif self.path == '/static/favicon.png':
      self.send_response(200)
      self.send_header('Content-Type', 'image/png')
      self.end_headers()

      self.wfile.write(self.server.favicon);

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
