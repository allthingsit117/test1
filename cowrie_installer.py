#!/usr/bin/env python3
import subprocess
import sys

def run_cmd(cmd):
    print(f"\n[+] Running: {cmd}")
    result = subprocess.run(cmd, shell=True)
    if result.returncode != 0:
        print(f"[!] Command failed: {cmd}")
        sys.exit(1)

# 1. Install dependencies
run_cmd("sudo apt update && sudo apt install -y git python3 python3-venv python3-dev libssl-dev libffi-dev "
        "build-essential libpython3-dev authbind virtualenv libmpfr-dev libmpc-dev "
        "libssl-dev libffi-dev libjpeg-dev libxslt1-dev zlib1g-dev")

# 2. Create cowrie user
run_cmd("sudo adduser --disabled-password --gecos '' cowrie || true")

# 3. Switch to cowrie user and clone repo
run_cmd("sudo -u cowrie bash -c 'cd ~ && git clone https://github.com/cowrie/cowrie.git || true'")

# 4. Setup virtual environment
run_cmd("sudo -u cowrie bash -c 'cd ~/cowrie && python3 -m venv cowrie-env'")

# 5. Activate venv and install requirements
run_cmd("sudo -u cowrie bash -c 'cd ~/cowrie && source cowrie-env/bin/activate && "
        "pip install --upgrade pip setuptools wheel && pip install -r requirements.txt'")

# 6. Copy config file
run_cmd("sudo -u cowrie bash -c 'cd ~/cowrie/etc && cp cowrie.cfg.dist cowrie.cfg'")

print("\n[+] Cowrie installation complete!")
print("[*] To start Cowrie:")
print("    sudo su - cowrie")
print("    cd cowrie && bin/cowrie start")
print("[*] Status check:")
print("    bin/cowrie status")
