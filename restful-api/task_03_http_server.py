#!/usr/bin/python3
"""A simple API built with Python's http.server module."""
import http.server
import json


class SimpleAPIHandler(http.server.BaseHTTPRequestHandler):
    """Handle GET requests and route them to the right endpoint."""

    def send_text(self, code, message):
        """Send a plain-text response with the given status code."""
        self.send_response(code)
        self.send_header("Content-Type", "text/plain")
        self.end_headers()
        self.wfile.write(message.encode("utf-8"))

    def send_json(self, code, data):
        """Send a dict as a JSON response with the given status code."""
        self.send_response(code)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(data).encode("utf-8"))

    def do_GET(self):
        """Route GET requests by path."""
        if self.path == "/":
            self.send_text(200, "Hello, this is a simple API!")
        elif self.path == "/data":
            self.send_json(200, {"name": "John", "age": 30,
                                 "city": "New York"})
        elif self.path == "/status":
            self.send_text(200, "OK")
        elif self.path == "/info":
            self.send_json(200, {"version": "1.0",
                                 "description":
                                 "A simple API built with http.server"})
        else:
            self.send_text(404, "Endpoint not found")


if __name__ == "__main__":
    server = http.server.HTTPServer(("", 8000), SimpleAPIHandler)
    print("Serving on port 8000")
    server.serve_forever()
