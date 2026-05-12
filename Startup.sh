#!/bin/bash

echo "[SQUADD-Startup] Starting discord bot"
echo "[SQUADD-Startup] -|----------"
echo "[SQUADD-Startup] --|---------"
echo "[SQUADD-Startup] ---|--------"
cd ~/SQUADD-BOT || exit 1
echo "[SQUADD-Startup] ----|-------"
echo "[SQUADD-Startup] -----|------"
echo "[SQUADD-Startup] ------|-----"
echo "[SQUADD-Startup] -------|----"
nohup /home/rocky/SQUADD-BOT/.venv/bin/python Main.py > bot.log 2>&1 &
echo "[SQUADD-Startup] --------|---"
echo "[SQUADD-Startup] ---------|--"
echo "[SQUADD-Startup] ----------|-"
echo "[SQUADD-Startup] Discord bot started successfully"
echo "[SQUADD-Startup] Bot log:   ~/SQUADD-BOT/backend.log"