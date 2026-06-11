from __future__ import annotations

try:
    import paramiko  # type: ignore
    HAS_PARAMIKO = True
except ImportError:
    HAS_PARAMIKO = False


def run_ssh_command(
    host: str,
    username: str,
    command: str,
    password: str | None = None,
    key_path: str | None = None,
    port: int = 22,
    timeout: float = 10.0,
) -> tuple[str, str, int]:
    if not HAS_PARAMIKO:
        raise RuntimeError("Библиотека paramiko не установлена.")

    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        client.connect(
            hostname=host,
            port=port,
            username=username,
            password=password,
            key_filename=key_path,
            timeout=timeout,
        )
        stdin, stdout, stderr = client.exec_command(command, timeout=timeout)
        exit_code = stdout.channel.recv_exit_status()
        out = stdout.read().decode("utf-8", errors="replace")
        err = stderr.read().decode("utf-8", errors="replace")
        return out, err, exit_code
    finally:
        client.close()


def main() -> None:
    print(f"paramiko доступен: {HAS_PARAMIKO}")
    if not HAS_PARAMIKO:
        print("Для реального запуска установите: pip install paramiko")
        print("Пример вызова:")
        print('  out, err, code = run_ssh_command("example.com", "user", "uname -a", password="...")')
        return
    out, err, code = run_ssh_command("example.com", "user", "uname -a", password="secret")
    print(f"exit={code}\nstdout={out}\nstderr={err}")


if __name__ == "__main__":
    main()
