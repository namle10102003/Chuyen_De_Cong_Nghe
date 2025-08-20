import os
import sys
import subprocess

def run_squashmigrations(app_label, migration_name):
    """Chạy lệnh squashmigrations cho app chỉ định."""
    result = subprocess.run(
        [sys.executable, "manage.py", "squashmigrations", app_label, migration_name],
        cwd=os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
        capture_output=True,
        text=True
    )
    print(result.stdout)
    if result.stderr:
        print(result.stderr)

if __name__ == "__main__":
    # Thay 'polls' và '0004' cho phù hợp với project của bạn
    run_squashmigrations("polls", "0004")
