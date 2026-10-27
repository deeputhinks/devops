from http.server import HTTPServer, BaseHTTPRequestHandler
import json
import os

REQUEST_COUNT = 0
HEALTH_CHECK_COUNT = 0

class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        global REQUEST_COUNT, HEALTH_CHECK_COUNT
        REQUEST_COUNT += 1

        app_env = os.getenv("APP_ENV", "local-development")
        secret_key = os.getenv("API_SECRET_KEY", "no-secret-provided")
        masked_secret = secret_key[:3] + "****" if len(secret_key) > 3 else "****"

        if self.path == "/health":
            HEALTH_CHECK_COUNT += 1
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            response = {
                "status": "UP",
                "environment": app_env,
                "secret_configured": secret_key != "no-secret-provided",
                "secret_masked": masked_secret
            }
            self.wfile.write(json.dumps(response, indent=2).encode())

        elif self.path == "/metrics":
            self.send_response(200)
            self.send_header("Content-Type", "text/plain; version=0.0.4")
            self.end_headers()
            metrics_payload = (
                "# HELP http_requests_total Total number of HTTP requests\n"
                "# TYPE http_requests_total counter\n"
                f'http_requests_total{{env="{app_env}"}} {REQUEST_COUNT}\n\n'
                "# HELP http_health_checks_total Total number of health check requests\n"
                "# TYPE http_health_checks_total counter\n"
                f'http_health_checks_total{{env="{app_env}"}} {HEALTH_CHECK_COUNT}\n'
            )
            self.wfile.write(metrics_payload.encode())

        else:
            self.send_response(200)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write(f"DevOps Service | Running in [{app_env}] environment\n".encode())

if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    server = HTTPServer(("0.0.0.0", port), SimpleHandler)
    print(f"Server running on port {port}...")
    server.serve_forever()
