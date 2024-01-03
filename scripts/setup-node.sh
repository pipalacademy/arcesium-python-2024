#! /bin/bash
#
# Script to setup the node
#
# Run this script as sudo
#

function setup_livenotes() {
    echo
    echo "Setting up live notes service"
    ln -sf /opt/training/etc/systemd/system/live-notes.service /etc/systemd/system/

    systemctl daemon-reload
    systemctl enable live-notes.service
    systemctl start live-notes.service

    domain=notes.arcesium-lab.pipal.in
    echo "  setting up the domain $domain ..."
    if ! tljh-config show | grep -q $domain
    then
        tljh-config add-item https.letsencrypt.domains $domain
    fi
    ln -sf /opt/training/etc/tljh/state/rules/live-notes.toml /opt/tljh/state/rules/
    tljh-config reload proxy
    echo "  The live notes will be live at https://$domain/ in a couple of seconds."
}

ROOT=$(realpath $(dirname $(dirname $0)))
echo "The traning repo is at: $ROOT"

echo "symlinking to /opt/training ..."
ln -sf $ROOT /opt/training
ls -l /opt/training

setup_livenotes