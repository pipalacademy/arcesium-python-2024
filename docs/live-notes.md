# Live Notes

The `scripts/setup-node.sh` setups the live notes.

```
$ sudo ./scripts/setup-node.sh
```

This setup the live-notes as a systemd service.

## Troubleshooting

Service status:

```
$ sudo systemctl status live-notes

● live-notes.service - Training Live Notes
     Loaded: loaded (/etc/systemd/system/live-notes.service; enabled; preset: enabled)
     Active: active (running) since Wed 2024-01-03 09:38:39 UTC; 7min ago
   Main PID: 152506 (quarto)
      Tasks: 7 (limit: 4539)
     Memory: 61.6M
        CPU: 3.759s
     CGroup: /system.slice/live-notes.service
             ├─152506 /bin/bash /usr/local/bin/quarto preview --port 4444
             └─152517 /opt/quarto/bin/tools/deno-x86_64-unknown-linux-gnu/deno run --unstable --no-config --cached-only --allow-read --allow-write --all>

Jan 03 09:38:39 arcesium-lab systemd[1]: Started live-notes.service - Training Live Notes.
Jan 03 09:38:41 arcesium-lab quarto[152517]: Preparing to preview
Jan 03 09:38:41 arcesium-lab quarto[152517]: Watching files for changes
Jan 03 09:38:41 arcesium-lab quarto[152517]: Browse at http://localhost:4444/
Jan 03 09:39:14 arcesium-lab quarto[152517]: GET: /
Jan 03 09:39:18 arcesium-lab quarto[152517]: GET: /
Jan 03 09:39:31 arcesium-lab quarto[152517]: GET: /
Jan 03 09:42:43 arcesium-lab quarto[152517]: GET: /
```

Restart the service:

```
$ sudo systemctl restart live-notes
```