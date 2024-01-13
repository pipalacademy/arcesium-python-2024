#! /usr/bin/env python
import subprocess
import shutil
from pathlib import Path
import os
import sys

users = open("users.txt").read().strip().split()

files = """
a.txt
""".strip().split()
files = [f.strip() for f in files if not f.startswith("#") and f.strip() != ""]

FORCE = "--force" in sys.argv

def cmd(command):
    print("$", command)
    subprocess.call(command, shell=True)

def copyfile(path, user):
    src = Path("final") / path
    dest = Path("/home") / user / path

    if FORCE or not dest.exists():
        dest.parent.mkdir(exist_ok=True, parents=True)
        shutil.copyfile(src, dest)
        print("copy", src, dest)
    else:
        print(f"{dest} already present. ignoring...")
        return

def fix_perms(user):
    cmd(f"chown -R {user}:{user} /home/{user}")

def sync():
    for user in users:
        username = "jupyter-" + user
        for f in files:
            copyfile(f, username)
        # os.system(f"ln -s /opt/images /home/{username}/data-analysis/")
        #os.system(f"ln -s /opt/files /home/{username}/assignments")
        #os.system(f"cd /home/{username}/data-analysis/assignments && ln -sf ../data .")
        fix_perms(username)

sync()
