import http.server
import json

class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/ping':
            self.send_response(200)
            self.end_headers()
            self.wfile.write(json.dumps({'ping':'ok'}).encode())
            return
        http.server.SimpleHTTPRequestHandler.do_GET(self)

if __name__ == "__main__":
    port = 80
    address = '127.8.8.8'
    httpd = http.server.HTTPServer((address, port), MyHandler)
    httpd.serve_forever()