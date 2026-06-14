# Tugas Besar Jaringan Komputer

### Kelompok Padmagriya

| Nama                        | NIM          |
| --------------------------- | ------------ |
| Kavka Yuza Gazetta          | 103012400339 |
| Muhammad Akhtar Siddiq      | 103012400089 |
| Annafy Rafy Kurnia Nurhakim | 103012400352 |

---

## Deskripsi Proyek

Proyek ini merupakan implementasi sistem jaringan berbasis arsitektur **Client–Proxy–Server** menggunakan **Socket Programming Python**.

Sistem terdiri dari tiga komponen utama:

1. **Client (client.py)**

   * Mengirim HTTP Request ke Proxy Server.
   * Melakukan pengujian QoS menggunakan UDP Ping.
   * Mendukung pengujian multi-client secara konkuren.

2. **Proxy Server (proxy.py)**

   * Menerima request dari Client.
   * Meneruskan request ke Web Server.
   * Menyimpan response ke cache.
   * Melayani Cache HIT dan Cache MISS.

3. **Web Server (webserver.py)**

   * Menyediakan layanan HTTP menggunakan TCP.
   * Menyediakan layanan UDP Echo untuk pengukuran QoS.
   * Menangani beberapa koneksi secara simultan menggunakan multithreading.

---

## Teknologi yang Digunakan

* Python 3
* Socket Programming
* TCP
* UDP
* Multithreading
* Wireshark (Analisis Jaringan)

---

## Struktur Folder

```text
TubesJarkom/
│
├── client.py
├── proxy.py
├── webserver.py
│
├── index.html
├── style.css
├── assets/
│
└── README.md
```

---

## Konfigurasi Port

| Komponen     | Protokol | Port |
| ------------ | -------- | ---- |
| Web Server   | TCP      | 8000 |
| Web Server   | UDP      | 9000 |
| Proxy Server | TCP      | 8080 |

---

## Fitur yang Diimplementasikan

### Web Server

* HTTP GET Request
* HTTP Response
* Status Code 200 OK
* Status Code 404 Not Found
* Status Code 500 Internal Server Error
* UDP Echo Server
* Multithreading

### Proxy Server

* HTTP Forwarding
* Cache HIT
* Cache MISS
* Error Handling
* Multithreading

### Client

* HTTP Client
* UDP QoS Measurement
* RTT Measurement
* Packet Loss Calculation
* Jitter Calculation
* Throughput Calculation
* Multi-client Testing

---

## Parameter Quality of Service (QoS)

Parameter yang diukur:

* RTT (Round Trip Time)
* Packet Loss (%)
* Jitter (ms)
* Throughput (kbps)

---

## Hasil yang Diharapkan

* Client dapat mengakses halaman web melalui Proxy Server.
* Proxy dapat melakukan caching terhadap response dari Web Server.
* Web Server dapat menangani beberapa koneksi secara bersamaan.
* Sistem mampu melakukan pengukuran QoS menggunakan UDP Echo.
# Tugas Besar Jaringan Komputer

### Kelompok Padmagriya

| Nama                        | NIM          |
| --------------------------- | ------------ |
| Kavka Yuza Gazetta          | 103012400339 |
| Muhammad Akhtar Siddiq      | 103012400089 |
| Annafy Rafy Kurnia Nurhakim | 103012400352 |

---

## Deskripsi Proyek

Proyek ini merupakan implementasi sistem jaringan berbasis arsitektur **Client–Proxy–Server** menggunakan **Socket Programming Python**.

Sistem terdiri dari tiga komponen utama:

1. **Client (client.py)**

   * Mengirim HTTP Request ke Proxy Server.
   * Melakukan pengujian QoS menggunakan UDP Ping.
   * Mendukung pengujian multi-client secara konkuren.

2. **Proxy Server (proxy.py)**

   * Menerima request dari Client.
   * Meneruskan request ke Web Server.
   * Menyimpan response ke cache.
   * Melayani Cache HIT dan Cache MISS.

3. **Web Server (webserver.py)**

   * Menyediakan layanan HTTP menggunakan TCP.
   * Menyediakan layanan UDP Echo untuk pengukuran QoS.
   * Menangani beberapa koneksi secara simultan menggunakan multithreading.

---

## Teknologi yang Digunakan

* Python 3
* Socket Programming
* TCP
* UDP
* Multithreading
* Wireshark (Analisis Jaringan)

---

## Struktur Folder

```text
TubesJarkom/
│
├── client.py
├── proxy.py
├── webserver.py
│
├── index.html
├── style.css
├── assets/
│
└── README.md
```

---

## Konfigurasi Port

| Komponen     | Protokol | Port |
| ------------ | -------- | ---- |
| Web Server   | TCP      | 8000 |
| Web Server   | UDP      | 9000 |
| Proxy Server | TCP      | 8080 |

---

## Fitur yang Diimplementasikan

### Web Server

* HTTP GET Request
* HTTP Response
* Status Code 200 OK
* Status Code 404 Not Found
* Status Code 500 Internal Server Error
* UDP Echo Server
* Multithreading

### Proxy Server

* HTTP Forwarding
* Cache HIT
* Cache MISS
* Error Handling
* Multithreading

### Client

* HTTP Client
* UDP QoS Measurement
* RTT Measurement
* Packet Loss Calculation
* Jitter Calculation
* Throughput Calculation
* Multi-client Testing

---

## Parameter Quality of Service (QoS)

Parameter yang diukur:

* RTT (Round Trip Time)
* Packet Loss (%)
* Jitter (ms)
* Throughput (kbps)

---

## Hasil yang Diharapkan

* Client dapat mengakses halaman web melalui Proxy Server.
* Proxy dapat melakukan caching terhadap response dari Web Server.
* Web Server dapat menangani beberapa koneksi secara bersamaan.
* Sistem mampu melakukan pengukuran QoS menggunakan UDP Echo.
