import os
import subprocess


def start_server():
    server_path = os.path.join(os.path.dirname(__file__), "..")
    command = "uvicorn main:app"
    subprocess.run(command, shell=True, cwd=server_path)


if __name__ == "__main__":
    start_server()
