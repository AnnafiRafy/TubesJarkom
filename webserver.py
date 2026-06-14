import socket
import threading
import os
from datetime import datetime

HTTP_PORT = 8000
UDP_PORT = 9000

ROOT = os.path.dirname(os.path.abspath(__file__))

MIME = {
    ".html": "text/html",
    ".css": "text/css",
    ".js": "text/javascript",
    ".png": "image/png",
    ".jpg": "image/jpeg",
    ".jpeg": "image/jpeg",
    ".gif": "image/gif",
    ".mp4": "video/mp4"
}


def log(ip, path, status):
    print(
        f"[{datetime.now().strftime('%H:%M:%S')}] "
        f"IP={ip} FILE={path} STATUS={status}"
    )


def http_response(code, text, body=b"", ctype="text/html"):
    header = (
        f"HTTP/1.1 {code} {text}\r\n"
        f"Content-Type: {ctype}\r\n"
        f"Content-Length: {len(body)}\r\n"
        f"Connection: close\r\n\r\n"
    ).encode()

    return header + body


def handle_client(conn, addr):
    path = "/"

    try:
        request = conn.recv(4096).decode(errors="ignore")

        if not request:
            return

        first_line = request.split("\r\n")[0]
        method, path, _ = first_line.split()

        if method != "GET":
            body = b"<h1>405 Method Not Allowed</h1>"

            conn.sendall(
                http_response(
                    405,
                    "Method Not Allowed",
                    body
                )
            )

            log(addr[0], path, 405)
            return

        if path == "/":
            path = "/index.html"

        path = path.split("?")[0]

        file_path = os.path.abspath(
            os.path.join(ROOT, path.lstrip("/"))
        )

        if not file_path.startswith(ROOT):
            raise Exception("Invalid path")

        if not os.path.exists(file_path):
            body = b"<h1>404 Not Found</h1>"

            conn.sendall(
                http_response(
                    404,
                    "Not Found",
                    body
                )
            )

            log(addr[0], path, 404)
            return

        with open(file_path, "rb") as f:
            body = f.read()

        ext = os.path.splitext(file_path)[1]

        conn.sendall(
            http_response(
                200,
                "OK",
                body,
                MIME.get(ext, "application/octet-stream")
            )
        )

        log(addr[0], path, 200)

    except Exception as e:

        body = f"<h1>500 Internal Server Error</h1><p>{e}</p>".encode()

        conn.sendall(
            http_response(
                500,
                "Internal Server Error",
                body
            )
        )

        log(addr[0], path, 500)

    finally:
        conn.close()


def http_server():
    server = socket.socket(
        socket.AF_INET,
        socket.SOCK_STREAM
    )

    server.setsockopt(
        socket.SOL_SOCKET,
        socket.SO_REUSEADDR,
        1
    )

    server.bind(("0.0.0.0", HTTP_PORT))
    server.listen(10)

    print(f"HTTP Server aktif di port {HTTP_PORT}")

    while True:
        conn, addr = server.accept()

        threading.Thread(
            target=handle_client,
            args=(conn, addr),
            daemon=True
        ).start()


def udp_server():
    udp = socket.socket(
        socket.AF_INET,
        socket.SOCK_DGRAM
    )

    udp.bind(("0.0.0.0", UDP_PORT))

    print(f"UDP Echo aktif di port {UDP_PORT}")

    while True:
        data, addr = udp.recvfrom(2048)

        udp.sendto(data, addr)


if __name__ == "__main__":

    threading.Thread(
        target=udp_server,
        daemon=True
    ).start()

    http_server()