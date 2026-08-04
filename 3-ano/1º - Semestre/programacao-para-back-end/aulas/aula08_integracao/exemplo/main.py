from http.server import *

class Servidor(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write("300-Info".encode())

HTTPServer(("localhost", 7777), Servidor).serve_forever()