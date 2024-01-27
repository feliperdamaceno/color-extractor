import os
import subprocess


def build_client():
    client_path = os.path.join(os.path.dirname(__file__), "..", "client")
    build_command = "npm run build"
    subprocess.run(build_command, shell=True, cwd=client_path)


if __name__ == "__main__":
    build_client()
