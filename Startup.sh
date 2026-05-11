#!/bin/bash

echo "Starting discord bot"
echo "-|----------"
echo "--|---------"
echo "---|--------"
cd ~/SQUADD-BOT || exit 1
echo "----|-------"
echo "-----|------"
echo "------|-----"
echo "-------|----"
nohup /home/rocky/SQUADD-BOT/.venv/bin/python Main.py > bot.log 2>&1 &
echo "--------|---"
echo "---------|--"
echo "----------|-"
echo "Discord bot started successfully"
echo "Bot log:   ~/SQUADD-BOT/backend.log"