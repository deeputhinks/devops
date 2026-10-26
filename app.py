from http.server import HTTPServer, BaseHTTPRequestHandler
import json
import os

class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Read dynamic configuration from environment variables
        app_env = os.getenv("APP_ENV", "local-development")
        secret_key = os.getenv("API_SECRET_KEY", "no-secret-provided")

        # Mask the secret so only the first 3 characters show (security best practice)
        masked_secret = secret_key[:3] + "****" if len(secret_key) > 3 else "****"

        if self.path == "/health":
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
