#!/bin/bash

# A shell script to afk steam games
# Prereq:
# 1. Install the idle master
# 2. Create a file named id.txt and put all the app ids in it
# 3. Put this script in the same folder as steam-idle.exe
# 4. Run this script

# Continuous dots are redirected to Disk C
readonly FILE_PATH="..\..\..\..\LetterWang\Apps\idle_master\\\
idle_master_extended_v1.7\idle_master_extended_v1.7\\"
readonly APP_ID_FILE='id.txt'
readonly IDLE_MASTER="steam-idle.exe"

cd $FILE_PATH
while IFS= read -r line; do start $IDLE_MASTER $line >> /dev/null 2>&1; \
done < $APP_ID_FILE && exit