from flask import Flask, Response

app = Flask(__name__)

@app.route('/')
def home():
    return "🔒 Hello from Flask over HTTPS!"


@app.route('/keys')
def show_keys():
    certs_folder = "/app/certs/"
    try:
        with open(certs_folder + 'server.crt', 'r') as f:
            cert_content = f.read()
        with open(certs_folder + 'server.key', 'r') as f:
            key_content = f.read()
        combined = f"--- PUBLIC KEY / CERTIFICATE ---\n{cert_content}\n\n--- PRIVATE KEY ---\n{key_content}"
        return Response(combined, mimetype='text/plain')
    except Exception as e:
        return f"Error reading keys: {e}", 500
    

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
