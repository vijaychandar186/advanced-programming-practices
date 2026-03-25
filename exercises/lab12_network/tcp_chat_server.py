"""
Lab 12 – Network Programming
Program A (server): TCP Chat Server.
Receives messages from the client and sends replies typed on the server.
"""

import socket

HOST = "127.0.0.1"
PORT = 6000


def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as srv:
        srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        srv.bind((HOST, PORT))
        srv.listen(1)
        print(f"[Server] TCP Chat listening on {HOST}:{PORT}")

        conn, addr = srv.accept()
        print(f"[Server] Connected: {addr}")

        with conn:
            while True:
                data = conn.recv(1024)
                if not data:
                    print("[Server] Client disconnected.")
                    break

                msg = data.decode()
                print(f"[Client]: {msg}")

                if msg.strip().lower() == "quit":
                    conn.sendall(b"Goodbye!")
                    break

                try:
                    reply = input("[Server] Reply: ")
                except EOFError:
                    conn.sendall(b"Goodbye!")
                    break

                conn.sendall(reply.encode())

                if reply.strip().lower() == "quit":
                    break

    print("[Server] Closed.")


if __name__ == "__main__":
    main()
