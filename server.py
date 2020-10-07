#!/usr/bin/env python3

from http.server import BaseHTTPRequestHandler, HTTPServer
import urllib.parse, json, os

html_dir = '/home/pi/src/sound-machine/'

class S(BaseHTTPRequestHandler):

    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
    
    def do_HEAD(self):
        self._set_headers()

    def do_GET(self):
        self._set_headers()
        if (self.path == '/'):
            f = open(html_dir + 'index.html', "r")
            self.wfile.write(f.read().encode())
            f.close()
        else:
            self.wfile.write(self.path.encode())

    def do_POST(self):
        if (self.path == '/start'):
            length = int(self.headers['Content-Length'])
            post_str = self.rfile.read(length).decode('utf-8')
            post_parsed = urllib.parse.parse_qs(post_str)
            name = post_parsed['name'][0]
            os.system(html_dir + "repeat.sh " + name + " &")
            self.data_string = json.dumps({ 'res' : name })
        elif (self.path == '/stop'):
            print("stopping")
            os.system('killall repeat.sh')
            os.system('killall omxplayer')
            os.system('killall omxplayer.bin')
            self.data_string = json.dumps({'res' : 'stopped'})
        self.wfile.write(self.data_string.encode())


def run(server_class=HTTPServer, handler_class=S, port=80):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print('Starting httpd...')
    httpd.serve_forever()


if __name__ == "__main__":
    from sys import argv

if len(argv) == 2:
    run(port=int(argv[1]))
else:
    run()

