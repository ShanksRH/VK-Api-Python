import http.server

class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        return http.server.SimpleHTTPRequestHandler.do_GET(self)

class MocServer(http.server.HTTPServer):
    port = 80
    address = '127.8.8.8'
    def __init__(self):
        self.httpd = http.server.HTTPServer((self.address, self.port), MyHandler)
