"""
Lab 12 – Network Programming
Program B (client): Echo Client.
"""

import socket

HOST = "127.0.0.1"
PORT = 6001


def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        print(f"[Echo Client] Connected to {HOST}:{PORT}")

        while True:
            try:
                msg = input("Message: ")
            except EOFError:
                break

            s.sendall(msg.encode())
            data = s.recv(1024).decode()
            print(f"Echo: {data}")

            if msg.strip().lower() == "quit":
                break

    print("[Echo Client] Disconnected.")


if __name__ == "__main__":
    main()
