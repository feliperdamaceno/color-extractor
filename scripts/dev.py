import os
import subprocess


def start_development():
    server_path = os.path.join(os.path.dirname(__file__), "..")
    command = "uvicorn main:app --reload"
    subprocess.run(command, shell=True, cwd=server_path)


if __name__ == "__main__":
    start_development()
