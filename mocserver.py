import http.server
import json

def friendsget(args):
    js = {'response' : {
        'count' : 0,
        'items' : []
    }}
    if args['user_id'] == '1':
        js = {
            'response' : {
                'count' : 3,
                'items' : [1, 2, 3]
            }
        }
    elif args['user_id'] == '2':
        js = {
            'response' : {
                'count' : 4,
                'items' : [10, 12, 33, 46]
            }
        }
    elif args['user_id'] == '3':
        js = {
            'error' : {
                'error_code' : 201,
                'error+msg' : 'permissoin denied'
            }
        }
    return js

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
                response = 201
            elif method == None:
                js = { 'error' : {'error_msg' : 'unknown method'} }
                response = 201
            else:
                splited = splited[1].split('&')
                args = dict()
                for a in splited:
                    t = a.split('=')
                    print(t)
                    if len(t) == 2:
                        args[t[0]] = t[1]
                    else:
                        js = { 'error' : {'error_msg' : 'incorrect number of "=" in ' + a} }
                        response = 201
                        break
                else:
                    if 'access_token' in args.keys():
                        js = method(args)
                        response = 200
                    else:
                        js = { 'error' : {'error_msg' : 'invalid access token argument'} }
                        response = 201
        self.send_response(response)
        self.end_headers()
        self.wfile.write(json.dumps(js).encode())

if __name__ == "__main__":
    port = 80
    address = '127.8.8.8'
    httpd = http.server.HTTPServer((address, port), MyHandler)
    httpd.serve_forever()