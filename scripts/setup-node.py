#! /usr/bin/env python
"""
Script to setup the node.

Run this script as sudo.
"""
from pathlib import Path
import subprocess
import shutil
import yaml

def symlink(target, path, force=True):
    """Creates the path a symlink to the target.

    If force is True, the existing file is removed before adding a symlink.
    """
    target = Path(target)
    path = Path(path)
    if path.is_dir():
        path = path / target.name
    if force:
        path.unlink(missing_ok=True)
    path.symlink_to(target)

def systemctl(*args):
    cmd = ["systemctl"] + list(args)
    subprocess.run(cmd)

def run_cmd(cmd):
    subprocess.run(cmd, shell=True)

def tljh_config():
    yaml.safe_load(open("/opt/tljh/config/config.yaml"))

def setup_livenotes():
    print
    print("Setting up live notes service")
    symlink("/opt/training/etc/systemd/system/live-notes.service", "/etc/systemd/system/")

    systemctl("daemon-reload")
    systemctl("enable", "live-notes.service")
    systemctl("start", "live-notes.service")

    domain = "notes.arcesium-lab.pipal.in"
    print(f"  setting up the domain {domain} ...")
    config = tljh_config()

    if domain not in config.get("https", {}).get("letsencrypt", {}).get("domains", []):
        run_cmd(f"tljh-config add-item https.letsencrypt.domains {domain}")

    # XXX: using cp as symlinking the file is not working
    shutil.copy("/opt/training/etc/tljh/state/rules/live-notes.toml", "/opt/tljh/state/rules/")

    run_cmd("tljh-config reload proxy"
    print(f"  The live notes will be live at https://$domain/ in a couple of seconds.")

def setup_magic_commands():
    # Setup /etc/skel so that new users will have startup script setup in their home dir
    # at ~/.ipython/profile_default/startup
    skel = Path(ROOT) / "etc" / "skel"
    shutil.copytree(skel, "/etc/skel")

ROOT = Path(__file__).parent.parent

print(f"The traning repo is at: {ROOT}")

echo "symlinking to /opt/training ..."
symlink(ROOT, "/opt/training", force=True)
run_cmd("ls -l /opt/training")

setup_livenotes()
setup_magic_commands()