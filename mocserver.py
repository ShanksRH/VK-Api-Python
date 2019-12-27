import http.server
import json

class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/ping':
            self.send_response(200)
            self.end_headers()
            self.wfile.write(json.dumps({'ping':'ok'}).encode())
            return
        splited = self.path.split('/')
        print(splited)
        js = {'error' : 'unknown_error'}
        response = 199
        if len(splited) < 3 or splited[1] != 'method':
            js = { 'error' : {'error_msg' : 'should use method'} }
            response = 201
        self.send_response(response)
        self.end_headers()
        self.wfile.write(json.dumps(js).encode())

if __name__ == "__main__":
    port = 80
    address = '127.8.8.8'
    httpd = http.server.HTTPServer((address, port), MyHandler)
    httpd.serve_forever()