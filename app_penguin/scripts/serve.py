from http.server import HTTPServer, SimpleHTTPRequestHandler
import os
from pathlib import Path
import webbrowser



def serve(site_path: Path, port: int = 8000):
    os.chdir(site_path)
    server = HTTPServer(('localhost', port), SimpleHTTPRequestHandler)
    print(f"Sirviendo {site_path} en http://localhost:{port}")
    webbrowser.open(f'http://localhost:{port}')
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\n Servidor detenido")


