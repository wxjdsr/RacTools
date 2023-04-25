#!/bin/bash

# A shell script to afk steam games

# Continuous dots are redirected to Disk C

# Note: the file path is hardcoded, change it to your own path
readonly FILE_PATH="..\..\..\..\LetterWang\Apps\idle_master\\\
idle_master_extended_v1.7\idle_master_extended_v1.7\\"
readonly APP_ID_FILE='id.txt'
readonly IDLE_MASTER="steam-idle.exe"

cd $FILE_PATH
while IFS= read -r line; do start $IDLE_MASTER $line >> /dev/null 2>&1; \
done < $APP_ID_FILE && exit