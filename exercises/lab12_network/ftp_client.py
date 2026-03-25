"""
Lab 12 – Network Programming
Program C (client): FTP-style client.

Commands:
  list               – list files on server
  download <name>    – download a file from the server
  quit               – disconnect
"""

import os
import socket

HOST       = "127.0.0.1"
PORT       = 6002
SEPARATOR  = "<SEP>"
BUFFER     = 4096
CLIENT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "client_files")


def recv_all(s: socket.socket, size: int) -> bytes:
    data = b""
    while len(data) < size:
        chunk = s.recv(min(BUFFER, size - len(data)))
        if not chunk:
            break
        data += chunk
    return data


def main():
    os.makedirs(CLIENT_DIR, exist_ok=True)

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        print(f"[FTP Client] Connected to {HOST}:{PORT}")
        print("Commands: list, download <filename>, quit\n")

        while True:
            try:
                cmd = input("ftp> ").strip()
            except EOFError:
                break
            if not cmd:
                continue

            if cmd == "list":
                s.sendall(b"LIST")
                data = s.recv(4096).decode()
                print("Files on server:")
                print(data)

            elif cmd.startswith("download "):
                filename = cmd[9:].strip()
                s.sendall(f"DOWNLOAD {filename}".encode())

                header_raw = s.recv(256).decode()
                parts = header_raw.split(SEPARATOR)

                if parts[0] == "OK" and len(parts) == 3:
                    _, fname, size_str = parts
                    size = int(size_str)
                    s.sendall(b"READY")
                    file_data = recv_all(s, size)
                    dest = os.path.join(CLIENT_DIR, fname)
                    with open(dest, "wb") as f:
                        f.write(file_data)
                    print(f"Downloaded '{fname}' ({size} bytes) → {dest}")
                else:
                    print(f"Server: {header_raw}")

            elif cmd == "quit":
                s.sendall(b"QUIT")
                print(s.recv(256).decode())
                break

            else:
                print("Unknown command. Try: list, download <filename>, quit")

    print("[FTP Client] Disconnected.")


if __name__ == "__main__":
    main()
