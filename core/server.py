from shell import Shell

import BaseHTTPServer

class Server(BaseHTTPServer.HTTPServer):

  def __init__(self, server_address, request_handler_class):
    BaseHTTPServer.HTTPServer.__init__(self, server_address, request_handler_class)

    self.shell = Shell()
