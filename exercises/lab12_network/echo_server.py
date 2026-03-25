"""
Lab 12 – Network Programming
Program B (server): Echo Server — sends back exactly what it receives.
"""

import socket

HOST = "127.0.0.1"
PORT = 6001


def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as srv:
        srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        srv.bind((HOST, PORT))
        srv.listen(1)
        print(f"[Echo Server] Listening on {HOST}:{PORT}")

        conn, addr = srv.accept()
        print(f"[Echo Server] Connected: {addr}")

        with conn:
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                print(f"[Echo Server] Echoing: {data.decode()!r}")
                conn.sendall(data)
                if data.strip().lower() == b"quit":
                    break

    print("[Echo Server] Closed.")


if __name__ == "__main__":
    main()
