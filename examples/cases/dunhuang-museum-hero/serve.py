#!/usr/bin/env python3
import argparse
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import unquote, urlsplit


SITE_ROOT = Path(__file__).resolve().parent / "site"


class SpaHandler(SimpleHTTPRequestHandler):
    quiet = False

    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(SITE_ROOT), **kwargs)

    def log_message(self, format, *args):
        if not self.quiet:
            super().log_message(format, *args)

    def send_head(self):
        request_path = unquote(urlsplit(self.path).path)
        candidate = (SITE_ROOT / request_path.lstrip("/")).resolve()
        try:
            candidate.relative_to(SITE_ROOT)
        except ValueError:
            self.send_error(404, "File not found")
            return None

        if request_path != "/" and not candidate.exists() and not candidate.suffix:
            self.path = "/index.html"
        return super().send_head()


def create_server(host="127.0.0.1", port=4173):
    return ThreadingHTTPServer((host, port), SpaHandler)


def main():
    parser = argparse.ArgumentParser(description="Serve the final Dunhuang Museum case.")
    parser.add_argument("--host", default="127.0.0.1")
    parser.add_argument("--port", type=int, default=4173)
    args = parser.parse_args()

    with create_server(args.host, args.port) as server:
        host, port = server.server_address[:2]
        print(f"Serving http://{host}:{port}/", flush=True)
        try:
            server.serve_forever()
        except KeyboardInterrupt:
            pass


if __name__ == "__main__":
    main()
