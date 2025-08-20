def run_management_command(command):
    import subprocess
    import sys
    import os
    result = subprocess.run(
        [sys.executable, "manage.py"] + command,
        cwd=os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
        capture_output=True,
        text=True
    )
    print(result.stdout)
    if result.stderr:
        print(result.stderr)

if __name__ == "__main__":
    # Các lệnh migrate polls theo yêu cầu
    run_management_command(["migrate", "polls", "0002"])
    run_management_command(["migrate", "polls", "zero"])
    run_management_command(["migrate", "polls", "0002"])
import os
import sys
import subprocess

def run_management_command(command):
    """Chạy lệnh quản lý Django từ Python."""
    result = subprocess.run(
        [sys.executable, "manage.py"] + command,
        cwd=os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
        capture_output=True,
        text=True
    )
    print(result.stdout)
    if result.stderr:
        print(result.stderr)

if __name__ == "__main__":
    # Tạo migration cho app 'polls'
    run_management_command(["makemigrations", "polls"])
    # Áp dụng migration cho app 'polls'
    run_management_command(["migrate", "polls"])
    # Tạo migration với tên tùy chỉnh cho app 'polls'
    run_management_command(["makemigrations", "--name", "changed_poll_model", "polls"])