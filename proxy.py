import socket
import threading
import os
import hashlib
import time
from datetime import datetime

PROXY_PORT = 8080
SERVER_HOST = "192.168.100.76"
SERVER_PORT = 8000
CACHE_DIR = "cache"

os.makedirs(CACHE_DIR, exist_ok=True)
cache_lock = threading.Lock()

def log(ip, path, status):
    print(f"[{datetime.now().strftime('%H:%M:%S')}] {ip} {path} {status}")

def cache_file(path):
    return os.path.join(CACHE_DIR, hashlib.md5(path.encode()).hexdigest())

def load_status_page(code):
    try:
        with open(os.path.join("status", f"{code}.html"), "rb") as f:
            return f.read()
    except:
        return f"<h1>{code}</h1>".encode()

def request_server(request):
    try:
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.settimeout(5)
        server.connect((SERVER_HOST, SERVER_PORT))
        server.sendall(request)

        data = b""
        while True:
            chunk = server.recv(4096)
            if not chunk:
                break
            data += chunk

        server.close()
        return data

    except socket.timeout:
        return b"HTTP/1.1 504 Gateway Timeout\r\nContent-Type:text/html\r\n\r\n" + load_status_page(504)

    except Exception:
        return b"HTTP/1.1 502 Bad Gateway\r\nContent-Type:text/html\r\n\r\n" + load_status_page(502)

def handle_client(conn, addr):
    try:
        request = conn.recv(4096)
        if not request:
            return

        text = request.decode(errors="ignore")
        path = text.split()[1]
        filename = cache_file(path)

        with cache_lock:
            if os.path.exists(filename):
                start = time.time()

                with open(filename, "rb") as f:
                    response = f.read()

                elapsed = (time.time() - start) * 1000

                print(f"[CACHE HIT] {path} | {elapsed:.2f} ms")

                conn.sendall(response)
                log(addr[0], path, f"HIT ({elapsed:.2f} ms)")
                return

        start = time.time()
        response = request_server(request)
        elapsed = (time.time() - start) * 1000

        print(f"[CACHE MISS] {path} | {elapsed:.2f} ms")

        if b"200 OK" in response:
            with cache_lock:
                with open(filename, "wb") as f:
                    f.write(response)

        conn.sendall(response)
        log(addr[0], path, f"MISS ({elapsed:.2f} ms)")

    except Exception as e:
        print("Proxy Error:", e)

    finally:
        conn.close()

def start_proxy():
    proxy = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    proxy.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    proxy.bind(("0.0.0.0", PROXY_PORT))
    proxy.listen(20)

    print(f"Proxy aktif di port {PROXY_PORT}")

    while True:
        conn, addr = proxy.accept()
        threading.Thread(target=handle_client, args=(conn, addr), daemon=True).start()

if __name__ == "__main__":
    start_proxy()
