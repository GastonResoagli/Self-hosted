from http.server import HTTPServer, BaseHTTPRequestHandler

class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()
        response_html = """
        <!DOCTYPE html>
        <html>
        <head>
            <style>
                body { font-family: system-ui, sans-serif; background: #0f172a; color: #f8fafc; display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; }
                .card { background: #1e293b; padding: 2rem; border-radius: 12px; box-shadow: 0 4px 20px rgba(0,0,0,0.3); text-align: center; border: 1px solid #334155; }
                h1 { color: #38bdf8; margin-bottom: 0.5rem; }
            </style>
        </head>
        <body>
            <div class="card">
                <h1>🐍 API en Python 3</h1>
                <p>Servidor microservicio ejecutándose en contenedor Docker.</p>
            </div>
        </body>
        </html>
        """
        self.wfile.write(response_html.encode('utf-8'))

if __name__ == '__main__':
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, SimpleHandler)
    print("Servidor Python activo en el puerto 8000...")
    httpd.serve_forever()