import http.server
import os

os.chdir("/Users/jonathanjosuesimancasdiaz/Desktop/Landing Neon Dash")

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory="/Users/jonathanjosuesimancasdiaz/Desktop/Landing Neon Dash", **kwargs)

with http.server.HTTPServer(("", 3000), Handler) as httpd:
    httpd.serve_forever()
