from http.server import SimpleHTTPRequestHandler, HTTPServer

HOST = "0.0.0.0"
PORT = 8000

class MyHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(b"Hello from Docker + GitHub Actions + EC2!\n")

if __name__ == "__main__":
    server = HTTPServer((HOST, PORT), MyHandler)
    print(f"Server running on port {PORT}")
    server.serve_forever()
