import socket
import sys


class FtpClient:
    def __init__(self, host: str, port: int = 21, timeout: float = 10.0) -> None:
        self._host = host
        self._port = port
        self._timeout = timeout
        self._control = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._reader = None

    def connect(self) -> str:
        self._control = socket.create_connection((self._host, self._port), self._timeout)
        self._reader = self._control.makefile("r", encoding="latin-1", newline="\r\n")
        return self._read_response()

    def _read_response(self) -> str:
        line = self._reader.readline()
        code = line[:3]
        if line[3:4] == "-":
            while True:
                current = self._reader.readline()
                if current[:3] == code and current[3:4] == " ":
                    break
        return line.strip()

    def _send(self, command: str) -> str:
        self._control.sendall((command + "\r\n").encode("latin-1"))
        return self._read_response()

    def login(self, user: str = "anonymous", password: str = "guest@example.com") -> str:
        self._send(f"USER {user}")
        return self._send(f"PASS {password}")

    def _enter_passive(self) -> socket.socket:
        response = self._send("PASV")
        numbers = [int(value) for value in response[response.index("(") + 1 : response.index(")")].split(",")]
        ip = ".".join(str(value) for value in numbers[:4])
        port = numbers[4] * 256 + numbers[5]
        return socket.create_connection((ip, port), self._timeout)

    def list_dir(self, path: str = "") -> str:
        self._send("TYPE A")
        data_socket = self._enter_passive()
        self._send(f"LIST {path}".strip())
        with data_socket:
            chunks = []
            while True:
                chunk = data_socket.recv(4096)
                if not chunk:
                    break
                chunks.append(chunk)
        self._read_response()
        return b"".join(chunks).decode("latin-1")

    def retrieve(self, remote_path: str) -> bytes:
        self._send("TYPE I")
        data_socket = self._enter_passive()
        self._send(f"RETR {remote_path}")
        with data_socket:
            chunks = []
            while True:
                chunk = data_socket.recv(4096)
                if not chunk:
                    break
                chunks.append(chunk)
        self._read_response()
        return b"".join(chunks)

    def quit(self) -> None:
        try:
            self._send("QUIT")
        finally:
            self._control.close()


def main() -> None:
    host = sys.argv[1] if len(sys.argv) > 1 else "ftp.gnu.org"
    client = FtpClient(host)
    try:
        print(client.connect())
        print(client.login())
        listing = client.list_dir("/")
        print("\nСодержимое /:")
        for line in listing.splitlines()[:10]:
            print(" ", line)
        client.quit()
    except (socket.timeout, OSError) as error:
        print(f"Нет доступа к FTP-серверу {host}: {error}")


if __name__ == "__main__":
    main()
