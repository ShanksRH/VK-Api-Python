import http.server
import json

def friendsget():
    pass

def mymethod(name : str):
    if name == 'friends.get':
        return friendsget
    pass

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
        else:
            splited = splited[2].split('?')
            method = mymethod(splited[0])
            if len(splited) != 2:
                js = { 'error' : {'error_msg' : 'incorrect number of "?"'} }
                response = 202
            elif method == None:
                js = { 'error' : {'error_msg' : 'unknown method'} }
                response = 203
            else:
                splited = splited[1].split('&')
                args = []
                for a in splited:
                    t = a.split('=')
                    print(t)
                    if len(t) == 2:
                        args.append(t)
                    else:
                        js = { 'error' : {'error_msg' : 'incorrect number of "=" in ' + a} }
                        response = 203
                        break
                else:
                    js = {'others' : 'ok'}
                    response = 200
        self.send_response(response)
        self.end_headers()
        self.wfile.write(json.dumps(js).encode())

if __name__ == "__main__":
    port = 80
    address = '127.8.8.8'
    httpd = http.server.HTTPServer((address, port), MyHandler)
    httpd.serve_forever()