#!/usr/bin/env python3
"""taxila-portal: a one-page practice application for the Day 4 lab.

It shows a form that asks for your index number and replies "Received".
It listens only on this machine (127.0.0.1), so nothing outside your own
virtual machine can reach it, and it uses only Python's standard library.

Plain web (port 8080):
    python3 taxila-portal.py

Secure web (port 8443), with the certificate and private key you made:
    python3 taxila-portal.py --secure --cert portal-cert.pem --key private.pem

Stop it with Ctrl+C.
"""
import argparse
import html
import http.server
import re
import ssl
import sys
import urllib.parse

HOST = "127.0.0.1"
INDEX_RULE = re.compile(r"^[A-Za-z0-9]{1,20}$")

PAGE = """<!doctype html>
<html lang="en-GB">
<head><meta charset="utf-8"><title>Taxila College portal</title></head>
<body style="font-family:sans-serif;max-width:32rem;margin:2rem auto">
<h1>Taxila College portal</h1>
<p>{message}</p>
<form method="post" action="/submit">
<label for="index">Your index number</label>
<input id="index" name="index" maxlength="20" autocomplete="off">
<button type="submit">Submit</button>
</form>
<p><small>Practice application for the Day 4 lab. It runs only on this machine.</small></p>
</body>
</html>
"""


class Portal(http.server.BaseHTTPRequestHandler):
    server_version = "taxila-portal"
    sys_version = ""

    def log_message(self, fmt, *args):
        # One short line per request, without the date and time.
        sys.stderr.write("request from your browser: " + (fmt % args) + "\n")

    def send_response(self, code, message=None):
        # Only the status line and a Server header: no Date header, so a capture carries no calendar date.
        self.log_request(code)
        self.send_response_only(code, message)
        self.send_header("Server", self.server_version)

    def reply(self, code, message):
        body = PAGE.format(message=message).encode("utf-8")
        self.send_response(code)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):
        if self.path != "/":
            self.reply(404, "That page does not exist. Go back to the form.")
            return
        self.reply(200, "Enter your index number, written without spaces or hyphens.")

    def do_POST(self):
        if self.path != "/submit":
            self.reply(404, "That page does not exist. Go back to the form.")
            return
        size = int(self.headers.get("Content-Length") or 0)
        fields = urllib.parse.parse_qs(self.rfile.read(min(size, 1000)).decode("utf-8", "replace"))
        index = (fields.get("index") or [""])[0].strip()
        if not INDEX_RULE.match(index):
            self.reply(400, "An index number has only letters and digits. Please try again.")
            return
        # The reply shows the value as text, never as markup.
        self.reply(200, "Received: " + html.escape(index) + ". Now look at what your capture shows.")


class QuietServer(http.server.ThreadingHTTPServer):
    def handle_error(self, request, client_address):
        # A browser that refuses an untrusted certificate closes the connection; say so in one line.
        print("a connection was closed by the browser (for example, after a certificate warning)")


def main():
    ap = argparse.ArgumentParser(description="Practice portal for the Day 4 lab (listens on 127.0.0.1 only).")
    ap.add_argument("--secure", action="store_true", help="serve secure web (port 8443) instead of plain web (port 8080)")
    ap.add_argument("--cert", help="your certificate file, for --secure")
    ap.add_argument("--key", help="your private key file, for --secure")
    ap.add_argument("--port", type=int, help="a different port, if the usual one is busy")
    a = ap.parse_args()
    port = a.port or (8443 if a.secure else 8080)
    httpd = QuietServer((HOST, port), Portal)
    if a.secure:
        if not (a.cert and a.key):
            sys.exit("Secure web needs --cert and --key: the certificate and private key you made in the lab.")
        ctx = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
        ctx.minimum_version = ssl.TLSVersion.TLSv1_2
        ctx.load_cert_chain(a.cert, a.key)
        httpd.socket = ctx.wrap_socket(httpd.socket, server_side=True)
        print(f"Secure web: open https://{HOST}:{port}/ in the browser. Stop with Ctrl+C.")
    else:
        print(f"Plain web: open http://{HOST}:{port}/ in the browser. Stop with Ctrl+C.")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nStopped.")


if __name__ == "__main__":
    main()
