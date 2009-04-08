from shell import Shell

import BaseHTTPServer

class Server(BaseHTTPServer.HTTPServer):

  def __init__(self, server_address, request_handler_class):
    BaseHTTPServer.HTTPServer.__init__(self, server_address, request_handler_class)

    self.shell = Shell()

    # read CSS
    file = open('data/style.css', 'r')
    self.css = file.read()
    file.close()

    # read favicon
    file = open('data/terminal.png', 'r')
    self.favicon = file.read()
    file.close()
