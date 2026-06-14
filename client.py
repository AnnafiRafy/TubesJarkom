import socket, time, argparse, threading

PROXY_HOST = "192.168.56.1"      # IP Proxy
PROXY_PORT = 8080

UDP_HOST = "192.168.100.1"       # IP Web Server
UDP_PORT = 9000


def tcp_request(path="/index.html"):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((PROXY_HOST, PROXY_PORT))

    req = (
        f"GET {path} HTTP/1.1\r\n"
        f"Host: proxy\r\n"
        f"Connection: close\r\n\r\n"
    )

    mulai = time.time()
    s.sendall(req.encode())

    data = b""
    while True:
        chunk = s.recv(4096)
        if not chunk:
            break
        data += chunk

    s.close()

    rtt = (time.time() - mulai) * 1000

    print("\n=== RESPONSE ===")
    print(data.decode(errors="ignore"))
    print(f"\nWaktu respons: {rtt:.2f} ms")


def udp_qos(jumlah=10):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.settimeout(1)

    rtt = []
    diterima = 0

    for i in range(jumlah):
        pesan = f"Ping {i} {time.time()}".encode()

        mulai = time.time()
        s.sendto(pesan, (UDP_HOST, UDP_PORT))

        try:
            data, _ = s.recvfrom(2048)

            waktu = (time.time() - mulai) * 1000
            rtt.append(waktu)

            diterima += len(data)

            print(f"Ping {i}: {waktu:.2f} ms")

        except socket.timeout:
            print(f"Ping {i}: Request timed out")

    s.close()

    loss = (jumlah - len(rtt)) / jumlah * 100

    if rtt:
        rtt_min = min(rtt)
        rtt_avg = sum(rtt) / len(rtt)
        rtt_max = max(rtt)

        diff = [
            abs(rtt[i] - rtt[i - 1])
            for i in range(1, len(rtt))
        ]

        jitter = sum(diff) / len(diff) if diff else 0

        durasi = sum(rtt) / 1000
        throughput = (diterima * 8) / durasi / 1000 if durasi else 0
    else:
        rtt_min = rtt_avg = rtt_max = jitter = throughput = 0

    print("\n=== HASIL QoS ===")
    print(f"RTT Min : {rtt_min:.2f} ms")
    print(f"RTT Avg : {rtt_avg:.2f} ms")
    print(f"RTT Max : {rtt_max:.2f} ms")
    print(f"Packet Loss : {loss:.2f}%")
    print(f"Jitter : {jitter:.2f} ms")
    print(f"Throughput : {throughput:.2f} kbps")


def banyak_client(jumlah=5):
    threads = []

    for _ in range(jumlah):
        t = threading.Thread(target=tcp_request)
        t.start()
        threads.append(t)

    for t in threads:
        t.join()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--mode",
        choices=["tcp", "udp", "multi"],
        default="tcp"
    )

    parser.add_argument(
        "--path",
        default="/index.html"
    )

    parser.add_argument(
        "--jumlah",
        type=int,
        default=10
    )

    args = parser.parse_args()

    if args.mode == "tcp":
        tcp_request(args.path)

    elif args.mode == "udp":
        udp_qos(args.jumlah)

    else:
        banyak_client(args.jumlah)