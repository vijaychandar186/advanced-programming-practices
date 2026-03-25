"""
Lab 12 – Network Programming
Program C (server): FTP-style file server over TCP.

Commands accepted from the client:
  LIST              – list files in server_files/
  DOWNLOAD <name>   – send the named file to the client
  QUIT              – close the connection
"""

import os
import socket

HOST       = "127.0.0.1"
PORT       = 6002
SEPARATOR  = "<SEP>"
BUFFER     = 4096
SERVER_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "server_files")


def send_file(conn: socket.socket, filepath: str) -> None:
    size = os.path.getsize(filepath)
    conn.sendall(f"OK{SEPARATOR}{os.path.basename(filepath)}{SEPARATOR}{size}".encode())
    ack = conn.recv(16)
    if ack != b"READY":
        return
    with open(filepath, "rb") as f:
        while chunk := f.read(BUFFER):
            conn.sendall(chunk)
    print(f"[FTP Server] Sent '{os.path.basename(filepath)}' ({size} bytes)")


def main():
    os.makedirs(SERVER_DIR, exist_ok=True)

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as srv:
        srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        srv.bind((HOST, PORT))
        srv.listen(1)
        print(f"[FTP Server] Listening on {HOST}:{PORT}")
        print(f"[FTP Server] Serving files from: {SERVER_DIR}")

        conn, addr = srv.accept()
        print(f"[FTP Server] Client connected: {addr}")

        with conn:
            while True:
                try:
                    raw = conn.recv(1024)
                except ConnectionResetError:
                    break
                if not raw:
                    break

                command = raw.decode().strip()
                print(f"[FTP Server] Command: {command!r}")
                parts = command.split(maxsplit=1)
                cmd   = parts[0].upper()

                if cmd == "QUIT":
                    conn.sendall(b"BYE")
                    break

                elif cmd == "LIST":
                    files = os.listdir(SERVER_DIR)
                    listing = "\n".join(files) if files else "(empty)"
                    conn.sendall(listing.encode())

                elif cmd == "DOWNLOAD":
                    if len(parts) < 2:
                        conn.sendall(b"ERROR: no filename")
                        continue
                    filepath = os.path.join(SERVER_DIR, parts[1].strip())
                    if not os.path.isfile(filepath):
                        conn.sendall(f"ERROR{SEPARATOR}File not found".encode())
                    else:
                        send_file(conn, filepath)

                else:
                    conn.sendall(b"ERROR: unknown command")

    print("[FTP Server] Closed.")


if __name__ == "__main__":
    main()
