from flask import Flask, request
from datetime import datetime
import socket

app = Flask(__name__)

@app.route("/")
def home():
    server_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    client_ip = request.headers.get('X-Forwarded-For', request.remote_addr)
    server_ip = socket.gethostbyname(socket.gethostname())

    return {
        "hello_world": "Hello World!",
        "server_time": server_time,
        "client_ip": client_ip,
        "server_ip": server_ip
    }

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)

