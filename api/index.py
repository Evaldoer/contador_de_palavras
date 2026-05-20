from http.server import BaseHTTPRequestHandler
from pathlib import Path
from urllib.parse import urlparse


ROOT = Path(__file__).resolve().parent.parent
PUBLIC_FILES = {
    "/": ("index.html", "text/html; charset=utf-8"),
    "/index.html": ("index.html", "text/html; charset=utf-8"),
    "/styles.css": ("styles.css", "text/css; charset=utf-8"),
    "/app.js": ("app.js", "application/javascript; charset=utf-8"),
    "/dados.csv": ("dados.csv", "text/csv; charset=utf-8"),
}


class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        route = urlparse(self.path).path
        file_info = PUBLIC_FILES.get(route)

        if file_info is None:
            self.send_error(404, "Arquivo nao encontrado")
            return

        filename, content_type = file_info
        body = (ROOT / filename).read_bytes()

        self.send_response(200)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)
