"""
Lab 12 – Network Programming
Program A (client): TCP Chat Client.
Sends messages to the server and prints replies.
"""

import socket

HOST = "127.0.0.1"
PORT = 6000


def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        print(f"[Client] Connected to {HOST}:{PORT}")

        while True:
            try:
                msg = input("[Client] Message: ")
            except EOFError:
                break

            s.sendall(msg.encode())

            data = s.recv(1024).decode()
            print(f"[Server]: {data}")

            if msg.strip().lower() == "quit" or data.strip().lower() in ("goodbye!", "quit"):
                break

    print("[Client] Connection closed.")


if __name__ == "__main__":
    main()
