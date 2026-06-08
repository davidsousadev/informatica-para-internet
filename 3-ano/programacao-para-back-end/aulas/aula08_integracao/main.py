from http.server import BaseHTTPRequestHandler, HTTPServer

class Servidor(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write("Mensagem do back-end Python".encode())

HTTPServer(("localhost", 8000), Servidor).serve_forever()