import json

from http.server import HTTPServer, BaseHTTPRequestHandler


class echoHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('content-type', 'text/html')
        self.end_headers()

        output = "<html><body>Testing</body></html>"
        self.wfile.write(output.encode())

    def do_POST(self):
        if self.path.endswith('/task'):
            data_string = self.rfile.read(int(self.headers['Content-Length']))
            print(json.loads(data_string)["task"])


        self.send_response(301)
        self.send_header('content-type', 'text/html')
        self.end_headers()


def main():
    PORT = 9000
    server_address = ('localhost', PORT)
    server = HTTPServer(server_address, echoHandler)
    print('Server running on port %s' % PORT)
    server.serve_forever()


if __name__ == '__main__':
    main()
